import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API using the key stored in .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_model(model_name="gemini-2.5-pro"):
    """
    Initializes and returns a Gemini model.
    Default is the fast and cost-efficient gemini-1.5-flash.
    """
    return genai.GenerativeModel(model_name)
