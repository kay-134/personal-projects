"""
PCOS Buddy Chatbot
A friendly AI chatbot that helps people understand PCOS in simple, approachable terms.
"""

import re
from pcos_knowledge_base import PCOS_KNOWLEDGE, get_greeting, TOPIC_SUGGESTIONS

class PCOSChatbot:
    def __init__(self):
        self.conversation_history = []
        self.user_name = None
        self.greeted = False

    def get_initial_greeting(self):
        """Return the first greeting when chat starts."""
        self.greeted = True
        return get_greeting() + "\n\n" + TOPIC_SUGGESTIONS

    def detect_topic(self, message):
        """Detect what topic the user is asking about."""
        message_lower = message.lower()

        # Topic detection patterns
        patterns = {
            "what_is": [
                r"what is pcos", r"what's pcos", r"explain pcos", r"pcos mean",
                r"what does pcos", r"tell me about pcos", r"pcos basics",
                r"understand pcos", r"new to pcos", r"just diagnosed",
                r"recently diagnosed", r"what is polycystic"
            ],
            "diagnosis": [
                r"diagnos", r"how do (they|doctors|you) know", r"test",
                r"rotterdam", r"ultrasound", r"blood test", r"how is pcos",
                r"find out if", r"do i have", r"criteria", r"amh"
            ],
            "symptoms": [
                r"symptom", r"sign", r"feel", r"experience", r"what happens",
                r"side effect", r"what are the", r"how does pcos affect",
                r"acne", r"hair", r"period", r"irregular", r"weight",
                r"tired", r"fatigue", r"mood", r"depression", r"anxiety",
                r"pain", r"cramp"
            ],
            "metformin": [
                r"metformin", r"glucophage", r"insulin sensitiz"
            ],
            "birth_control": [
                r"birth control", r"pill", r"oral contracept", r"bc pill",
                r"yaz", r"yasmin", r"the pill", r"hormonal contracept"
            ],
            "spironolactone": [
                r"spiro", r"aldactone", r"anti.?androgen", r"antiandrogen"
            ],
            "medications": [
                r"medicin", r"medicat", r"drug", r"prescription", r"pharma",
                r"what (can|should) i take", r"treatment option", r"treat pcos"
            ],
            "inositol": [
                r"inositol", r"myo.?inositol", r"d.?chiro", r"ovasitol"
            ],
            "supplements": [
                r"supplement", r"vitamin", r"natural", r"alternative",
                r"herbal", r"holistic", r"without medication", r"nac",
                r"berberine", r"omega", r"zinc", r"spearmint"
            ],
            "diet": [
                r"diet", r"eat", r"food", r"nutrition", r"carb", r"sugar",
                r"keto", r"low glycemic", r"meal", r"what should i eat",
                r"mediterranean", r"gluten", r"dairy"
            ],
            "exercise": [
                r"exercise", r"workout", r"gym", r"cardio", r"weight train",
                r"strength", r"fitness", r"active", r"movement", r"walk",
                r"yoga", r"hiit"
            ],
            "stress": [
                r"stress", r"sleep", r"relax", r"meditat", r"anxiety",
                r"mental", r"self care", r"self-care", r"cope", r"overwhelm"
            ],
            "mental_health": [
                r"mental health", r"depress", r"anxious", r"anxiety",
                r"sad", r"emotion", r"feel down", r"mood swing", r"therapy",
                r"counseling", r"support group"
            ],
            "fertility": [
                r"fertil", r"pregnant", r"pregnanc", r"baby", r"conceiv",
                r"ovulat", r"trying to conceive", r"ttc", r"ivf", r"iui",
                r"have kids", r"have children", r"get pregnant"
            ],
            "long_term": [
                r"long term", r"long-term", r"future", r"risk", r"diabetes",
                r"heart", r"cancer", r"health risk", r"complicat"
            ],
            "community": [
                r"reddit", r"community", r"other people", r"tips",
                r"advice from", r"what works", r"success stor"
            ],
            "greeting": [
                r"^hi$", r"^hello$", r"^hey$", r"^hi there", r"^hello there",
                r"^good (morning|afternoon|evening)", r"^howdy", r"^hiya"
            ],
            "thanks": [
                r"thank", r"thanks", r"appreciate", r"helpful", r"great info"
            ],
            "help": [
                r"^help$", r"what can you", r"how do you work", r"what do you know"
            ]
        }

        for topic, topic_patterns in patterns.items():
            for pattern in topic_patterns:
                if re.search(pattern, message_lower):
                    return topic

        return None

    def generate_response(self, message):
        """Generate a friendly response based on the user's message."""
        topic = self.detect_topic(message)

        # Store conversation
        self.conversation_history.append({"role": "user", "message": message})

        response = self._get_topic_response(topic, message)

        self.conversation_history.append({"role": "assistant", "message": response})

        return response

    def _get_topic_response(self, topic, message):
        """Get response for a specific topic."""

        if topic == "greeting":
            if not self.greeted:
                return self.get_initial_greeting()
            return "Hey again! 😊 What else can I help you learn about PCOS?"

        if topic == "thanks":
            return """
You're so welcome! 💜 That's what I'm here for.

Is there anything else you'd like to know about PCOS? I'm happy to keep chatting!
            """.strip()

        if topic == "help":
            return TOPIC_SUGGESTIONS

        if topic == "what_is":
            return PCOS_KNOWLEDGE["what_is_pcos"]["simple_explanation"].strip()

        if topic == "diagnosis":
            return PCOS_KNOWLEDGE["diagnosis"]["criteria"].strip()

        if topic == "symptoms":
            return PCOS_KNOWLEDGE["symptoms"]["common"].strip()

        if topic == "metformin":
            return PCOS_KNOWLEDGE["medications"]["metformin"]["friendly_explanation"].strip()

        if topic == "birth_control":
            return PCOS_KNOWLEDGE["medications"]["birth_control"]["friendly_explanation"].strip()

        if topic == "spironolactone":
            return PCOS_KNOWLEDGE["medications"]["spironolactone"]["friendly_explanation"].strip()

        if topic == "medications":
            overview = PCOS_KNOWLEDGE["medications"]["overview"].strip()
            return f"""
{overview}

The main medications for PCOS are:

**1. Metformin** - Helps with insulin sensitivity
**2. Birth Control Pills** - Regulates hormones and periods
**3. Spironolactone** - Reduces androgen effects (hair, acne)

Which one would you like to learn more about? Just ask!

I can also tell you about other options like:
- Letrozole or Clomid (for fertility)
- GLP-1 medications like Ozempic (for weight/insulin)
- Eflornithine cream (for facial hair)
            """.strip()

        if topic == "inositol":
            return PCOS_KNOWLEDGE["alternative_treatments"]["inositol"]["friendly_explanation"].strip()

        if topic == "supplements":
            overview = PCOS_KNOWLEDGE["alternative_treatments"]["overview"].strip()
            supps = PCOS_KNOWLEDGE["alternative_treatments"]["supplements"]
            return f"""
{overview}

Here are the most researched supplements for PCOS:

**INOSITOL** ⭐ (The most evidence behind it!)
{supps["vitamin_d"]}

{supps["omega_3"]}

{supps["nac"]}

{supps["berberine"]}

**Quick mentions:**
- **Zinc** - {supps["zinc"]}
- **Chromium** - {supps["chromium"]}
- **Spearmint Tea** - {supps["spearmint_tea"]}

Would you like more details on any of these? Inositol is usually the #1 recommendation!
            """.strip()

        if topic == "diet":
            return PCOS_KNOWLEDGE["alternative_treatments"]["lifestyle"]["diet"].strip()

        if topic == "exercise":
            return PCOS_KNOWLEDGE["alternative_treatments"]["lifestyle"]["exercise"].strip()

        if topic == "stress":
            return PCOS_KNOWLEDGE["alternative_treatments"]["lifestyle"]["stress_management"].strip()

        if topic == "mental_health":
            return PCOS_KNOWLEDGE["mental_health"]["overview"].strip()

        if topic == "fertility":
            return PCOS_KNOWLEDGE["fertility"]["overview"].strip()

        if topic == "long_term":
            return PCOS_KNOWLEDGE["long_term_health"]["overview"].strip()

        if topic == "community":
            return PCOS_KNOWLEDGE["community_wisdom"]["reddit_tips"].strip()

        # Default response for unrecognized topics
        return self._get_default_response(message)

    def _get_default_response(self, message):
        """Handle messages that don't match specific topics."""
        return f"""
Hmm, I want to make sure I give you the best info! Could you tell me a bit more about what you'd like to know?

Here are some things I can help with:

🔬 **"What is PCOS?"** - The basics explained simply
📋 **"How is PCOS diagnosed?"** - Tests and criteria
🩺 **"What are PCOS symptoms?"** - What to look out for
💊 **"Tell me about medications"** - Metformin, birth control, spiro
🌿 **"Natural treatments"** - Inositol, supplements, herbs
🥗 **"What should I eat?"** - Diet tips that work
🏃‍♀️ **"Exercise for PCOS"** - Movement that helps
🧠 **"Mental health and PCOS"** - Emotional support
👶 **"PCOS and fertility"** - Getting pregnant info
💬 **"Community tips"** - What others have learned

Just type your question or pick a topic! No wrong questions here. 💜
        """.strip()

    def get_quick_tips(self):
        """Return quick tips for someone just starting out."""
        tips = PCOS_KNOWLEDGE["quick_tips"]["getting_started"]
        tips_formatted = "\n".join([f"✅ {tip}" for tip in tips])
        return f"""
Here are my top 10 tips for someone just diagnosed with PCOS:

{tips_formatted}

Remember: You don't have to do everything at once! Pick one or two things to focus on first. Which of these would you like to know more about?
        """.strip()


# Create a singleton instance
chatbot = PCOSChatbot()

def get_response(message):
    """Main function to get a chatbot response."""
    return chatbot.generate_response(message)

def start_chat():
    """Get the initial greeting."""
    return chatbot.get_initial_greeting()


if __name__ == "__main__":
    # Simple CLI for testing
    print("=" * 60)
    print("PCOS Buddy - Your Friendly PCOS Information Chatbot")
    print("=" * 60)
    print()
    print(start_chat())
    print()

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nPCOS Buddy: Take care of yourself, friend! You've got this. 💜 Bye!\n")
            break
        if user_input:
            response = get_response(user_input)
            print(f"\nPCOS Buddy: {response}")
