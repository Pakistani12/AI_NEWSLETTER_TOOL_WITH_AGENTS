# AI_NEWSLETTER_TOOL_WITH_AGENTS
This project leverages **CrewAI** to automate research, writing, and proofreading using **Groq's Llama 3.1-70B** model. It integrates **SerperDevTool** for web search capabilities, making it ideal for generating insights on various topics.

## **Features**
- **Researcher Agent**: Analyzes trends and gathers insights.
- **Writer Agent**: Transforms research into engaging articles.
- **Proofreader Agent**: Ensures clarity, accuracy, and proper citations.
- **Google Search Integration**: Fetches real-time information for up-to-date content.
1- Create Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate
```
2- Install Dependencies
```sh
pip install -r requirements.txt
```
3- Set Up API Keys
- Create a .env file in the project root and add
```sh
GROQ_API_KEY=""
SERPER_API_KEY=""
```
## **Usage**
```sh
python crew.py
```
## **Project Structure**
```plaintxt
├── agents.py        # Defines AI agents (Researcher, Writer, Proofreader)
├── tasks.py         # Defines tasks for each agent
├── tools.py         # Initializes search tool (Google Search via Serper API)
├── crew.py          # Orchestrates the workflow
├── requirements.txt # Required dependencies
├── README.md        # Documentation
├── .env             # API keys
```
