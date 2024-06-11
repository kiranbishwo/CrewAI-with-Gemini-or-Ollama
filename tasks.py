from crewai import Task
from tools import search_tool
from agents import researcher,news_writer

research_task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=researcher,
    tools=[search_tool]
)  # Creating an instance of the Task class with the specified description, expected output, agent, and tools

write_task = Task(
    description='Write a news article on the latest AI news',
    expected_output='A well-written news article on the latest AI news',
    agent=news_writer,
    context=[research_task],
    async_execution=False,
    output_file='news_article.md'
)  