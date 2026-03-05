/**
 * Club Kaya — Onboarding Assessment Form Generator
 *
 * HOW TO USE:
 * 1. Go to https://script.google.com
 * 2. Click "New Project"
 * 3. Delete the default code
 * 4. Paste this entire script
 * 5. Click "Run" (the play button)
 * 6. It will ask for permissions — click "Allow"
 * 7. Check your Google Drive — the form will be there called "Club Kaya — Onboarding Assessment"
 * 8. Open the form, review it, and grab the shareable link
 */

function createClubKayaOnboardingForm() {
  var form = FormApp.create('Club Kaya — Onboarding Assessment');
  form.setDescription(
    'Welcome to Club Kaya. This assessment helps us build your personalized performance system. ' +
    'Please answer every question honestly and thoroughly — the more detail you give, the better your program will be.\n\n' +
    'This takes about 10-15 minutes. Take your time.'
  );
  form.setConfirmationMessage('Thank you! Your assessment has been submitted. We\'re building your personalized program now.');
  form.setAllowResponseEdits(false);
  form.setLimitOneResponsePerUser(false);
  form.setProgressBar(true);

  // ==========================================
  // SECTION 1: BASICS
  // ==========================================
  form.addPageBreakItem().setTitle('Basic Information');

  // Q1 - Weight
  form.addTextItem()
    .setTitle('Weight')
    .setHelpText('Please convert if you use the metric system. Your account settings will soon be switched to the metric system for check-ins, workouts, and related metrics. Don\'t worry!')
    .setRequired(true);

  // Q2 - Height
  form.addTextItem()
    .setTitle('Height')
    .setHelpText('Please convert if you use the metric system. Your account settings will soon be switched to the metric system for check-ins, workouts, and related metrics. Don\'t worry!')
    .setRequired(true);

  // Q3 - Sex
  form.addMultipleChoiceItem()
    .setTitle('Sex')
    .setChoiceValues(['Male', 'Female', 'Intersex', 'Prefer not to say'])
    .setRequired(true);

  // Q4 - Gender Identity
  form.addMultipleChoiceItem()
    .setTitle('Gender Identity')
    .setChoiceValues(['Man', 'Woman', 'Non-binary', 'Another identity', 'Prefer not to say'])
    .setRequired(true);

  // Q5 - Age
  form.addTextItem()
    .setTitle('Age')
    .setRequired(true);

  // Q6 - Time Zone
  form.addTextItem()
    .setTitle('Time Zone')
    .setHelpText('Please also give location! Examples: GMT (UTC+0), EST (UTC-5), CST (UTC-6), MST (UTC-7), and PST (UTC-8)')
    .setRequired(true);

  // Q7 - Body Fat Estimate
  form.addMultipleChoiceItem()
    .setTitle('Right now, I estimate my body fat category to be')
    .setChoiceValues(['Lean', 'Average', 'Above Average', 'Very High'])
    .setRequired(true);

  // ==========================================
  // SECTION 2: GOALS & OPTIMIZATION
  // ==========================================
  form.addPageBreakItem().setTitle('Goals & Optimization');

  // Q8 - 90-Day Goal
  form.addMultipleChoiceItem()
    .setTitle('Over the next 90 days, I am most concerned with...')
    .setHelpText('Specific health desires in addition to body composition outlined in next question.')
    .setChoiceValues([
      'Gaining muscle and losing fat',
      'Gaining weight (mostly muscle)',
      'Only losing body fat while preserving muscle',
      'No change in body composition desired, seeking other health optimization'
    ])
    .setRequired(true);

  // Q9 - Help Specifically With (multi-select)
  form.addCheckboxItem()
    .setTitle('I need help specifically with')
    .setHelpText('Choose only TOP priorities and/or struggles')
    .setChoiceValues([
      'Very concerned with body composition (muscle gain and/or fat loss)',
      'Gut Health',
      'Skincare',
      'Hormone Health',
      'Non Toxic Living Swaps',
      'Consistent Energy Levels',
      'Insulin',
      'Sleep',
      'Longevity',
      'Mental Presence',
      'Athletic Movement',
      'Mobility'
    ])
    .setRequired(true);

  // Q10 - Other Desires
  form.addParagraphTextItem()
    .setTitle('Any other desires you want/need for your health that were not covered?')
    .setHelpText('OPTIONAL: If you could snap your fingers, who are you in 90 days?')
    .setRequired(false);

  // Q11 - Injuries
  form.addParagraphTextItem()
    .setTitle('Any current injuries? If yes, please describe. If none, type "NA"')
    .setRequired(true);

  // ==========================================
  // SECTION 3: NUTRITION & DIET
  // ==========================================
  form.addPageBreakItem().setTitle('Nutrition & Diet');

  // Q12 - Diet Type
  form.addMultipleChoiceItem()
    .setTitle('I am a')
    .setChoiceValues([
      'Standard Omnivore (No dietary needs)',
      'Vegetarian',
      'Vegan',
      'Pescatarian',
      'Keto',
      'Gluten Sensitive',
      '100% Gluten Intolerant',
      'Dairy Sensitive',
      '100% Lactose Intolerant',
      'Diabetic'
    ])
    .setRequired(true);

  // Q13 - Allergies
  form.addParagraphTextItem()
    .setTitle('Any allergies or foods you absolutely hate?')
    .setHelpText('Canned sardines? Carrots? Turkey? Beets? Cottage cheese? If nothing, please put "NA"')
    .setRequired(true);

  // Q14 - Full Day of Eating
  form.addParagraphTextItem()
    .setTitle('Detail a regular full day of eating')
    .setRequired(true);

  // Q15 - Meal Control
  form.addParagraphTextItem()
    .setTitle('What meals throughout the day are in your control to cook or meal prep? What meals are outside your control (Takeout, restaurant, or catered needed because you are too busy)')
    .setHelpText('Please explain which meal structure works with schedule. Can you meal prep everything and cook everything at home? Are there certain meals that always need to be catered or ordered from a restaurant or meal service? Are you comfortable skipping breakfast?')
    .setRequired(true);

  // Q16 - Meals Per Day (multi-select)
  form.addCheckboxItem()
    .setTitle('How many meals a day work for your schedule and desires (select multiple if applicable, depending on day of the week)')
    .setChoiceValues([
      '1 large meal (OMAD)',
      '2 big meals',
      '3-4 smaller meals (2-4 meals and a snack)'
    ])
    .setRequired(true);

  // Q17 - Protein Intake
  form.addMultipleChoiceItem()
    .setTitle('How much protein do you get in a day?')
    .setChoiceValues([
      'About 1 gram per lb. of body weight (1 gram per 0.5 kg of body weight)',
      'More than 1 gram per lb. of body weight',
      'Less than I should',
      'I don\'t know or track'
    ])
    .setRequired(true);

  // Q18 - Cooking Oils (multi-select)
  form.addCheckboxItem()
    .setTitle('What cooking oils do you use in your kitchen?')
    .setHelpText('You can select multiple')
    .setChoiceValues([
      'Canola, Sesame, Corn, Vegetable, Soybean, Cottonseed, Peanut, Grapeseed, Sunflower',
      'Grass Fed Tallow, Grass Fed Butter, Extra virgin Cold Pressed Coconut Oil, Grass Fed Ghee, Cold Pressed Macadamia Nut Oil',
      'Extra Virgin Cold Pressed Olive Oil (room temperature meal add-on)',
      'Extra Virgin Cold Pressed Olive Oil (for cooking and room temperature add-on)'
    ])
    .setRequired(true);

  // Q19 - Eating Habits
  form.addMultipleChoiceItem()
    .setTitle('What describes your eating habits best?')
    .setChoiceValues(['I overeat', 'I undereat', 'Unsure'])
    .setRequired(true);

  // Q20 - Supplements
  form.addParagraphTextItem()
    .setTitle('Current supplements (Brands, timing, and dosages if you know amounts) & protein powder/bars')
    .setRequired(true);

  // Q21 - Electrolytes
  form.addTextItem()
    .setTitle('Do you take electrolytes? If yes, what brand?')
    .setHelpText('Please type "No" if you do not.')
    .setRequired(true);

  // ==========================================
  // SECTION 4: TRAINING & GYM
  // ==========================================
  form.addPageBreakItem().setTitle('Training & Gym');

  // Q22 - Gym Setup
  form.addParagraphTextItem()
    .setTitle('Current Gym Setup (Do you have any equipment at home? What equipment? Do you have a gym membership? What gym and location?) Please send a video in our chat showing all the at-home equipment!')
    .setHelpText('Please let me know if you would like to do workouts BOTH at home and at the gym.')
    .setRequired(true);

  // Q23 - Weightlifting Experience
  form.addScaleItem()
    .setTitle('Past weightlifting experience')
    .setBounds(1, 10)
    .setRequired(true);

  // Q24 - Fasted Workouts
  form.addMultipleChoiceItem()
    .setTitle('Do you ever workout fasted? (Without having eaten that day)')
    .setHelpText('and Do you ever consistently run, play sports, attend yoga, weight lift, or etc without having eaten since the day before.')
    .setChoiceValues([
      'Yes',
      'No',
      'Yes and I prefer working out this way'
    ])
    .setRequired(true);

  // ==========================================
  // SECTION 5: LIFESTYLE & ACTIVITY
  // ==========================================
  form.addPageBreakItem().setTitle('Lifestyle & Activity');

  // Q25 - Job / Schedule
  form.addParagraphTextItem()
    .setTitle('What\'s your job? Typical work hours & schedule?')
    .setRequired(true);

  // Q26 - Steps Per Day
  form.addMultipleChoiceItem()
    .setTitle('How many steps do you take on average each day? (Please take your best guess! FYI, 10,000 steps is 5 miles or 8km)')
    .setChoiceValues([
      'Under 3,000',
      '5,000 to 8,000',
      '10,000+',
      '15,000+'
    ])
    .setRequired(true);

  // Q27 - Non-Exercise Activity Level
  form.addParagraphTextItem()
    .setTitle('What is your typical non-exercise activity level during the day? (How long are you sitting each day? Are you walking throughout the day for lunch, public transportation, or any other reason? How often are you sitting vs moving? Do you tend to fidget?)')
    .setRequired(true);

  // Q28 - Weekly Workout Routine
  form.addParagraphTextItem()
    .setTitle('What is your typical weekly workout routine? (Include frequency, type, and duration of training — e.g., strength, cardio, classes, etc.)')
    .setRequired(true);

  // ==========================================
  // SECTION 6: SLEEP, ENERGY & HABITS
  // ==========================================
  form.addPageBreakItem().setTitle('Sleep, Energy & Habits');

  // Q29 - Caffeine
  form.addScaleItem()
    .setTitle('How many servings of caffeine do you typically have a day?')
    .setBounds(1, 10)
    .setRequired(true);

  // Q30 - Morning Light
  form.addMultipleChoiceItem()
    .setTitle('How often do you get morning light?')
    .setChoiceValues([
      'Every morning, I make sure to get 10-15 minutes of direct sunlight on my eyes (not through a window)',
      '50% of the time I make sure to get outside in the morning',
      'I don\'t include this in my routine'
    ])
    .setRequired(true);

  // Q31 - Energy
  form.addParagraphTextItem()
    .setTitle('How is your energy throughout the day? Do you ever crash? When?')
    .setRequired(true);

  // Q32 - Sleep Rating
  form.addScaleItem()
    .setTitle('Rate your current sleep schedule? (Consider hours slept, how you feel in the morning, etc.)')
    .setBounds(1, 10)
    .setRequired(true);

  // Q33 - Time to Fall Asleep
  form.addMultipleChoiceItem()
    .setTitle('Approximately how long does it take for you to fall asleep?')
    .setHelpText('(When you are actually in bed with your eyes closed, not scrolling on your phone)')
    .setChoiceValues(['5 minutes', '15 minutes', '30 minutes', '1 hour'])
    .setRequired(true);

  // Q34 - Nighttime Light Habits
  form.addMultipleChoiceItem()
    .setTitle('Which one best describes your nighttime habits?')
    .setChoiceValues([
      'I keep all my lights on in the evening (all my lightbulbs are LEDs and Fluorescents), I don\'t switch my phone and laptop to red mode, and I don\'t own blue light blocking glasses',
      'I have a full spectrum lamp or incandescent light bulbs at my desk and in my bedroom (no forms of LEDs or Fluorescents in the evening), I wear blue light blockers after sunset, and I have turned on the red screen shortcut on both my phone and laptop',
      'I am aware of reducing blue light exposure in the evening, but I am not very strict with it (sometimes blue light blockers, I lower the lights in the evening, I try not to scroll in bed)'
    ])
    .setRequired(true);

  // Q35 - Nighttime Routine
  form.addParagraphTextItem()
    .setTitle('Do you have a nighttime routine? If yes, please describe.')
    .setRequired(true);

  // Q36 - Alcohol
  form.addMultipleChoiceItem()
    .setTitle('Do you drink alcohol?')
    .setChoiceValues([
      'No',
      'Yes, but I am willing to do 90 days of sobriety',
      'Yes, and I\'m unable to break from alcohol at this time'
    ])
    .setRequired(true);

  // Q37 - Nicotine
  form.addMultipleChoiceItem()
    .setTitle('Do you use nicotine? If yes, how often and what form?')
    .setChoiceValues([
      'No',
      'Yes, I use pouches',
      'Yes, I smoke cigarettes',
      'Yes, I vape'
    ])
    .setRequired(true);

  // Q38 - Travel
  form.addParagraphTextItem()
    .setTitle('What is your travel schedule the next 90 days? Or any trips that may come up for work/family/vacation.')
    .setRequired(true);

  // ==========================================
  // DONE
  // ==========================================

  Logger.log('Form created successfully!');
  Logger.log('Form URL: ' + form.getPublishedUrl());
  Logger.log('Edit URL: ' + form.getEditUrl());

  // Also create a connected Google Sheet for responses
  var ss = SpreadsheetApp.create('Club Kaya — Onboarding Responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Response spreadsheet created: ' + ss.getUrl());
  Logger.log('');
  Logger.log('=== SETUP COMPLETE ===');
  Logger.log('Form link (share with clients): ' + form.getPublishedUrl());
  Logger.log('Edit form: ' + form.getEditUrl());
  Logger.log('View responses: ' + ss.getUrl());
}
