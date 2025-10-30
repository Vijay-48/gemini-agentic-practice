from utils.search import web_search

class ResearcherAgent:
    """
    The Researcher Agent is responsible for gathering raw information
    from the web before analysis.
    """

    def __init__(self):
        pass

    def collect_data(self, topic):
        """
        Searches the web for the topic and returns textual data.
        """
        print(f"[🔎] Collecting data for topic: {topic}")
        data = web_search(topic, max_results=5)
        if not data:
            print("[⚠️] No data found.")
        return "\n\n".join(data)
