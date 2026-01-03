from orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()

    user_query = "Explain Gradient Descent"
    final_answer = orchestrator.run(user_query)

    print("\nFINAL OUTPUT:\n")
    print(final_answer)
