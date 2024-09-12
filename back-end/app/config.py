import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
