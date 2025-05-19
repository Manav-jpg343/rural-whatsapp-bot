import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from JSON key file
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

# Authorize the client
client = gspread.authorize(creds)

# Open your spreadsheet (replace with your sheet name)
sheet = client.open("RuralLearningProgress").sheet1

# Function to record progress
def record_progress(phone_number, score, question="", user_answer="", correct=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, phone_number, question, user_answer, "✅" if correct else "❌", score])
