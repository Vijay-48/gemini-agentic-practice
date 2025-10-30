from agents.coordinator import Coordinator

def main():
    print("=== Gemini Multi-Agent Intelligence System ===")
    topic = input("Enter a topic to research and verify: ").strip()

    coordinator = Coordinator()
    final_report = coordinator.run_pipeline(topic)

    print("\n✅ VERIFIED SUMMARY:\n")
    print(final_report)

if __name__ == "__main__":
    main()
