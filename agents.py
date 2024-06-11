from crewai import Agent
import os
from langchain_community.llms import Ollama  # Importing the Ollama class from the langchain_community.llms module
from tools import search_tool
from dotenv import load_dotenv  # Importing the load_dotenv function from the dotenv module
from langchain_google_genai import ChatGoogleGenerativeAI  # Importing the ChatGoogleGenerativeAI class from the langchain_google_genai module
load_dotenv()

ollama_lama = Ollama(model="llama3") 
geminai_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                     verbose=True,
                                     temperature=0.5,
                                     google_api_key=os.getenv("GOOGLE_API_KEY"))  # Creating an instance of the ChatGoogleGenerativeAI class with the specified model, verbosity, temperature, and Google API key


researcher = Agent(
    role='Researcher',
    goal='Find and summarize the latest AI news',
    backstory="""You're a researcher at a large company.
    You're responsible for analyzing data and providing insights
    to the business.""",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    llm=geminai_llm
)  # Creating an instance of the Agent class with the specified role, goal, backstory, verbosity, and language model

news_writer = Agent(
    role='News Writer',
    goal='Write a news article on the latest AI news',
    backstory="""You're a news writer at a popular tech news website.
    You're responsible for writing engaging and informative news articles
    on the latest AI news.""",
    verbose=True,
    tools=[],
    llm=geminai_llm
)  # Creating an instance of the Agent class with the specified role, goal, backstory, verbosity, and language model
