# 🔍 Langchain Multi-Agent Research System

An autonomous multi-agent research pipeline that discovers, scrapes, synthesizes, and critiques research reports on any given topic. Built with **LangChain**, **Groq**, **Tavily Search**, **Trafilatura / BeautifulSoup**, and **Streamlit**.

---

## 📌 Architecture & Workflow

The system operates as a 4-stage pipeline orchestrated via specialized agents and chains:

```
                  ┌──────────────────────┐
                  │    User / Query      │
                  └──────────┬───────────┘
                             │
                             ▼
    [Step 1]       ┌──────────────────────┐
                   │     Search Agent     │  <-- Tavily Search Tool
                   └──────────┬───────────┘
                             │
                             ▼
    [Step 2]       ┌──────────────────────┐
                   │     Reader Agent     │  <-- Web Scraper (Trafilatura / BS4)
                   └──────────┬───────────┘
                             │
                             ▼
    [Step 3]       ┌──────────────────────┐
                   │     Writer Chain     │  <-- Structured Research Synthesis
                   └──────────┬───────────┘
                             │
                             ▼
    [Step 4]       ┌──────────────────────┐
                   │     Critic Chain     │  <-- Scoring & Quality Evaluation
                   └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  Final Report + Score│
                  └──────────────────────┘
```

1. **Step 1 - Search Agent**: Queries the web using Tavily API to collect top recent articles, sources, and snippets.
2. **Step 2 - Reader / Scraper Agent**: Inspects search findings, selects the most relevant URLs, and scrapes complete, clean article content using `trafilatura` (with `BeautifulSoup` fallback).
3. **Step 3 - Writer Chain**: Analyzes both search snippets and deep scraped content to draft a structured, professional research report (Introduction, Key Findings, Conclusion, Sources).
4. **Step 4 - Critic Chain**: Evaluates the drafted report for quality, providing a score out of 10, identified strengths, areas to improve, and a final verdict.

---

## 📁 Project Structure

```
Langchain-Multi-Agent-Research-System/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── agents.py          # Search agent, scrape agent, writer chain & critic chain
│   ├── pipelines/
│   │   ├── __init__.py
│   │   └── pipeline.py        # Pipeline orchestration (run_research_pipeline)
│   └── tools/
│       ├── __init__.py
│       └── tools.py           # Tavily search tool & web scraping tool
│
├── app.py                     # Streamlit frontend user interface
├── main.py                    # CLI entrypoint for testing the pipeline
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (API keys)
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10+
- [Groq API Key](https://console.groq.com/)
- [Tavily API Key](https://tavily.com/)

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/Langchain-Multi-Agent-Research-System.git
cd Langchain-Multi-Agent-Research-System
pip install -r requirements.txt
```

### 3. Environment Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 💻 Usage

### Run via Streamlit Web App (Recommended)

Launch the interactive web UI:

```bash
streamlit run app.py
```

- Enter any research topic.
- Track real-time agent execution progress.
- View and download the formatted Markdown report.
- Inspect critic evaluations and intermediate raw agent outputs.

### Run via Command Line Interface (CLI)

To run a quick pipeline test from the terminal:

```bash
python main.py
```

---

## 🛠️ Tech Stack

- **Framework**: LangChain / LangGraph
- **LLM Provider**: Groq (`ChatGroq`)
- **Web Search**: Tavily Search API (`tavily-python`)
- **Web Scraping**: Trafilatura, BeautifulSoup4, Requests
- **UI & Visualization**: Streamlit, Rich
- **Configuration**: Python-dotenv
