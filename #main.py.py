#mood_bot.py
import datetime 
import random
import os #For file path handling and activity suggestions

#--- Configuration ---
ACTIVITIES_FILE = "activities.txt"
MOOD_LOG_FILE = "mood_log.txt"

# --- Helper Functions ---
def log_mood(mood, user_note=""):
    """Logs the user's mood and an optional note to a file."""
    filepath = os.path.join(os.path.dirname(__file__), MOOD_LOG_FILE)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filepath, "a", encoding="utf-8") as f: # "a" for append mode
            f.write(f"[{timestamp}] Mood: {mood.capitalize()} | Note: {user_note}\n")
    except Exception as e:
        print(f"Bot: Couldn't log your mood: {e}")

def get_random_activity():
    """Reads activities from a file and returns a random one."""
    filepath = os.path.join(os.path.dirname(__file__), ACTIVITIES_FILE)
    activities = [] # Corrected variable name from 'activites' to 'activities'

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    activities.append(stripped_line) # THIS LINE WAS MISSING
    except FileNotFoundError:
        return "Sorry, I can't find the activities list. Make sure 'activities.txt' exists!"
    except Exception as e:
        return f"An error occurred while getting activities: {e}"

    if not activities: # Check if the list is empty after reading
        return "My activities list is empty! Add some ideas to activities.txt."
    
    return random.choice(activities) # THIS LINE WAS MISSINGbad
def tell_a_joke():
    """Returns a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why did the tomato turn red? Because it saw the salad dressing!"
    ]
    return random.choice(jokes)

#---Main Bot Logic---
  
print("Hello! I'm MinimoodBot 🤖")
print("How are you feeling today?")

user_input= input("You:").lower()
#Expaned Mood response

#happy/positve Mood
if"happy" in user_input or "great" in user_input or "good" in user_input or "fantastic" in user_input:
    current_mood ="happy"
    print("Bot: That's absolutely wonderful to hear! Keep that positive energy going! 😄")
    user_note= input("Bot: What made you feel so good today? (just a few words): ")
    log_mood(current_mood, user_note)

#sad/upset Moods
elif "sad"in user_input or "unhappy" in user_input or "dowm" in user_input or "gloomy" in user_input:
    current_mood = "sad"
    print("Bot: I'm really soory to hear you're feeling this way. Remember, it's okay not to be okay. I'm here for you 💙💙")
    user_note= input("Bot: Do you want to share a bit about why you're feeling sad, or prefer to just acknowlegde it? (Type 'yes' to share, or 'no'): "). lower()
    if user_note== "yes":
        detail= input("You: ")
        log_mood(current_mood, detail)
    else:
        log_mood(current_mood, "chose not to share details")
        #offer a distraction 
        distract_choice = input("Bot: Would you like to hear a joke to lighten the mood? (yes/no: ").lower()
        if distract_choice =="yes":
            print(f"Bot: Here's one: {tell_a_joke()}")

#Angry/ fraustrated moods
elif" angry" in user_input or "mad" in user_input or "frustrated" in user_input or "annoyed" in user_input:
    current_mood= "angry"
    print("Bot: what specifically is making you feel angry rigt now?(just a few words): ")
    log_mood(current_mood,user_note) # type: ignore
    print("Bot: Remeber to take a break if you need to.")
 
#Tired/Exhausted moods
elif "tired" in user_input or "sleepy" in user_input or "exhausted" in user_input or "drained" in user_input:
    current_mood = "tired"
    print("Bot: oh dear, it sounds like you're running on empty. You should definitely prioritize some rest💤💤💤 ")
    user_note = input("Bot: Have you been overworking or not sleeping well?(just a few words): ")
    log_mood(current_mood, user_note)
    #offer a distraction (joke)
    distract_choice = input ("Bot: How about a quick joke to perk you up a little(yes/no): ").lower()
    if distract_choice == "yes":
        print(f"Bot: Here's one:{tell_a_joke()}")

# Confused/Unsure Moods
elif "confused" in user_input or "unsure" in user_input or "puzzled" in user_input or "lost" in user_input:
    current_mood = "confused"
    print("Bot: It seems like you're feeling a bit muddled. Sometimes taking a step back helps clear things up 🤔")
    user_note = input("Bot: What specifically is confusing you? (Just a few words): ")
    log_mood(current_mood, user_note)

# Bored Moods
elif "bored" in user_input or "boring" in user_input:
    current_mood = "bored"
    print("Bot: Feeling a bit of ennui? Sometimes a new activity can help. ✨")
    user_note = input("Bot: What usually helps you when you're bored? (Just a few words): ")
    log_mood(current_mood, user_note)
    # Suggest an activity
    activity_choice = input("Bot: Would you like an activity suggestion? (yes/no): ").lower()
    if activity_choice == "yes":
        print(f"Bot: How about this: {get_random_activity()}")
    # Also offer a joke
    joke_choice = input("Bot: Or perhaps a joke to chase the boredom away? (yes/no): ").lower()
    if joke_choice == "yes":
        print(f"Bot: Here's one: {tell_a_joke()}")


# Neutral/Okay Moods
elif "okay" in user_input or "alright" in user_input or "fine" in user_input or "neutral" in user_input:
    current_mood = "okay"
    print("Bot: Thanks for sharing! 'Okay' is a perfectly valid feeling. Sometimes just being is enough. 👍")
    user_note = input("Bot: Anything specific on your mind, or just a calm day? (Just a few words): ")
    log_mood(current_mood, user_note)

# Default/Fallback Response
else:
    current_mood = "unrecognized"
    print("Bot: I'm not quite sure how you're feeling based on that, but I want you to know I'm here to chat whenever you need! 😊")
    user_note = input("Bot: Can you describe your feeling in other words? (Just a few words): ")
    log_mood(current_mood, user_note)

print("\nBot: Talk to you again soon! Have a good rest of your day. 👋")
