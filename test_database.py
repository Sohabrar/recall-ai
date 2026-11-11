
from database import test_connection

try:
    if test_connection():
        print("SUCCESS! Recall AI is connected to MongoDB! 💚")

except Exception as e:
    print("MongoDB connection failed.")
    print("Error:", e)
