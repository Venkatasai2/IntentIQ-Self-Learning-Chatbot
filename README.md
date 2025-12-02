🧠 IntentIQ – Self-Learning Chatbot

A lightweight, console-based Python chatbot that learns automatically from user inputs.
Whenever the chatbot encounters a new question, it asks the user for the correct response, saves it permanently, and uses it the next time — achieving a self-updating, expanding knowledge base.

🚀 Features
✅ Self-Learning Memory

Learns new responses dynamically at runtime

Stores all learned responses in a JSON file

Automatically answers stored questions in future conversations

🔍 Smart Matching

Uses fuzzy matching to detect similar questions

Example:

“your name?”

“what is your name”

“whats ur name?”
→ All matched to the same stored answer

💾 Persistent Knowledge

All learned data is saved in chatbot_memory.json

Memory persists even after closing and reopening the program

📌 Lightweight & Dependency-Free

No NLTK, No ML models, No external APIs

Uses only built-in Python libraries
