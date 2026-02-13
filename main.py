import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("⚠️ GEMINI_API_KEY not found in .env file")
    exit(1)

genai.configure(api_key=API_KEY)

print("===================================================")
print("   ██████  ███████ ███    ███ ██ ███    ██ ██ ")
print("  ██       ██      ████  ████ ██ ████   ██ ██ ")
print("  ██   ███ █████   ██ ████ ██ ██ ██ ██  ██ ██ ")
print("  ██    ██ ██      ██  ██  ██ ██ ██  ██ ██ ██ ")
print("   ██████  ███████ ██      ██ ██ ██   ████ ██ ")
print("")
print("                GEMINI_CLI")
print("===================================================")

while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        break
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        chat = model.start_chat()
        response = chat.send_message(user_input)
        print("gemini:", response.text)
    except Exception as e:
        print("Error:", e)