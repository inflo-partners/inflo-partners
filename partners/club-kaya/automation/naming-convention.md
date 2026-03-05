# Club Kaya — Naming Convention System

## Overview

Three product lines, each pulling from different categories. Final output always uses dashes between categories.

---

## Product Lines

| Product Line | Categories Used | Purpose |
|---|---|---|
| **Kaya Tracker** | 1, 2, 3, 4, 5 | Habits, tracking, optimization |
| **Kaya Movement** | 1, 5(Z only), 6, 7 | Training, workouts |
| **Kaya Fuel** | 1, 2, 3, 5, 8, 9, 10 | Nutrition, meal plans |

---

## Category Definitions

### 1 SEX
| Code | Meaning |
|---|---|
| M | Male |
| F | Female |

### 2 GOAL
| Code | Meaning |
|---|---|
| C | Needs to lose fat (calorie deficit) |
| B | Needs to gain muscle/weight (maintenance or tiny surplus) |
| N | No weight change goal |

### 3 DIET
| Code | Meaning |
|---|---|
| S | Standard omnivore |
| V | Vegetarian |
| V+ | Vegan |
| P | Pescatarian |
| KETO | Ketogenic |
| GF | Gluten free |
| L | Lactose intolerant |
| D | Diabetic |

### 4 OPTIMIZATION
| Code | Meaning |
|---|---|
| O:{specific} | Health desire + optimization area |

Examples: O:{gut}, O:{sleep}, O:{mental health}, O:{hormone}, O:{inflammation}, O:{energy}

### 5 ADDITIONAL DESIRE
| Code | Meaning |
|---|---|
| A:{protocol} | Add a specific protocol |
| Z:{restriction} | Cannot have / restriction / allergy |

A examples: A:{magnesium}, A:{skincare}, A:{meditation}
Z examples: Z:{shellfish}, Z:{fasting}, Z:{eating window}, Z:{heavy weight}

Multiple can be combined: 5A:{skincare} Z:{shellfish + eating window}

### 6 GYM
| Code | Meaning |
|---|---|
| H | Home, no equipment |
| G | Regular commercial gym |
| g | Gym with lack of equipment |
| T(equipment) | Travel plan with specified equipment |
| H(equipment) | Home gym with specified equipment |

T examples: T(bands+bodyweight), T(pull up bar + dumbbells)
H examples: H(pull up bar + dumbbells + bench + cable machines)

### 7 SPLIT
| Code | Meaning |
|---|---|
| FB4 | 4-day full body split |
| M | 3-day Menzer method |
| F | 3-day home mobility |
| FBC1 | Full body circuits, basic (beginner/overweight) |
| FBC2 | Full body circuits, advanced (pike pushups, ninja pushups, etc.) |

FBC is for travel or clients that use dumbbell/bodyweight circuits.

### 8 TOTAL CALORIES
Calculated via TDEE (Mifflin-St Jeor), rounded to nearest bucket:
1400, 1600, 1800, 2000, 2200, 2500, 2800, 3000, 3200

### 9 MEALS PER DAY
| Code | Meaning |
|---|---|
| 1 | One meal per day (OMAD) |
| 2 | Two meals per day |
| 2.5 | Two meals and a snack |
| 3 | Three meals a day |
| 3.5 | Three meals and a snack |
| 4 | Two meals and two snacks |

Combinations indicate day-by-day variation:
- 9{3+2} = 3 meals weekdays, 2 meals weekends
- 9{2.5+2+1} = 2.5 weekdays, 2 Saturdays, OMAD Sundays

### 10 MEAL PREP TYPE
| Code | Meaning |
|---|---|
| H | Home cooked meals |
| MP | Meal prep options |
| C | Eating out often or catered meals |

Can combine: 10{H+MP}, 10{MP+C}

---

## Full Examples

**Kaya Tracker:**
```
Kaya Tracker 1M-2C-3S-4O:{gut} 5A:{skincare} Z:{shellfish + eating window}
Kaya Tracker 1F-2B-3GF 4O:{sleep} 5A:{OMAD+low glycemic carbs}
```

**Kaya Movement:**
```
Kaya Movement 1M-5Z:{hips}-6G-7FB4
Kaya Movement 1M-6T(bands+bodyweight)-FBC2
Kaya Movement 1M-6T(pull up bar + bodyweight)-FBC1
```

**Kaya Fuel:**
```
Kaya Fuel 1M-2C-3S-5A:{skincare} Z:{canned fish}-8{2500}-9{2.5+2}-10{H+MP}
```

---

## Onboarding Form Question Mapping

| Category | Form Questions |
|---|---|
| 1 SEX | Q3 |
| 2 GOAL | Q8, Q9 |
| 3 DIET | Q12, Q13 |
| 4 OPTIMIZATION | Q9, Q10 |
| 5A ADDITIONAL | Q0 |
| 5Z RESTRICTIONS | Q11, Q13, Q15 |
| 6 GYM | Q22, Q38 |
| 7 SPLIT | Q3, Q22, Q23, Q38 |
| 8 CALORIES (TDEE) | Q1, Q2, Q3, Q5, Q7, Q8, Q25, Q26, Q27, Q28 |
| 9 MEALS/DAY | Q14, Q15, Q16 |
| 10 MEAL PREP | Q14, Q15, Q16 |

---

## Conditional Module Triggers

| Question(s) | Condition | Module to Assign |
|---|---|---|
| Q16 | Needs nutrition/protein education | Nutrition & Protein Info |
| Q18 | Needs volume hacking | Volume Hacking (Jet Fuel Bowl) |
| Q19, Q20 | Needs brand switching | Brand Switching Guide |
| Q23 | Trains fasted | Fasted Weightlifting Protocol |
| Q28 | Caffeine issues | Caffeine Optimization |
| Q29 | No morning sunlight | Morning Light Education |
| Q30 | Inconsistent energy | Energy Consistency Protocol |
| Q31, Q32, Q33, Q34 | Sleep issues | Sleep Protocol |
| Q35 | Regular alcohol | Alcohol Module |
| Q36 | Uses nicotine | Nicotine Protocol (fat loss) |
| Q37 | Frequent travel | Travel Workouts, Meal Plans, Resources |
