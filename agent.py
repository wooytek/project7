from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from db_connection import get_database
import openai
import os

# Set OpenAI key
os.environ["OPENAI_API_KEY"] = ""  # Replace with your actual key
openai.api_key = os.environ["OPENAI_API_KEY"]

# LangChain SQL Agent setup
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
db = get_database()
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
sql_agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)

# Fallback for general-purpose LLM response
def fallback_llm_response(question: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Failed to fetch response from LLM: {str(e)}"

# Combined routing logic
def query_database_or_llm(question: str) -> str:
    db_keywords = ["employee", "salary", "join", "table", "select", "from", "where", "date", "position"]
    if any(keyword in question.lower() for keyword in db_keywords):
        try:
            return sql_agent.run(question)
        except Exception as e:
            return f"⚠️ DB agent error: {str(e)}"
    else:
        return fallback_llm_response(question)
