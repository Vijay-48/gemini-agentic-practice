from agents.researcher import ResearcherAgent
from agents.analyst import AnalystAgent
from agents.fact_checker import FactCheckerAgent
from agents.memory import MemoryAgent

class Coordinator:
    """
    The Coordinator orchestrates the workflow across multiple agents.
    It decides execution order, merges results, and ensures memory persistence.
    """

    def __init__(self):
        self.researcher = ResearcherAgent()
        self.analyst = AnalystAgent()
        self.fact_checker = FactCheckerAgent()
        self.memory = MemoryAgent()

    def run_pipeline(self, topic):
        # Step 1: Check memory
        cached = self.memory.get_summary(topic)
        if cached:
            print(f"[🧠 Memory] Cached result found for '{topic}'.")
            return cached

        # Step 2: Research phase
        data = self.researcher.collect_data(topic)

        # Step 3: Analysis phase
        summary = self.analyst.analyze(topic, data)

        # Step 4: Verification phase
        verified = self.fact_checker.verify(topic, summary)

        # Step 5: Save and return
        self.memory.save_summary(topic, verified)
        return verified
