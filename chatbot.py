import json
import difflib
import os

DATA_FILE = "chatbot_memory.json"

# ------------------------------------
# Load / Create memory
# ------------------------------------
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}  # empty learning memory


# ------------------------------------
# Get best matching question
# ------------------------------------
def get_best_match(user_text, memory_keys):
    matches = difflib.get_close_matches(user_text.lower(), memory_keys, n=1, cutoff=0.6)
    return matches[0] if matches else None


# ------------------------------------
# Main Chat Loop
# ------------------------------------
print("🤖 IntentIQ Self-Learning Chatbot")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    # try to find a similar stored question
    best_match = get_best_match(user_input, memory.keys())

    if best_match:
        print("Chatbot:", memory[best_match])
    else:
        print("Chatbot: I don't know this yet. Please teach me!")
        new_answer = input("Enter correct response: ").strip()

        # Save this new learning
        memory[user_input] = new_answer

        with open(DATA_FILE, "w") as f:
            json.dump(memory, f, indent=4)

        print("Chatbot: Got it! I learned this response. ✅\n")
