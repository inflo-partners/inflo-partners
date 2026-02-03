#!/usr/bin/env python3
"""
Quality Gate Hook
Validates deliverables against quality standards before approval.

Checks:
- Word count requirements
- Readability scores
- Required sections present
- Format compliance
- Custom rules per deliverable type
"""

import json
import sys
import re
import os
from pathlib import Path

# Quality standards by deliverable type
QUALITY_STANDARDS = {
    "vsl": {
        "min_words": 3500,
        "max_reading_level": 6,  # Grade level
        "required_sections": [
            "HOOK",
            "PROBLEM",
            "SOLUTION",
            "PROOF",
            "OFFER",
            "CTA"
        ],
        "forbidden_words": [
            "revolutionary",
            "secret",
            "guaranteed results",
            "limited time only",
            "act now"
        ]
    },
    "landing_page": {
        "min_words": 500,
        "max_reading_level": 6,
        "required_sections": [
            "HERO",
            "PROOF",
            "CTA"
        ],
        "forbidden_words": []
    },
    "email": {
        "max_subject_length": 50,
        "min_words": 50,
        "max_words": 500,
        "max_reading_level": 5,
        "required_elements": [
            "subject",
            "preview",
            "cta"
        ]
    },
    "email_sequence": {
        "min_emails": 3,
        "max_emails": 15,
        "required_elements": [
            "trigger",
            "exit_conditions"
        ]
    }
}


def count_words(text):
    """Count words in text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def calculate_reading_level(text):
    """
    Estimate Flesch-Kincaid grade level.
    Simplified calculation for quick validation.
    """
    sentences = len(re.findall(r'[.!?]+', text)) or 1
    words = count_words(text)
    syllables = count_syllables(text)

    if words == 0:
        return 0

    # Flesch-Kincaid Grade Level formula
    grade = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
    return max(0, grade)


def count_syllables(text):
    """Estimate syllable count."""
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    count = 0
    for word in words:
        # Simple syllable estimation
        word = re.sub(r'[^a-z]', '', word)
        if len(word) <= 3:
            count += 1
        else:
            # Count vowel groups
            vowels = re.findall(r'[aeiouy]+', word)
            count += max(1, len(vowels))
    return count


def check_required_sections(text, required_sections):
    """Check if required sections are present."""
    text_upper = text.upper()
    missing = []
    for section in required_sections:
        if section.upper() not in text_upper:
            missing.append(section)
    return missing


def check_forbidden_words(text, forbidden_words):
    """Check for forbidden words/phrases."""
    text_lower = text.lower()
    found = []
    for word in forbidden_words:
        if word.lower() in text_lower:
            found.append(word)
    return found


def validate_vsl(content):
    """Validate VSL script."""
    standards = QUALITY_STANDARDS["vsl"]
    issues = []
    warnings = []

    # Word count
    word_count = count_words(content)
    if word_count < standards["min_words"]:
        issues.append(f"Word count: {word_count} (minimum: {standards['min_words']})")

    # Reading level
    reading_level = calculate_reading_level(content)
    if reading_level > standards["max_reading_level"]:
        issues.append(f"Reading level: {reading_level:.1f} (maximum: {standards['max_reading_level']})")

    # Required sections
    missing = check_required_sections(content, standards["required_sections"])
    if missing:
        issues.append(f"Missing sections: {', '.join(missing)}")

    # Forbidden words
    forbidden = check_forbidden_words(content, standards["forbidden_words"])
    if forbidden:
        warnings.append(f"Hype words found: {', '.join(forbidden)}")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
        "metrics": {
            "word_count": word_count,
            "reading_level": round(reading_level, 1)
        }
    }


def validate_landing_page(content):
    """Validate landing page copy."""
    standards = QUALITY_STANDARDS["landing_page"]
    issues = []
    warnings = []

    # Word count
    word_count = count_words(content)
    if word_count < standards["min_words"]:
        issues.append(f"Word count: {word_count} (minimum: {standards['min_words']})")

    # Reading level
    reading_level = calculate_reading_level(content)
    if reading_level > standards["max_reading_level"]:
        warnings.append(f"Reading level: {reading_level:.1f} (target: {standards['max_reading_level']})")

    # Required sections
    missing = check_required_sections(content, standards["required_sections"])
    if missing:
        warnings.append(f"Consider adding: {', '.join(missing)}")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
        "metrics": {
            "word_count": word_count,
            "reading_level": round(reading_level, 1)
        }
    }


def validate_email(content):
    """Validate single email."""
    standards = QUALITY_STANDARDS["email"]
    issues = []
    warnings = []

    # Extract subject line (assuming format: Subject: xxx)
    subject_match = re.search(r'Subject:\s*(.+?)(?:\n|$)', content, re.IGNORECASE)
    if subject_match:
        subject = subject_match.group(1).strip()
        if len(subject) > standards["max_subject_length"]:
            issues.append(f"Subject too long: {len(subject)} chars (max: {standards['max_subject_length']})")
    else:
        issues.append("No subject line found")

    # Word count
    word_count = count_words(content)
    if word_count < standards["min_words"]:
        issues.append(f"Email too short: {word_count} words")
    if word_count > standards["max_words"]:
        warnings.append(f"Email may be too long: {word_count} words")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
        "metrics": {
            "word_count": word_count
        }
    }


def validate_deliverable(deliverable_type, content_or_path):
    """Main validation entry point."""
    # Load content if path provided
    if os.path.exists(content_or_path):
        with open(content_or_path, 'r') as f:
            content = f.read()
    else:
        content = content_or_path

    validators = {
        "vsl": validate_vsl,
        "landing_page": validate_landing_page,
        "email": validate_email
    }

    if deliverable_type not in validators:
        return {
            "valid": False,
            "issues": [f"Unknown deliverable type: {deliverable_type}"],
            "warnings": []
        }

    return validators[deliverable_type](content)


def format_result(result):
    """Format validation result for display."""
    output = []

    if result["valid"]:
        output.append("✓ PASSED: Deliverable meets quality standards")
    else:
        output.append("✗ FAILED: Quality issues found")

    if result.get("metrics"):
        output.append("\nMetrics:")
        for key, value in result["metrics"].items():
            output.append(f"  {key}: {value}")

    if result["issues"]:
        output.append("\nIssues (must fix):")
        for issue in result["issues"]:
            output.append(f"  ✗ {issue}")

    if result["warnings"]:
        output.append("\nWarnings (consider fixing):")
        for warning in result["warnings"]:
            output.append(f"  ⚠ {warning}")

    return "\n".join(output)


def main():
    if len(sys.argv) < 3:
        print("Usage: quality_gate.py <type> <file_or_content>")
        print("Types: vsl, landing_page, email")
        sys.exit(1)

    deliverable_type = sys.argv[1]
    content_or_path = sys.argv[2]

    result = validate_deliverable(deliverable_type, content_or_path)
    print(format_result(result))

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
