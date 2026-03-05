# Club Kaya — Google Sheets Specification

## Sheet 1: "Process Queue" (Trigger Sheet)

This is the "go button." When a client completes their Everfit onboarding form, paste their email here. Zapier triggers on new rows.

### Columns

| Column | Header | Description | Who fills it |
|---|---|---|---|
| A | `client_email` | Client's email (must match Everfit) | Coach/assistant |
| B | `client_name` | Client name (for reference) | Coach/assistant |
| C | `date_added` | Date pasted | Coach/assistant |
| D | `status` | "pending" → "processed" (Zapier updates) | Auto |

### Setup
1. Create a new Google Sheet called "Club Kaya - Process Queue"
2. Add the headers above in Row 1
3. Connect to Zapier: Trigger = "New Spreadsheet Row" in this sheet

---

## Sheet 2: "Parsed Assignments" (Intermediary Sheet)

Zap 1 writes the AI-parsed output here. Zaps 2-5 all trigger from new rows in this sheet.

### Columns

| Column | Header | Description |
|---|---|---|
| A | `client_email` | Client email |
| B | `client_name` | Client name |
| C | `date_processed` | Timestamp |
| D | `cat1_sex` | M or F |
| E | `cat2_goal` | C, B, or N |
| F | `cat3_diet` | S, V, V+, P, KETO, GF, L, D |
| G | `cat4_optimization` | Comma-separated or "none" |
| H | `cat5a_additional` | Comma-separated or "none" |
| I | `cat5z_restrictions` | Free text or "none" |
| J | `cat6_gym` | H, G, g, T, H-eq |
| K | `cat7_split` | FB4, M, F, FBC1, FBC2 |
| L | `cat8_calories` | 1400-3200 bucket |
| M | `cat9_meals` | 1, 2, 2.5, 3, 3.5, 4 |
| N | `cat10_meal_prep` | H, MP, C, or combination |
| O | `naming_tracker` | Full Kaya Tracker string |
| P | `naming_movement` | Full Kaya Movement string |
| Q | `naming_fuel` | Full Kaya Fuel string |
| R | `tdee_calculated` | Raw TDEE number |
| S | `calorie_target` | Goal-adjusted, bucketed |
| T | `mod_nutrition_protein` | true/false |
| U | `mod_volume_hacking` | true/false |
| V | `mod_brand_switching` | true/false |
| W | `mod_fasted_lifting` | true/false |
| X | `mod_caffeine` | true/false |
| Y | `mod_morning_light` | true/false |
| Z | `mod_energy_consistency` | true/false |
| AA | `mod_sleep` | true/false |
| AB | `mod_alcohol` | true/false |
| AC | `mod_nicotine` | true/false |
| AD | `mod_travel` | true/false |
| AE | `flags_for_review` | Free text or "none" |

### Setup
1. Create a new Google Sheet called "Club Kaya - Parsed Assignments"
2. Add all headers above in Row 1
3. Connect to Zapier: Zap 1 writes rows here, Zaps 2-5 trigger from new rows

---

## Sheet 3: "Everfit Assignment Map" (Reference Sheet)

Maps module codes to Everfit asset names. Used by Zapier Lookup Tables to convert AI output codes into the exact Everfit asset to assign.

### Columns

| Column | Header | Description |
|---|---|---|
| A | `code` | Module code (e.g., 1M, 2C, 3S, 7FB4) |
| B | `everfit_name` | Exact name in Everfit |
| C | `everfit_type` | Program, Resource Collection, or Workout Collection |
| D | `exists` | Yes/No (track what's been built) |

### Pre-fill with all codes from module-inventory.md
This sheet becomes the source of truth for which modules exist and what they're called in Everfit. Update the `exists` column as modules are built.

---

## Zapier Connection Summary

| Zap | Reads From | Writes To |
|---|---|---|
| Zap 1: Parser | Process Queue (trigger) + Everfit (Get Client Info) | Parsed Assignments |
| Zap 2: Core Assigner | Parsed Assignments (trigger) | Everfit (assign modules) |
| Zap 3: Product-Specific | Parsed Assignments (trigger) | Everfit (assign modules) |
| Zap 4: Conditional Modules | Parsed Assignments (trigger) | Everfit (assign modules) |
| Zap 5: Coach Notification | Parsed Assignments (trigger) | Slack/Email to Mitchell |
