import json
import os

class MemoryAgent:
    """
    The Memory Agent is a simple JSON-based persistence layer.
    It stores and retrieves past topic summaries.
    """

    def __init__(self, filepath="data/summaries.json"):
        self.filepath = filepath
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump({}, f)

    def save_summary(self, topic, summary):
        """
        Saves the summary for the given topic.
        """
        with open(self.filepath, "r+") as f:
            data = json.load(f)
            data[topic] = summary
            f.seek(0)
            json.dump(data, f, indent=4)
        print(f"[💾] Saved summary for '{topic}'.")

    def get_summary(self, topic):
        """
        Returns saved summary for a topic if exists.
        """
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return data.get(topic, None)
