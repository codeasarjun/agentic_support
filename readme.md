# Multi-Agent Customer Support Escalation System

An AI-powered multi-agent customer support system built using LangGraph, LangChain, and Ollama.

This project simulates a real-world customer support workflow where multiple AI agents collaborate to:
- classify support tickets
- analyze customer sentiment
- resolve issues
- retrieve knowledge-base answers
- escalate critical cases to humans

The system is fully local and can run using Ollama models like `llama3.2`.

---

# Features

## Multi-Agent Workflow
The system contains specialized agents with independent responsibilities.

### Agents
- Triage Agent
- Billing Support Agent
- Technical Support Agent
- FAQ Agent
- Sentiment Analysis Agent
- Escalation Agent

---

## Ticket Classification
Automatically categorizes tickets into:
- billing
- technical
- refund
- account
- complaint

---

## Sentiment Detection
Analyzes customer tone:
- angry
- frustrated
- neutral
- happy
- urgent

---

## Intelligent Escalation
Escalates tickets when:
- sentiment is highly negative
- confidence is low
- issue cannot be resolved
- refund/legal keywords appear

---

## Conversation Memory
Stores:
- previous interactions
- ticket history
- escalation history
- customer context

---

## Local LLM Support
Runs locally using Ollama.

Supported models:
- llama3.2


---

# Architecture

```text
need to add img
```

---

# Tech Stack

| Component | Technology |
|---|---|
| LLM | Ollama |
| Models | llama3.2 |
| Framework | LangChain |
| Orchestration | LangGraph |
| Backend | FastAPI |
| UI | Streamlit |
| Database | SQLite |
| Vector Store | ChromaDB |

---

# Project Structure

```text
customer_support_ai/
│
├── agents/
│   ├── triage_agent.py
│   ├── billing_agent.py
│   ├── technical_agent.py
│   ├── faq_agent.py
│   ├── sentiment_agent.py
│   └── escalation_agent.py
│
├── graph/
│   └── workflow.py
│
├── prompts/
│   └── prompts.py
│
├── memory/
│   └── chat_memory.py
│
├── database/
│   └── tickets.db
│
├── ui/
│   └── app.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>

cd customer_support_ai
```

---

## 2. Create Virtual Environment

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama:

https://ollama.com/

---

# Pull LLM Model

```bash
ollama pull llama3.2
```

---

# Run Ollama

```bash
ollama run llama3.2
```

---

# Environment Variables

Create a `.env` file:

```env
MODEL_NAME=llama3.2:latest
TEMPERATURE=0
```

---

# Running the Application

## Run Backend

```bash
python main.py
```

---

## Run Streamlit UI

```bash
streamlit run ui/app.py
```

---

# Example Ticket

```text
I was charged twice for my subscription and nobody has responded for 3 days.
```

---

# Example Workflow

```text
Ticket Received
      ↓
Triage Agent
      ↓
Billing Agent
      ↓
Sentiment Analysis
      ↓
Escalation Decision
      ↓
Human Escalation
```

---




# Objectives

This project demonstrates:
- Multi-agent orchestration
- AI workflow design
- LangGraph state management
- LLM routing
- Memory systems
- Human escalation pipelines



# Sample Agent Responsibilities

| Agent | Responsibility |
|---|---|
| Triage Agent | Ticket classification |
| Billing Agent | Payment/refund issues |
| Technical Agent | Bug troubleshooting |
| FAQ Agent | General support |
| Sentiment Agent | Emotion detection |
| Escalation Agent | Human escalation |

---


# License

MIT License

---




Built using:
- LangChain
- LangGraph
- Ollama
- Streamlit
- FastAPI