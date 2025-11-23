"""
PCOS Knowledge Base
Contains comprehensive information about Polycystic Ovary Syndrome sourced from
medical research, clinical guidelines, and community experiences.
"""

PCOS_KNOWLEDGE = {
    "what_is_pcos": {
        "simple_explanation": """
PCOS stands for Polycystic Ovary Syndrome. I know it sounds super complicated, but let me break it down for you like we're chatting over lunch! 🍕

Basically, PCOS is when your hormones (the chemical messengers in your body) get a little out of whack. It's one of the most common hormone conditions - about 1 in 10 women have it! So you're definitely not alone.

Here's what's happening: Your ovaries (those small organs that hold eggs) might make too much of certain hormones called androgens. Think of androgens as the "boy hormones" - everyone has them, but with PCOS, you might have a bit more than usual.

This can cause a few things:
- Your periods might be irregular or skip around
- You might get small fluid-filled sacs (they call them "cysts" but they're really just follicles) on your ovaries
- You might notice extra hair growth or acne

But here's the important thing - PCOS is super manageable! Lots of people live totally normal, happy lives with it. It just means you need to pay a bit more attention to your body and maybe make some tweaks to how you take care of yourself.
        """,
        "medical_definition": "Polycystic Ovary Syndrome is the most common endocrine disorder affecting 6-13% of reproductive-aged women. It's characterized by hormonal imbalances, irregular ovulation, and often polycystic ovaries.",
        "sources": ["WHO", "NIH", "Mayo Clinic"]
    },

    "diagnosis": {
        "criteria": """
So, how do doctors figure out if you have PCOS? They use something called the "Rotterdam Criteria" - fancy name, I know!

To get diagnosed, you usually need to have at least 2 out of these 3 things:

1. IRREGULAR PERIODS 📅
   - Your periods are super unpredictable
   - They come more than 35 days apart (or less than 21 days)
   - Or sometimes you skip them entirely
   - This happens because you're not ovulating regularly

2. HIGH ANDROGENS (those "boy hormones" I mentioned) 💪
   - This can show up as:
     • Extra hair on your face, chest, or back (called hirsutism)
     • Acne that won't quit
     • Hair thinning on your head
   - Or it might just show up in a blood test

3. POLYCYSTIC OVARIES 🔬
   - An ultrasound might show lots of small follicles on your ovaries
   - Or you might have high AMH levels (a hormone test)
   - Fun fact: You can have PCOS without having "polycystic ovaries" - confusing, right?

The doctor will also want to rule out other conditions that can look similar, like thyroid problems or other hormone issues.

If you're a teenager, diagnosis can be trickier because your body is still figuring things out! Doctors are usually more careful about diagnosing teens.
        """,
        "tests": [
            "Blood tests (hormone levels, including testosterone, LH, FSH)",
            "Ultrasound of ovaries",
            "AMH (Anti-Müllerian Hormone) test",
            "Glucose and insulin tests",
            "Thyroid function tests",
            "Prolactin levels"
        ],
        "sources": ["2023 International PCOS Guidelines", "ASRM", "NHS"]
    },

    "symptoms": {
        "common": """
Okay, let's talk about what PCOS can actually feel like. Everyone's experience is different - you might have some of these, all of these, or just a few!

PERIOD STUFF 🩸
- Irregular periods (they come whenever they want, basically)
- Heavy periods when they do show up
- Sometimes no periods for months
- Painful cramps

SKIN & HAIR CHANGES 💇‍♀️
- Acne (especially along your jawline and chin)
- Extra hair growth on face, chest, belly, or back
- Hair thinning or loss on your head (usually at the crown)
- Skin tags (little skin bumps)
- Dark, velvety patches of skin (usually in skin folds)

WEIGHT & ENERGY 💪
- Weight gain, especially around your belly
- Difficulty losing weight even when you try hard
- Feeling tired a lot
- Cravings, especially for carbs and sweets

MOOD STUFF 🧠
- Anxiety or feeling worried a lot
- Depression or feeling down
- Mood swings
- Brain fog (trouble concentrating)

OTHER THINGS 🌙
- Trouble sleeping or sleep apnea
- Headaches
- Pelvic pain

Remember: Having PCOS doesn't mean you'll have ALL of these symptoms. And many of these can be managed with the right approach!
        """,
        "symptom_list": [
            "Irregular or absent menstrual periods",
            "Heavy menstrual bleeding",
            "Excess facial and body hair (hirsutism)",
            "Acne",
            "Male-pattern baldness or hair thinning",
            "Weight gain or difficulty losing weight",
            "Darkening of skin (acanthosis nigricans)",
            "Skin tags",
            "Infertility or difficulty getting pregnant",
            "Anxiety and depression",
            "Sleep problems",
            "Fatigue"
        ]
    },

    "medications": {
        "overview": """
Let me walk you through the main medications doctors might suggest for PCOS. Think of these as tools in your toolbox - your doctor will help you pick the right ones for YOUR situation!
        """,
        "metformin": {
            "friendly_explanation": """
METFORMIN - The Insulin Helper 💊

What is it?
Metformin is actually a diabetes medication, but it works really well for PCOS too! It helps your body use insulin better.

Why might it help you?
- Makes your body more sensitive to insulin (so it works better)
- Can help with weight management
- Might make your periods more regular
- Can lower androgen (boy hormone) levels
- May reduce your risk of type 2 diabetes

The real talk:
- It might upset your tummy at first (start low, go slow!)
- Take it with food to help with side effects
- Extended-release version is usually gentler on your stomach
- It's not a magic weight loss pill, but it can help alongside healthy habits

Typical dose: Usually starts at 500mg and works up to 1500-2000mg daily
            """,
            "side_effects": ["Nausea", "Diarrhea", "Stomach upset", "Metallic taste", "B12 deficiency (long-term)"]
        },
        "birth_control": {
            "friendly_explanation": """
BIRTH CONTROL PILLS - The Hormone Balancers 💜

What are they?
Combined birth control pills have estrogen and progestin. They're often the first thing doctors suggest for PCOS symptoms.

Why might they help you?
- Regulate your periods (finally, some predictability!)
- Lower androgen levels
- Clear up acne
- Reduce unwanted hair growth
- Protect your uterine lining
- Obviously, prevent pregnancy if that's needed

The real talk:
- There are TONS of different pills - if one doesn't work, try another!
- Some pills are better for PCOS than others
- They don't fix the underlying issue, but they manage symptoms well
- You can't take them if you're trying to get pregnant
- Some people feel great on them, others not so much - it's personal

Good options for PCOS often contain:
- Drospirenone (like Yaz or Yasmin)
- Norgestimate
- Desogestrel
            """,
            "considerations": ["Blood clot risk (especially if you smoke)", "Not for those trying to conceive", "May affect mood in some people"]
        },
        "spironolactone": {
            "friendly_explanation": """
SPIRONOLACTONE (Spiro) - The Anti-Androgen 🌟

What is it?
Spironolactone is actually a blood pressure medication, but it blocks androgens really well!

Why might it help you?
- Reduces facial and body hair growth
- Helps with acne
- Can help with hair loss on your head
- Blocks those excess "boy hormones"

The real talk:
- Takes 3-6 months to see results (patience, friend!)
- You MUST use birth control with it (it can affect a male baby)
- Makes you pee more (it's a diuretic)
- Can make your periods irregular
- Often prescribed with birth control pills for best results
- Check your potassium levels - avoid potassium supplements and too many bananas!

Typical dose: Usually 50-200mg daily
            """,
            "important_note": "Must be used with contraception due to potential effects on male fetus"
        },
        "other_medications": {
            "letrozole": "Used to help with ovulation if you're trying to get pregnant. Often works better than the older medication clomiphene for PCOS.",
            "clomiphene": "Another fertility medication that helps you ovulate. Been around longer than letrozole.",
            "ozempic_wegovy": "GLP-1 medications - newer options that can help with weight and insulin resistance. Ask your doctor about these!",
            "eflornithine": "A cream for facial hair - slows down hair growth where you apply it."
        }
    },

    "alternative_treatments": {
        "overview": """
Not everyone wants to take prescription meds, and that's totally okay! There are some natural approaches that research actually supports. BUT (and this is a big but) - always talk to your doctor before starting supplements, especially if you're on other medications!
        """,
        "inositol": {
            "friendly_explanation": """
INOSITOL - The Star Supplement ⭐

What is it?
Inositol is a type of sugar that your body makes naturally. It comes in two main forms:
- Myo-inositol (the more common one)
- D-chiro-inositol

Why the hype?
Research actually shows this stuff works! It can:
- Improve how your body uses insulin
- Help with ovulation
- Balance hormones
- Potentially help with egg quality if you're trying to conceive
- May help with weight management
- Could reduce anxiety (bonus!)

How to take it:
- Myo-inositol: Usually 2-4 grams per day
- Or a combo of Myo + D-chiro in a 40:1 ratio
- Usually taken as a powder mixed in water
- Best split into 2 doses (morning and evening)

Real talk:
- It's generally safe with few side effects
- Takes about 3 months to see results
- Look for quality brands (Ovasitol is popular)
- Way cheaper than prescription meds
- Actually has decent research behind it!
            """,
            "dosage": "2-4 grams daily of myo-inositol, often combined with D-chiro-inositol"
        },
        "supplements": {
            "vitamin_d": """
VITAMIN D - The Sunshine Vitamin ☀️

Many people with PCOS are low in vitamin D! Getting your levels up might help with:
- Insulin sensitivity
- Mood
- Period regularity
- Inflammation

Get tested first, then supplement if you're low. Most people need 1000-4000 IU daily.
            """,
            "omega_3": """
OMEGA-3 FATTY ACIDS - The Inflammation Fighters 🐟

Found in fish oil, these can help with:
- Reducing inflammation
- Improving cholesterol levels
- Possibly helping with mood

Aim for 1-3 grams of EPA/DHA daily from fish oil or algae supplements if you're vegetarian.
            """,
            "nac": """
NAC (N-Acetylcysteine) - The Antioxidant 🛡️

This is an antioxidant that research shows might:
- Improve insulin sensitivity
- Help with ovulation
- Work well with fertility medications
- Support liver health

Typical dose: 600-1800mg daily
            """,
            "berberine": """
BERBERINE - Nature's Metformin 🌿

This herbal compound works similarly to metformin:
- Improves insulin sensitivity
- May help with weight management
- Can lower blood sugar

Heads up: It's strong! Don't take it with metformin without doctor approval.
Typical dose: 500mg, 2-3 times daily with meals
            """,
            "zinc": "May help with hair loss and acne. 30mg daily is typical.",
            "chromium": "Could help with blood sugar control. 200-1000mcg daily.",
            "spearmint_tea": "2 cups daily may help reduce androgen levels and facial hair. Plus it tastes good!"
        },
        "lifestyle": {
            "diet": """
EATING FOR PCOS 🥗

Okay, so diet is HUGE for PCOS. Here's what actually helps:

Focus on LOW-GLYCEMIC foods:
- These don't spike your blood sugar as much
- Think: whole grains, vegetables, legumes, most fruits

Eat enough PROTEIN:
- Helps you feel full
- Keeps blood sugar stable
- Aim for protein at every meal

Healthy FATS are your friend:
- Avocados, olive oil, nuts, fatty fish
- Help with hormone production
- Keep you satisfied

What to limit:
- Sugary drinks (this is a big one!)
- White bread, pasta, rice
- Processed snacks
- Too much dairy (for some people)

Popular approaches that work for many:
- Mediterranean diet
- Low-carb (not necessarily keto)
- Anti-inflammatory diet
- Avoiding gluten/dairy (helps some, not all)

The key: Find what works for YOUR body. We're all different!
            """,
            "exercise": """
MOVEMENT & EXERCISE 🏃‍♀️

Exercise is like medicine for PCOS - seriously! Here's the deal:

What works best:
- Mix of cardio AND strength training
- Strength training is especially good (builds muscle, improves insulin sensitivity)
- HIIT (High Intensity Interval Training) can be great
- But honestly? Any movement you'll actually DO is the best exercise

How much:
- Aim for 150 minutes per week (that's like 30 min, 5 days)
- Even 10-minute walks help!
- Strength training 2-3 times per week

Why it helps:
- Improves insulin sensitivity (huge for PCOS!)
- Helps with weight management
- Reduces inflammation
- Improves mood and energy
- Can help regulate periods

Real talk:
- Start where you are
- Don't overdo it (too much exercise can stress your body)
- Rest days are important
- Find something you enjoy!
            """,
            "stress_management": """
STRESS & SLEEP 😴

These might seem unrelated to PCOS, but they're actually super important!

STRESS raises cortisol, which can:
- Worsen insulin resistance
- Mess with your hormones
- Make symptoms worse
- Cause weight gain, especially belly fat

Stress busters that help:
- Deep breathing
- Meditation (try apps like Calm or Headspace)
- Yoga
- Time in nature
- Journaling
- Setting boundaries
- Therapy if you need it!

SLEEP is when your body repairs itself:
- Aim for 7-9 hours
- Keep a consistent sleep schedule
- Watch for sleep apnea (common with PCOS)
- Poor sleep = worse insulin resistance

These "soft" things matter just as much as diet and exercise!
            """
        }
    },

    "mental_health": {
        "overview": """
Let's get real for a second - PCOS isn't just physical. It affects your mental health too, and that's completely valid and normal to experience.

Many people with PCOS deal with:
- Anxiety (more common than in the general population)
- Depression
- Body image struggles
- Frustration with symptoms
- Grief around fertility concerns
- Feeling misunderstood

This is NOT your fault. PCOS itself affects brain chemistry and hormones that influence mood. Plus, dealing with the symptoms is genuinely hard!

What helps:
- Talking about it (therapy, support groups, friends)
- The PCOS subreddit community is super supportive
- Treating the physical symptoms often helps mood too
- Exercise is proven to help with PCOS-related depression
- Sometimes medication for anxiety/depression is needed - and that's okay!
- Self-compassion (be nice to yourself, friend)

You're dealing with something real and challenging. It's okay to ask for help.
        """
    },

    "fertility": {
        "overview": """
Okay, let's talk about the elephant in the room - fertility and PCOS.

THE GOOD NEWS FIRST:
Many people with PCOS get pregnant - with or without help! PCOS doesn't mean you can't have kids. It might just mean it takes a bit more planning.

WHY PCOS AFFECTS FERTILITY:
- Irregular ovulation = unpredictable egg release
- Sometimes you don't ovulate at all
- Higher androgens can affect egg quality
- Insulin resistance plays a role too

WHAT HELPS:
1. Lifestyle changes (yes, they really work!)
   - Losing 5-10% of body weight can restore ovulation
   - Low-glycemic diet
   - Exercise

2. Medications for ovulation:
   - Letrozole (often first choice now)
   - Clomiphene (Clomid)
   - Metformin can help too

3. If those don't work:
   - Injectable hormones
   - IUI (intrauterine insemination)
   - IVF (in vitro fertilization)

4. Supplements that may help:
   - Inositol
   - CoQ10
   - Vitamin D

IMPORTANT:
- Work with a reproductive endocrinologist if you're struggling
- Track your cycles (OPKs, basal body temperature, apps)
- Be patient but advocate for yourself
- Many people with PCOS need help - and that's normal!
        """
    },

    "long_term_health": {
        "overview": """
PCOS is a lifelong condition, so let's talk about taking care of future you!

THINGS TO WATCH:
- Type 2 diabetes (get tested regularly)
- Heart disease risk
- High blood pressure
- High cholesterol
- Sleep apnea
- Endometrial cancer (if you don't have regular periods)
- Fatty liver disease
- Mental health

SOUNDS SCARY BUT:
- These are RISKS, not guarantees
- You can absolutely reduce these risks
- Lifestyle changes make a HUGE difference
- Regular check-ups catch things early
- Many people with PCOS live long, healthy lives!

WHAT TO DO:
- Regular check-ups (at least yearly)
- Monitor blood sugar (A1C test yearly)
- Check cholesterol and blood pressure
- Have at least 4 periods per year (to protect your uterus)
- Stay active
- Don't smoke
- Limit alcohol
- Maintain a healthy weight (or work toward it)

You've got this! Taking care of PCOS now is an investment in your future health.
        """
    },

    "community_wisdom": {
        "reddit_tips": """
FROM THE PCOS COMMUNITY (r/PCOS) 💬

Here's what people who've been dealing with PCOS for years say actually helps:

ON DOCTORS:
- "Find a doctor who actually listens. If they dismiss you, find another."
- "Endocrinologists often get PCOS better than regular OBGYNs."
- "Write down your questions before appointments!"

ON DIET:
- "I stopped focusing on calories and focused on blood sugar. Game changer."
- "Going dairy-free helped my acne SO much."
- "Meal prepping is the only way I stay consistent."
- "Don't do keto if it stresses you out - stress makes PCOS worse!"

ON EXERCISE:
- "Strength training did more for me than endless cardio."
- "Walking is underrated. I do 10K steps and it helps so much."
- "Yoga helped my stress AND my symptoms."

ON SUPPLEMENTS:
- "Inositol changed my life. Wish I'd started it sooner."
- "Take Ovasitol or any good myo-inositol. It's worth it."
- "Spearmint tea is surprisingly effective for facial hair."

ON MENTAL HEALTH:
- "Be patient with yourself. This is a marathon, not a sprint."
- "Comparing yourself to others with PCOS doesn't help - we're all different."
- "Finding a community of people who get it made such a difference."
- "Therapy helped me accept my body and stop fighting it."

ON DAILY LIFE:
- "Apple cider vinegar before carby meals actually helps my blood sugar."
- "Track your symptoms - you'll notice patterns."
- "Good sleep is non-negotiable for me now."
        """
    },

    "quick_tips": {
        "getting_started": [
            "Get your diagnosis confirmed with blood tests AND ultrasound",
            "Start tracking your cycles and symptoms (apps like Clue work great)",
            "Focus on one change at a time - don't overhaul everything at once",
            "Find a supportive doctor who takes PCOS seriously",
            "Join a community (r/PCOS on Reddit is amazing)",
            "Consider starting inositol - it's safe and many find it helpful",
            "Reduce added sugars and processed foods",
            "Add movement you enjoy - even walking counts!",
            "Get your vitamin D levels checked",
            "Be patient - most changes take 3-6 months to show results"
        ]
    }
}

# Conversation starters and responses
FRIENDLY_GREETINGS = [
    "Hey there, friend! 👋 I'm so glad you're here. I know a PCOS diagnosis can feel overwhelming, but you've got this - and I'm here to help you understand it all. What would you like to know about?",
    "Hi! Welcome to our chat. 💜 Think of me as your PCOS-savvy friend who's read ALL the research so you don't have to. What's on your mind today?",
    "Hey! I'm here to help you navigate all things PCOS. No question is too basic or too weird - I've heard them all! What can I help you with?"
]

TOPIC_SUGGESTIONS = """
Here are some things I can help you with:

🔬 **Understanding PCOS** - What it is and why it happens
📋 **Diagnosis** - How doctors figure out if you have it
🩺 **Symptoms** - What to look out for
💊 **Medications** - Metformin, birth control, spironolactone, and more
🌿 **Natural treatments** - Supplements and lifestyle changes
🥗 **Diet & exercise** - What actually works
🧠 **Mental health** - Because feelings matter too
👶 **Fertility** - When you're thinking about pregnancy
❤️ **Community tips** - What other people with PCOS have learned

Just ask me anything! I'm here for you.
"""

def get_greeting():
    import random
    return random.choice(FRIENDLY_GREETINGS)
