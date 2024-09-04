from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, la team!'

if __name__ == '__main__':
    app.run(debug=True)


print(f"DB Username: {db_username}")
print(f"DB Password: {db_password}")
print(f"DB Name: {db_name}")
