import mysql.connector
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os

# Load environment variables (.env for local; env vars in GKE)
load_dotenv()

# Connect to MySQL (Cloud SQL or local)
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

cursor = conn.cursor()

# Cleanup old data
cursor.execute("DELETE FROM incorrect_answers")
cursor.execute("DELETE FROM questions")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM scores")
conn.commit()

# Insert quiz data
question_data = [
    {
        "question": "The Apostle Paul's first letter in the New Testament is to the Galatians.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "question": "King Ahab's wife was Jezebel.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }
    # ✅ Add more as needed
]

for q in question_data:
    cursor.execute(
        "INSERT INTO questions (question_text, correct_answer) VALUES (%s, %s)",
        (q["question"], q["correct_answer"])
    )
    question_id = cursor.lastrowid
    for wrong in q["incorrect_answers"]:
        cursor.execute(
            "INSERT INTO incorrect_answers (question_id, answer_text) VALUES (%s, %s)",
            (question_id, wrong)
        )

# Insert users
users = [
    {"email": "test@example.com", "password_hash": generate_password_hash("test1234"), "is_admin": False},
    {"email": "msuryaprasad11@gmail.com", "password_hash": generate_password_hash("Admin123"), "is_admin": True}
]

for user in users:
    cursor.execute(
        "INSERT INTO users (email, password_hash, is_admin) VALUES (%s, %s, %s)",
        (user["email"].strip(), user["password_hash"], user["is_admin"])
    )

# Insert example score
cursor.execute(
    "INSERT INTO scores (user_email, score) VALUES (%s, %s)",
    ("test@example.com", 100)
)

# Finalize
conn.commit()
cursor.close()
conn.close()

print("✅ Cloud SQL (MySQL) seeded successfully.")
