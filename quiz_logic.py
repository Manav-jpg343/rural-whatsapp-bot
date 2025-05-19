import random

# Predefined set of quiz questions
quiz_data = [
    {
        "question": "भारत की राजधानी क्या है?",
        "options": ["मुंबई", "दिल्ली", "कोलकाता"],
        "answer": "b"
    },
    {
        "question": "महात्मा गांधी का जन्म कब हुआ था?",
        "options": ["1869", "1857", "1901"],
        "answer": "a"
    },
    {
        "question": "भारत ने आज़ादी कब प्राप्त की?",
        "options": ["1947", "1950", "1930"],
        "answer": "a"
    }
]

# Stores the last asked question globally (optional for future improvements)
current_question = {}

def get_quiz_question():
    global current_question
    current_question = random.choice(quiz_data)
    return current_question

def check_answer(user_input):
    global current_question
    return user_input.lower() == current_question['answer']
