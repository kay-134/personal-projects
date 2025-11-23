/**
 * PCOS Buddy - Client-side Chatbot
 * A friendly AI chatbot that helps people understand PCOS
 */

const PCOSChatbot = (function() {
    // Knowledge Base
    const KNOWLEDGE = {
        what_is: `PCOS stands for Polycystic Ovary Syndrome. I know it sounds super complicated, but let me break it down for you like we're chatting over lunch! 🍕

Basically, PCOS is when your hormones (the chemical messengers in your body) get a little out of whack. It's one of the most common hormone conditions - about 1 in 10 women have it! So you're definitely not alone.

Here's what's happening: Your ovaries (those small organs that hold eggs) might make too much of certain hormones called androgens. Think of androgens as the "boy hormones" - everyone has them, but with PCOS, you might have a bit more than usual.

This can cause a few things:
- Your periods might be irregular or skip around
- You might get small fluid-filled sacs (they call them "cysts" but they're really just follicles) on your ovaries
- You might notice extra hair growth or acne

But here's the important thing - PCOS is super manageable! Lots of people live totally normal, happy lives with it. It just means you need to pay a bit more attention to your body and maybe make some tweaks to how you take care of yourself.`,

        diagnosis: `So, how do doctors figure out if you have PCOS? They use something called the "Rotterdam Criteria" - fancy name, I know!

To get diagnosed, you usually need to have at least 2 out of these 3 things:

**1. IRREGULAR PERIODS** 📅
- Your periods are super unpredictable
- They come more than 35 days apart (or less than 21 days)
- Or sometimes you skip them entirely

**2. HIGH ANDROGENS (those "boy hormones")** 💪
This can show up as:
- Extra hair on your face, chest, or back (called hirsutism)
- Acne that won't quit
- Hair thinning on your head
- Or it might just show up in a blood test

**3. POLYCYSTIC OVARIES** 🔬
- An ultrasound might show lots of small follicles on your ovaries
- Or you might have high AMH levels (a hormone test)
- Fun fact: You can have PCOS without having "polycystic ovaries" - confusing, right?

The doctor will also want to rule out other conditions that can look similar, like thyroid problems or other hormone issues.`,

        symptoms: `Okay, let's talk about what PCOS can actually feel like. Everyone's experience is different - you might have some of these, all of these, or just a few!

**PERIOD STUFF** 🩸
- Irregular periods (they come whenever they want, basically)
- Heavy periods when they do show up
- Sometimes no periods for months
- Painful cramps

**SKIN & HAIR CHANGES** 💇‍♀️
- Acne (especially along your jawline and chin)
- Extra hair growth on face, chest, belly, or back
- Hair thinning or loss on your head (usually at the crown)
- Skin tags (little skin bumps)
- Dark, velvety patches of skin (usually in skin folds)

**WEIGHT & ENERGY** 💪
- Weight gain, especially around your belly
- Difficulty losing weight even when you try hard
- Feeling tired a lot
- Cravings, especially for carbs and sweets

**MOOD STUFF** 🧠
- Anxiety or feeling worried a lot
- Depression or feeling down
- Mood swings
- Brain fog (trouble concentrating)

**OTHER THINGS** 🌙
- Trouble sleeping or sleep apnea
- Headaches
- Pelvic pain

Remember: Having PCOS doesn't mean you'll have ALL of these symptoms. And many of these can be managed with the right approach!`,

        medications: `Let me walk you through the main medications doctors might suggest for PCOS. Think of these as tools in your toolbox - your doctor will help you pick the right ones for YOUR situation!

**1. METFORMIN** 💊
- Actually a diabetes medication, but works great for PCOS
- Helps your body use insulin better
- Can help with weight and make periods more regular
- Might upset your tummy at first (start low, go slow!)

**2. BIRTH CONTROL PILLS** 💜
- Often the first thing doctors suggest
- Regulates your periods (finally, predictability!)
- Lowers androgen levels
- Clears up acne and reduces unwanted hair growth
- There are TONS of different pills - if one doesn't work, try another!

**3. SPIRONOLACTONE (Spiro)** 🌟
- Blocks androgens really well
- Reduces facial and body hair growth
- Helps with acne and hair loss on your head
- Takes 3-6 months to see results (patience!)
- MUST use birth control with it

**OTHER OPTIONS:**
- **Letrozole/Clomid** - For fertility help
- **Ozempic/Wegovy** - Newer options for weight and insulin
- **Eflornithine cream** - For facial hair

Which one would you like to know more about?`,

        metformin: `**METFORMIN - The Insulin Helper** 💊

**What is it?**
Metformin is actually a diabetes medication, but it works really well for PCOS too! It helps your body use insulin better.

**Why might it help you?**
- Makes your body more sensitive to insulin (so it works better)
- Can help with weight management
- Might make your periods more regular
- Can lower androgen (boy hormone) levels
- May reduce your risk of type 2 diabetes

**The real talk:**
- It might upset your tummy at first (start low, go slow!)
- Take it with food to help with side effects
- Extended-release version is usually gentler on your stomach
- It's not a magic weight loss pill, but it can help alongside healthy habits

**Typical dose:** Usually starts at 500mg and works up to 1500-2000mg daily

**Side effects to know about:**
- Nausea and stomach upset (usually gets better)
- Diarrhea
- Metallic taste in your mouth
- Can cause B12 deficiency long-term (ask about supplements!)`,

        birth_control: `**BIRTH CONTROL PILLS - The Hormone Balancers** 💜

**What are they?**
Combined birth control pills have estrogen and progestin. They're often the first thing doctors suggest for PCOS symptoms.

**Why might they help you?**
- Regulate your periods (finally, some predictability!)
- Lower androgen levels
- Clear up acne
- Reduce unwanted hair growth
- Protect your uterine lining
- Obviously, prevent pregnancy if that's needed

**The real talk:**
- There are TONS of different pills - if one doesn't work, try another!
- Some pills are better for PCOS than others
- They don't fix the underlying issue, but they manage symptoms well
- You can't take them if you're trying to get pregnant
- Some people feel great on them, others not so much - it's personal

**Good options for PCOS often contain:**
- Drospirenone (like Yaz or Yasmin)
- Norgestimate
- Desogestrel

**Things to consider:**
- Blood clot risk (especially if you smoke)
- May affect mood in some people
- Not for those trying to conceive right now`,

        spironolactone: `**SPIRONOLACTONE (Spiro) - The Anti-Androgen** 🌟

**What is it?**
Spironolactone is actually a blood pressure medication, but it blocks androgens really well!

**Why might it help you?**
- Reduces facial and body hair growth
- Helps with acne
- Can help with hair loss on your head
- Blocks those excess "boy hormones"

**The real talk:**
- Takes 3-6 months to see results (patience, friend!)
- You MUST use birth control with it (it can affect a male baby)
- Makes you pee more (it's a diuretic)
- Can make your periods irregular
- Often prescribed with birth control pills for best results
- Check your potassium levels - avoid potassium supplements and too many bananas!

**Typical dose:** Usually 50-200mg daily

**Important:** Must be used with contraception due to potential effects on male fetus if you get pregnant.`,

        natural: `Not everyone wants to take prescription meds, and that's totally okay! There are some natural approaches that research actually supports. BUT - always talk to your doctor before starting supplements!

**INOSITOL** ⭐ (The Star Supplement!)
- A type of sugar your body makes naturally
- Research shows it actually works!
- Improves insulin sensitivity
- Helps with ovulation
- Usually 2-4 grams of myo-inositol daily
- Look for Ovasitol or similar quality brands

**VITAMIN D** ☀️
- Many with PCOS are low in vitamin D
- Helps with insulin sensitivity and mood
- Get tested first, then supplement if needed
- Usually 1000-4000 IU daily

**OMEGA-3s** 🐟
- Found in fish oil
- Reduces inflammation
- Improves cholesterol
- 1-3 grams EPA/DHA daily

**NAC (N-Acetylcysteine)** 🛡️
- Antioxidant that may help with ovulation
- 600-1800mg daily

**BERBERINE** 🌿
- Works similarly to metformin
- Don't take WITH metformin without doctor approval!
- 500mg 2-3x daily with meals

**SPEARMINT TEA** 🍵
- 2 cups daily may help reduce facial hair
- Plus it tastes good!

Would you like more details on any of these?`,

        inositol: `**INOSITOL - The Star Supplement** ⭐

**What is it?**
Inositol is a type of sugar that your body makes naturally. It comes in two main forms:
- Myo-inositol (the more common one)
- D-chiro-inositol

**Why the hype?**
Research actually shows this stuff works! It can:
- Improve how your body uses insulin
- Help with ovulation
- Balance hormones
- Potentially help with egg quality if you're trying to conceive
- May help with weight management
- Could reduce anxiety (bonus!)

**How to take it:**
- Myo-inositol: Usually 2-4 grams per day
- Or a combo of Myo + D-chiro in a 40:1 ratio
- Usually taken as a powder mixed in water
- Best split into 2 doses (morning and evening)

**Real talk:**
- It's generally safe with few side effects
- Takes about 3 months to see results
- Look for quality brands (Ovasitol is popular)
- Way cheaper than prescription meds
- Actually has decent research behind it!

Many people in the PCOS community swear by this one!`,

        diet: `**EATING FOR PCOS** 🥗

Okay, so diet is HUGE for PCOS. Here's what actually helps:

**Focus on LOW-GLYCEMIC foods:**
- These don't spike your blood sugar as much
- Think: whole grains, vegetables, legumes, most fruits
- Swap white bread for whole grain, white rice for brown or cauliflower rice

**Eat enough PROTEIN:**
- Helps you feel full longer
- Keeps blood sugar stable
- Aim for protein at every meal
- Examples: eggs, chicken, fish, Greek yogurt, legumes, tofu

**Healthy FATS are your friend:**
- Avocados, olive oil, nuts, fatty fish
- Help with hormone production
- Keep you satisfied longer

**What to limit:**
- Sugary drinks (this is a BIG one!)
- White bread, pasta, rice
- Processed snacks and fast food
- Too much dairy (for some people)
- Added sugars

**Popular approaches that work for many:**
- Mediterranean diet
- Low-carb (not necessarily keto)
- Anti-inflammatory diet
- Some find avoiding gluten/dairy helps

**Pro tips from the community:**
- Focus on blood sugar, not just calories
- Meal prep to stay consistent
- Don't stress about being perfect
- Apple cider vinegar before carby meals may help

The key: Find what works for YOUR body. We're all different!`,

        exercise: `**MOVEMENT & EXERCISE** 🏃‍♀️

Exercise is like medicine for PCOS - seriously! Here's the deal:

**What works best:**
- Mix of cardio AND strength training
- Strength training is especially good (builds muscle, improves insulin sensitivity)
- HIIT (High Intensity Interval Training) can be great
- But honestly? Any movement you'll actually DO is the best exercise

**How much:**
- Aim for 150 minutes per week (that's like 30 min, 5 days)
- Even 10-minute walks help!
- Strength training 2-3 times per week

**Why it helps:**
- Improves insulin sensitivity (huge for PCOS!)
- Helps with weight management
- Reduces inflammation
- Improves mood and energy
- Can help regulate periods

**Great options:**
- Walking (seriously underrated!)
- Weight lifting or resistance bands
- Swimming
- Yoga (great for stress too)
- Dancing
- Cycling

**Real talk:**
- Start where you are - don't compare yourself to others
- Don't overdo it (too much exercise can stress your body)
- Rest days are important
- Find something you actually enjoy!
- Consistency beats intensity

The community says: "Strength training changed my life" - you'll hear this a lot!`,

        fertility: `**PCOS AND FERTILITY** 👶

Okay, let's talk about the elephant in the room - fertility and PCOS.

**THE GOOD NEWS FIRST:**
Many people with PCOS get pregnant - with or without help! PCOS doesn't mean you can't have kids. It might just mean it takes a bit more planning.

**WHY PCOS AFFECTS FERTILITY:**
- Irregular ovulation = unpredictable egg release
- Sometimes you don't ovulate at all
- Higher androgens can affect egg quality
- Insulin resistance plays a role too

**WHAT HELPS:**

**1. Lifestyle changes (yes, they really work!)**
- Losing 5-10% of body weight can restore ovulation
- Low-glycemic diet
- Regular exercise

**2. Medications for ovulation:**
- Letrozole (often first choice now)
- Clomiphene (Clomid)
- Metformin can help too

**3. If those don't work:**
- Injectable hormones
- IUI (intrauterine insemination)
- IVF (in vitro fertilization)

**4. Supplements that may help:**
- Inositol
- CoQ10
- Vitamin D

**IMPORTANT:**
- Work with a reproductive endocrinologist if you're struggling
- Track your cycles (OPKs, basal body temperature, apps)
- Be patient but advocate for yourself
- Many people with PCOS need help - and that's totally normal!

You can absolutely have a family with PCOS. 💜`,

        mental_health: `**MENTAL HEALTH & PCOS** 🧠

Let's get real for a second - PCOS isn't just physical. It affects your mental health too, and that's completely valid.

**Many people with PCOS deal with:**
- Anxiety (more common than in the general population)
- Depression
- Body image struggles
- Frustration with symptoms
- Grief around fertility concerns
- Feeling misunderstood by doctors or others

**This is NOT your fault.**
PCOS itself affects brain chemistry and hormones that influence mood. Plus, dealing with the symptoms is genuinely hard!

**What helps:**

**Talk about it:**
- Therapy or counseling
- Support groups (online or in person)
- The r/PCOS subreddit is super supportive
- Friends and family who listen

**Physical things that help mood:**
- Exercise (proven to help with PCOS-related depression)
- Getting enough sleep
- Reducing stress
- Treating the physical symptoms

**Professional help:**
- Sometimes medication for anxiety/depression is needed
- And that's okay!
- A therapist who understands chronic conditions can be amazing

**Self-compassion:**
- Be nice to yourself, friend
- You're dealing with something real and challenging
- Progress isn't linear
- Celebrate small wins

You're not alone in this. 💜`,

        community: `**FROM THE PCOS COMMUNITY** 💬

Here's what people who've been dealing with PCOS for years say actually helps:

**ON DOCTORS:**
- "Find a doctor who actually listens. If they dismiss you, find another."
- "Endocrinologists often get PCOS better than regular OBGYNs."
- "Write down your questions before appointments!"

**ON DIET:**
- "I stopped focusing on calories and focused on blood sugar. Game changer."
- "Going dairy-free helped my acne SO much."
- "Meal prepping is the only way I stay consistent."
- "Don't do keto if it stresses you out - stress makes PCOS worse!"

**ON EXERCISE:**
- "Strength training did more for me than endless cardio."
- "Walking is underrated. I do 10K steps and it helps so much."
- "Yoga helped my stress AND my symptoms."

**ON SUPPLEMENTS:**
- "Inositol changed my life. Wish I'd started it sooner."
- "Take Ovasitol or any good myo-inositol. It's worth it."
- "Spearmint tea is surprisingly effective for facial hair."

**ON MENTAL HEALTH:**
- "Be patient with yourself. This is a marathon, not a sprint."
- "Comparing yourself to others with PCOS doesn't help - we're all different."
- "Finding a community of people who get it made such a difference."
- "Therapy helped me accept my body and stop fighting it."

**ON DAILY LIFE:**
- "Apple cider vinegar before carby meals actually helps my blood sugar."
- "Track your symptoms - you'll notice patterns."
- "Good sleep is non-negotiable for me now."

You've got this! 💜`,

        stress: `**STRESS & SLEEP** 😴

These might seem unrelated to PCOS, but they're actually super important!

**STRESS raises cortisol, which can:**
- Worsen insulin resistance
- Mess with your hormones
- Make symptoms worse
- Cause weight gain, especially belly fat
- Affect your menstrual cycle

**Stress busters that help:**
- Deep breathing exercises
- Meditation (try apps like Calm or Headspace)
- Yoga
- Time in nature
- Journaling
- Setting boundaries
- Therapy if you need it!
- Hobbies you enjoy

**SLEEP is when your body repairs itself:**
- Aim for 7-9 hours
- Keep a consistent sleep schedule
- Watch for sleep apnea (common with PCOS - talk to your doctor!)
- Poor sleep = worse insulin resistance
- Create a relaxing bedtime routine

**The stress-PCOS cycle:**
PCOS symptoms → stress about symptoms → stress worsens symptoms → more stress

Breaking this cycle matters! These "soft" things are just as important as diet and exercise.

**Tips:**
- You can't eliminate all stress, but you can manage your response
- Even 5 minutes of deep breathing helps
- Prioritize sleep like you would a medication
- It's okay to say no to things`,

        long_term: `**LONG-TERM HEALTH & PCOS** ❤️

PCOS is a lifelong condition, so let's talk about taking care of future you!

**THINGS TO BE AWARE OF:**
- Type 2 diabetes risk (get tested regularly)
- Heart disease risk
- High blood pressure
- High cholesterol
- Sleep apnea
- Endometrial concerns (if you don't have regular periods)
- Fatty liver disease
- Mental health

**SOUNDS SCARY BUT:**
- These are RISKS, not guarantees
- You can absolutely reduce these risks
- Lifestyle changes make a HUGE difference
- Regular check-ups catch things early
- Many people with PCOS live long, healthy lives!

**WHAT TO DO:**
- Regular check-ups (at least yearly)
- Monitor blood sugar (A1C test yearly)
- Check cholesterol and blood pressure
- Have at least 4 periods per year (to protect your uterus)
- Stay active
- Don't smoke
- Limit alcohol
- Work toward a healthy weight

**THE POSITIVE SPIN:**
Taking care of PCOS now is actually an investment in your overall health! You're being proactive about things many people ignore until they're problems.

You've got this! 💜`
    };

    const GREETINGS = [
        "Hey there, friend! 👋 I'm so glad you're here. I know a PCOS diagnosis can feel overwhelming, but you've got this - and I'm here to help you understand it all. What would you like to know about?",
        "Hi! Welcome to PCOS Buddy! 💜 Think of me as your PCOS-savvy friend who's read ALL the research so you don't have to. What's on your mind today?",
        "Hey! I'm here to help you navigate all things PCOS. No question is too basic or too weird - I've heard them all! What can I help you with?"
    ];

    const TOPICS = `
Here are some things I can help you with:

🔬 **"What is PCOS?"** - The basics explained simply
📋 **"How is PCOS diagnosed?"** - Tests and criteria
🩺 **"What are the symptoms?"** - What to look out for
💊 **"Tell me about medications"** - Metformin, birth control, spiro
🌿 **"Natural treatments"** - Inositol, supplements, herbs
🥗 **"Diet tips"** - What to eat and avoid
🏃‍♀️ **"Exercise for PCOS"** - Movement that helps
🧠 **"Mental health"** - Emotional support
👶 **"Fertility"** - Getting pregnant info
💬 **"Community tips"** - What others have learned

Just type your question or pick a topic! 💜`;

    // Pattern matching
    const PATTERNS = {
        what_is: /what is pcos|what's pcos|explain pcos|pcos mean|tell me about pcos|pcos basics|understand pcos|new to pcos|just diagnosed|recently diagnosed|polycystic ovary/i,
        diagnosis: /diagnos|how do (they|doctors|you) know|test for pcos|rotterdam|ultrasound|blood test|criteria|amh|find out if i have/i,
        symptoms: /symptom|sign|feel|experience|what happens|side effect|how does pcos affect|acne|hair growth|hirsutism|irregular period|weight gain|tired|fatigue|mood/i,
        medications: /^(medication|medicine|drug|prescription|treatment option|treat pcos|what can i take)s?$/i,
        metformin: /metformin|glucophage|insulin sensitiz/i,
        birth_control: /birth control|the pill|oral contracept|bc pill|yaz|yasmin|hormonal contracept/i,
        spironolactone: /spiro|aldactone|anti.?androgen/i,
        natural: /natural|supplement|vitamin|alternative|herbal|holistic|without medication|home remed/i,
        inositol: /inositol|myo.?inositol|d.?chiro|ovasitol/i,
        diet: /diet|eat|food|nutrition|carb|sugar|keto|low glycemic|meal|what should i eat|mediterranean|gluten|dairy/i,
        exercise: /exercise|workout|gym|cardio|weight train|strength|fitness|active|movement|walk|yoga|hiit/i,
        stress: /stress|sleep|relax|meditat|self care|self-care|cope|overwhelm|cortisol/i,
        mental_health: /mental health|depress|anxious|anxiety|sad|emotion|feel down|mood swing|therapy|counseling|support/i,
        fertility: /fertil|pregnant|baby|conceiv|ovulat|trying to conceive|ttc|ivf|iui|have kids|have children|get pregnant/i,
        long_term: /long term|long-term|future|risk|diabetes|heart|cancer|health risk|complicat/i,
        community: /reddit|community|other people|tips|advice from|what works|success stor/i,
        greeting: /^(hi|hello|hey|howdy|hiya|good morning|good afternoon|good evening)!?$/i,
        thanks: /thank|thanks|appreciate|helpful|great info/i,
        help: /^help$|what can you|how do you work|what do you know/i
    };

    function detectTopic(message) {
        const msg = message.toLowerCase().trim();

        for (const [topic, pattern] of Object.entries(PATTERNS)) {
            if (pattern.test(msg)) {
                return topic;
            }
        }
        return null;
    }

    function getResponse(message) {
        const topic = detectTopic(message);

        switch(topic) {
            case 'greeting':
                return "Hey again! 😊 What would you like to know about PCOS?" + TOPICS;
            case 'thanks':
                return "You're so welcome! 💜 That's what I'm here for.\n\nIs there anything else you'd like to know about PCOS? I'm happy to keep chatting!";
            case 'help':
                return TOPICS;
            case 'what_is':
                return KNOWLEDGE.what_is;
            case 'diagnosis':
                return KNOWLEDGE.diagnosis;
            case 'symptoms':
                return KNOWLEDGE.symptoms;
            case 'medications':
                return KNOWLEDGE.medications;
            case 'metformin':
                return KNOWLEDGE.metformin;
            case 'birth_control':
                return KNOWLEDGE.birth_control;
            case 'spironolactone':
                return KNOWLEDGE.spironolactone;
            case 'natural':
                return KNOWLEDGE.natural;
            case 'inositol':
                return KNOWLEDGE.inositol;
            case 'diet':
                return KNOWLEDGE.diet;
            case 'exercise':
                return KNOWLEDGE.exercise;
            case 'stress':
                return KNOWLEDGE.stress;
            case 'mental_health':
                return KNOWLEDGE.mental_health;
            case 'fertility':
                return KNOWLEDGE.fertility;
            case 'long_term':
                return KNOWLEDGE.long_term;
            case 'community':
                return KNOWLEDGE.community;
            default:
                return `Hmm, I want to make sure I give you the best info! Could you tell me a bit more about what you'd like to know?\n${TOPICS}`;
        }
    }

    function getGreeting() {
        const index = Math.floor(Math.random() * GREETINGS.length);
        return GREETINGS[index] + "\n" + TOPICS;
    }

    // Public API
    return {
        getResponse,
        getGreeting
    };
})();
