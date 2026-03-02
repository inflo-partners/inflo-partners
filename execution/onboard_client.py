#!/usr/bin/env python3
"""
Inflo Partners — Client Onboarding Automation
Parses Tally form CSV export and generates:
  1. Partner folder structure
  2. Populated PARTNER.md from form responses
  3. Auto-detected output style

Usage:
  python3 execution/onboard_client.py <path_to_tally_csv>

Processes ALL rows in the CSV (one client per row).
"""

import csv
import os
import re
import sys
import shutil

# --- Configuration ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENTS_DIR = os.path.join(BASE_DIR, "partners")
TEMPLATE_DIR = os.path.join(CLIENTS_DIR, "_template")

# Column name mappings (Tally question text → internal key)
# These match the column headers from the Tally CSV export
COLUMN_MAP = {
    "1. Legal business name": "business_name",
    "2. Business address": "address",
    "3. Primary business phone number": "phone",
    "4. Please attach your logo": "logo_url",
    "5. What do your company do?": "company_description",
    "6. What problem do you primarily solve for clients?": "problem_solved",
    "7. What is your target audience? ": "target_audience",
    "8. Describe your ideal client in detail": "ideal_client",
    "9. What pain points does your audience struggle with the most?": "pain_points",
    "10. What are your clients' dream outcomes?": "dream_outcomes",
    "11. Describe your product or service": "product_description",
    "12. What is your USP / unique mechanism?": "usp",
    "13. Why do traditional approaches in your industry fail?": "traditional_fail",
    "15. What was your starting point before entering this field?": "origin_story",
    "16. What did your timeline of growth look like?": "growth_timeline",
    "17. What are the average results your clients achieve?": "avg_results",
    "18. What is the most impressive client result story you've seen?": "best_result",
    "19. How is your offering structured?": "offer_structure",
    "20. What is the expected timeframe for clients to typically see results?": "time_to_results",
    "21. What is the expected timeline for clients from start to finish?": "full_timeline",
    "22. What is the market size and growth potential for your industry?": "market_size",
    "23. What current trends are impacting your industry right now?": "current_trends",
    "Is there any additional context or details you'd like to share that we haven't covered above that you think is important for us to know?": "additional_context",
}

# --- Output Style Auto-Detection ---
STYLE_KEYWORDS = {
    "financial-advisory": [
        "wealth", "tax", "financial", "advisory", "fiduciary", "estate planning",
        "retirement", "portfolio", "assets under management", "aum", "cfp",
    ],
    "coaching-fitness": [
        "coach", "coaching", "fitness", "training", "athlete", "transformation",
        "health", "wellness", "strength", "performance", "workout", "gym",
        "weight loss", "nutrition", "mindset",
    ],
    "saas-b2b": [
        "saas", "software", "platform", "b2b", "enterprise", "api",
        "subscription", "mrr", "arr", "churn", "onboarding",
    ],
    "real-estate-capital": [
        "real estate", "fund", "syndication", "investor", "accredited",
        "capital", "equity", "property", "commercial real estate", "self storage",
        "multifamily", "acquisition", "portfolio", "lp", "gp",
    ],
}


def detect_output_style(data: dict) -> str:
    """Auto-detect the output style based on keyword frequency in responses."""
    # Combine all text fields for analysis
    text = " ".join(str(v) for v in data.values()).lower()

    scores = {}
    for style, keywords in STYLE_KEYWORDS.items():
        score = sum(text.count(kw) for kw in keywords)
        scores[style] = score

    best_style = max(scores, key=scores.get)
    if scores[best_style] == 0:
        return "default"
    return best_style


def detect_industry(data: dict, style: str) -> str:
    """Infer a short industry label from the output style and company description."""
    industry_map = {
        "financial-advisory": "Wealth Management / Financial Advisory",
        "coaching-fitness": "Coaching / Fitness / Performance",
        "saas-b2b": "SaaS / B2B",
        "real-estate-capital": "Real Estate / Capital / Syndication",
        "default": "Services",
    }
    return industry_map.get(style, "Services")


def slugify(name: str) -> str:
    """Convert a business name to a folder-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)  # remove special chars
    slug = re.sub(r"[\s]+", "-", slug)  # spaces to hyphens
    slug = re.sub(r"-+", "-", slug)  # collapse multiple hyphens
    slug = slug.strip("-")
    return slug


def clean_multiline(text: str) -> str:
    """Clean up multi-line text from CSV — normalize line breaks."""
    if not text:
        return ""
    # Replace literal \n with actual newlines, strip excess whitespace
    text = text.replace("\\n", "\n")
    # Remove excessive blank lines (more than 2 in a row)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_case_studies(best_result: str, avg_results: str) -> list:
    """Extract individual case studies from the best result text."""
    studies = []
    if best_result:
        # Split on common separators
        parts = re.split(r"(?:Another|A third|Additionally|Also)[:\s]", best_result)
        for part in parts:
            part = part.strip()
            if len(part) > 20:
                # Truncate to first 2-3 sentences for the brief
                sentences = re.split(r"(?<=[.!?])\s+", part)
                summary = " ".join(sentences[:3])
                studies.append(summary)
    if not studies and best_result:
        studies.append(best_result.strip()[:500])
    return studies


def generate_partner_md(data: dict) -> str:
    """Generate a populated PARTNER.md from parsed Tally data."""
    style = detect_output_style(data)
    industry = detect_industry(data, style)

    # Extract case studies
    case_studies = extract_case_studies(
        data.get("best_result", ""),
        data.get("avg_results", ""),
    )
    case_study_lines = "\n".join(f"- {cs}" for cs in case_studies) if case_studies else "- [To be added]"

    # Build the PARTNER.md
    md = f"""# {data.get('business_name', '[Partner Name]')}

## Overview
- **Industry:** {industry}
- **Output Style:** {style}
- **Monthly Revenue:** [To be confirmed]
- **Website:** {data.get('website', '[To be confirmed]')}
- **Business Address:** {data.get('address', '[Not provided]')}
- **Phone:** {data.get('phone', '[Not provided]')}
- **Logo:** {data.get('logo_url', '/assets/logo.png')}

## Target Audience
- **Who:** {clean_multiline(data.get('target_audience', '[Not provided]'))}
- **Ideal Client Profile:** {clean_multiline(data.get('ideal_client', '[Not provided]'))}
- **Pain Points:** {clean_multiline(data.get('pain_points', '[Not provided]'))}
- **Dream Outcomes:** {clean_multiline(data.get('dream_outcomes', '')) or '[Not provided]'}

## Offer
- **What:** {clean_multiline(data.get('company_description', '[Not provided]'))}
- **Offer Structure:** {clean_multiline(data.get('offer_structure', '[Not provided]'))}
- **Price Point:** [Extract from offer structure above]
- **Time to Results:** {clean_multiline(data.get('time_to_results', '[Not provided]'))}
- **Full Timeline:** {clean_multiline(data.get('full_timeline', '[Not provided]'))}
- **CTA:** [Book a call / Watch VSL / Apply]
- **Booking URL:** [To be confirmed]

## Mechanism
- **USP / Unique Mechanism:** {clean_multiline(data.get('usp', '[Not provided]'))}
- **Why Traditional Approaches Fail:** {clean_multiline(data.get('traditional_fail', '[Not provided]'))}
- **Problem Solved:** {clean_multiline(data.get('problem_solved', '[Not provided]'))}

## Founder Story
- **Origin:** {clean_multiline(data.get('origin_story', '[Not provided]'))}
- **Growth Timeline:** {clean_multiline(data.get('growth_timeline', '[Not provided]'))}

## Proof / Case Studies
{case_study_lines}

## Average Client Results
{clean_multiline(data.get('avg_results', '[Not provided]'))}

## Key Stats
- [To be extracted from results data]

## Brand
- **Primary Color:** [To be confirmed]
- **Secondary Color:** [To be confirmed]
- **Tone Notes:** [See output style: {style}]

## Market Context
- **Market Size & Growth:** {clean_multiline(data.get('market_size', '[Not provided]'))}
- **Current Trends:** {clean_multiline(data.get('current_trends', '[Not provided]'))}

## Objections to Address
1. [To be identified from audience analysis]
2. [To be identified from audience analysis]
3. [To be identified from audience analysis]

## Notes
### Product / Service Details
{clean_multiline(data.get('product_description', '[Not provided]'))}

### Additional Context
{clean_multiline(data.get('additional_context', '[Not provided]'))}
"""
    return md


def scaffold_client_folder(client_slug: str) -> str:
    """Create the full client folder structure from template."""
    client_dir = os.path.join(CLIENTS_DIR, client_slug)

    if os.path.exists(client_dir):
        print(f"  [SKIP] Folder already exists: {client_dir}")
        return client_dir

    # Copy template structure
    shutil.copytree(TEMPLATE_DIR, client_dir)
    print(f"  [OK] Created folder: {client_dir}")
    return client_dir


def normalize_header(header: str) -> str:
    """Normalize CSV header — strip BOM, whitespace, newlines, smart quotes."""
    # Remove BOM
    header = header.lstrip("\ufeff")
    # Remove surrounding quotes that sometimes appear
    header = header.strip('"')
    # Normalize smart/curly apostrophes and quotes to straight versions
    header = header.replace("\u2018", "'").replace("\u2019", "'")  # single curly
    header = header.replace("\u201c", '"').replace("\u201d", '"')  # double curly
    # Collapse whitespace and newlines
    header = re.sub(r"[\n\r]+", " ", header)
    header = header.strip()
    return header


def post_process(data: dict) -> dict:
    """Fix common data issues — e.g., URL in address field."""
    # If the address looks like a URL, move it to website
    address = data.get("address", "")
    if address and re.match(r"https?://", address):
        data["website"] = address
        data["address"] = "[Not provided]"

    # If no website detected, try to find one in other fields
    if not data.get("website"):
        data["website"] = "[To be confirmed]"

    return data


def parse_csv(filepath: str) -> list:
    """Parse the Tally CSV export into a list of dicts with normalized keys."""
    clients = []

    # Build a normalized lookup for column mapping
    normalized_map = {}
    for key, value in COLUMN_MAP.items():
        normalized_map[normalize_header(key)] = value

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            data = {}
            for col_name, value in row.items():
                col_clean = normalize_header(col_name)
                if col_clean in normalized_map:
                    data[normalized_map[col_clean]] = value.strip() if value else ""

            if data.get("business_name"):
                data = post_process(data)
                clients.append(data)

    return clients


def onboard_clients(csv_path: str):
    """Main function — parse CSV and onboard all clients."""
    print(f"\n{'='*60}")
    print(f"  INFLO PARTNERS — CLIENT ONBOARDING")
    print(f"{'='*60}\n")
    print(f"CSV: {csv_path}\n")

    # Parse
    clients = parse_csv(csv_path)
    print(f"Found {len(clients)} client(s) in CSV.\n")

    for i, data in enumerate(clients, 1):
        name = data.get("business_name", "Unknown")
        slug = slugify(name)
        style = detect_output_style(data)

        print(f"--- Client {i}: {name} ---")
        print(f"  Slug: {slug}")
        print(f"  Detected Style: {style}")

        # Scaffold folder
        client_dir = scaffold_client_folder(slug)

        # Generate PARTNER.md
        partner_md = generate_partner_md(data)
        md_path = os.path.join(client_dir, "PARTNER.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(partner_md)
        print(f"  [OK] Generated PARTNER.md")

        print(f"  [OK] Ready for agents\n")

    print(f"{'='*60}")
    print(f"  ONBOARDING COMPLETE — {len(clients)} client(s) processed")
    print(f"{'='*60}\n")
    print("Next steps:")
    print("  1. Review each PARTNER.md and fill in [To be confirmed] fields")
    print("  2. Run @funnel-strategist for each client")
    print("  3. Build assets with the relevant agents")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 execution/onboard_client.py <path_to_tally_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print(f"Error: File not found: {csv_path}")
        sys.exit(1)

    onboard_clients(csv_path)
