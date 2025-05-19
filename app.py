from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os

from utils.sheet_api import record_progress
from quiz_logic import get_quiz_question, check_answer

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Global variable to store user's last quiz question (if needed later for extension)
user_last_question = {}

@app.route("/bot", methods=['POST'])

def bot():
    msg_body = request.values.get('Body', '').lower()
    user_number = request.values.get('From', '')  # Unique identifier
    print(f"User: {user_number} | Message: {msg_body}")

    resp = MessagingResponse()
    msg = resp.message()

    if 'lesson' in msg_body:
        msg.body("📖 Hindi Lesson:\nभारत की स्वतंत्रता संग्राम 1857 में शुरू हुआ और 1947 में भारत को आज़ादी मिली। इसमें महात्मा गांधी, भगत सिंह, और नेताजी सुभाष चंद्र बोस जैसे नेता शामिल थे।")
    
    elif 'quiz' in msg_body:
        quiz = get_quiz_question()
        user_last_question[user_number] = quiz  # Optional: Save if multi-question logic is needed
        msg.body(f"📝 {quiz['question']}\nA) {quiz['options'][0]}\nB) {quiz['options'][1]}\nC) {quiz['options'][2]}")
    
    elif msg_body in ['a', 'b', 'c']:
        correct = check_answer(msg_body)
        record_progress(user_number, 1 if correct else 0)
        msg.body("✅ सही उत्तर! बहुत बढ़िया!" if correct else "❌ गलत उत्तर। अगली बार सही करने की कोशिश करें।")
    
    else:
        msg.body("🙏 Welcome to Rural Learning Bot!\n\nType:\n👉 `lesson` – to receive today's learning\n👉 `quiz` – to take a quick quiz")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
