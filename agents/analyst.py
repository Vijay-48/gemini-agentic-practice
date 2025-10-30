from utils.config import get_gemini_model

class AnalystAgent:
    """
    The Analyst Agent takes collected data and distills it into key insights.
    It uses Gemini's large context and reasoning capabilities.
    """

    def __init__(self):
        self.model = get_gemini_model()

    def analyze(self, topic, text):
        """
        Generates a concise, insightful summary for the given text.
        """
        if not text:
            return "[❌] No data provided for analysis."
        
        prompt = f"""
        You are a data intelligence analyst.
        Summarize the following web research on '{topic}' into clear, 
        structured insights (3–5 points), focusing on patterns, trends, 
        and implications:\n\n{text}
        """
        
        print(f"[🧠] Analyzing information on: {topic}")
        response = self.model.generate_content(prompt)
        return response.text.strip()
