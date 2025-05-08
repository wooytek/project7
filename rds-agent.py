# agent.py
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from db_connection import get_database
import os

os.environ["OPENAI_API_KEY"] = ""

def get_sql_agent():
    db = get_database()
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = initialize_agent(
        toolkit.get_tools(),
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent_executor

