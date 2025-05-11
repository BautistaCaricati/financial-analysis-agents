# 🧠 Financial Analysis Agents (Open-Source, Local-LLM Version)

This project showcases a multi-agent system for **automated financial analysis** and **trading strategy development** using [CrewAI](https://docs.crewai.com), powered entirely by **free local LLMs via Ollama** (no OpenAI API key required).

---

## ✅ Key Features

- 📊 **Market Analysis** — monitor real-time market data
- 🧠 **Trading Strategy Generation** — generate and refine tactics based on trends and risk profiles
- ⚙️ **Execution Planning** — propose optimal entry/exit timing
- 🛡️ **Risk Management** — evaluate and mitigate exposure
- 💻 **100% Local** — runs with Ollama + Mistral, no paid APIs

---

## 🔧 Technologies Used

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [LiteLLM](https://github.com/BerriAI/litellm)
- [Ollama](https://ollama.com) with `mistral` model
- Python 3.10+
- LangChain (used by CrewAI under the hood)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/BautistaCaricati/financial-analysis-agents.git
cd financial-analysis-agents
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Ollama & Pull a Model

Install and start Ollama:

```bash
brew install ollama
ollama serve
ollama pull mistral
```

(You can replace `mistral` with another local model like `llama3` or `gemma:2b`.)

### 4. Run the Agent Crew

```bash
python main.py
```

---

## 📂 Project Structure

```
.
├── main.py               # Entry point to launch the Crew
├── agents/               # Definitions for each agent role
├── tasks/                # Definitions for CrewAI tasks
├── requirements.txt      # Python dependencies
└── README.md             # You're reading it
```

---

## 📌 Notes

- No OpenAI or Hugging Face keys are needed.
- Make sure Ollama is running in the background before launching `main.py`.

---

## 📜 License

MIT License — free to use, modify, and build upon.

---
