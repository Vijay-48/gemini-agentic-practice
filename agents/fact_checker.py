from utils.config import get_gemini_model

class FactCheckerAgent:
    """
    Validates the Analyst's output by checking factual consistency.
    Uses Gemini to cross-reference claims and highlight uncertain points.
    """

    def __init__(self):
        self.model = get_gemini_model()

    def verify(self, topic, summary):
        """
        Cross-checks the summary content for accuracy.
        """
        prompt = f"""
        You are a fact-checking AI. Review the following summary about '{topic}'.
        Identify any questionable claims or missing evidence.
        Suggest corrections or mark it 'Verified' if factual consistency is strong.

        --- SUMMARY ---
        {summary}
        """

        print(f"[🕵️‍♂️] Fact-checking analysis for: {topic}")
        response = self.model.generate_content(prompt)
        return response.text.strip()
