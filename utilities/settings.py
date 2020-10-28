from dotenv import load_dotenv
import os

load_dotenv()

sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
