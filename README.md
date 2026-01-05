# Standalone Multi-Agent AI Core Engine

A **framework-style, standalone multi-agent AI system** designed to demonstrate how multiple specialized agents can collaboratively solve a user query using **planning, explanation, evaluation, and feedback**.

This project focuses purely on **agent orchestration and communication**, without UI or product-level complexity, making it ideal for understanding and explaining **multi-agent AI architectures**.

## Project Overview

Modern AI systems require more than a single model response.  
This project implements a **clean, minimal multi-agent pipeline** where each agent performs a single responsibility and is coordinated by a central orchestrator.

The system processes a user query through four agents:

1. **Planner Agent** – breaks the task into logical steps  
2. **Explainer Agent** – generates an initial structured answer  
3. **Evaluator Agent** – critiques correctness and identifies gaps  
4. **Feedback Agent** – refines and improves the final response  

This creates a **closed feedback loop**, enabling self-improving AI behavior.

## System Architecture

```text
User Query
↓
Orchestrator
↓
Planner Agent → Task Decomposition
↓
Explainer Agent → Draft Answer
↓
Evaluator Agent → Quality Check
↓
Feedback Agent → Improved Final Answer
```

## Folder Structure
```text
multi_agent_core/
│
├── agents/
│ ├── base_agent.py # Abstract base class for all agents
│ ├── planner.py # Task decomposition agent
│ ├── explainer.py # Answer generation agent
│ ├── evaluator.py # Answer evaluation agent
│ └── feedback.py # Answer refinement agent
│
├── orchestrator.py # Controls agent execution order
├── llm_client.py # Centralized LLM abstraction (mocked)
├── main.py # Entry point
└── README.md
```

## Agents Description

### Planner Agent
- Breaks a user query into clear, logical steps
- Normalizes LLM output into a structured list
- Prevents prompt leakage to downstream agents

### Explainer Agent
- Generates a structured explanation
- Follows the plan produced by the Planner
- Focuses on clarity and completeness

### Evaluator Agent
- Critiques the generated answer
- Identifies missing points and issues
- Produces structured evaluation output

### Feedback Agent
- Uses evaluator feedback
- Improves clarity, correctness, and coverage
- Closes the multi-agent feedback loop

## LLM Abstraction

All model interactions are routed through a single `LLMClient`.

This design allows easy replacement with:
- OpenAI
- Gemini
- Local LLMs

without changing agent logic.

## How to Run

```bash
python main.py

Example query (inside main.py):

"Explain Gradient Descent"
```
