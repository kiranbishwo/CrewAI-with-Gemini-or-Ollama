import os
from crewai import Crew,Process
from agents import researcher,news_writer,geminai_llm
from tasks import research_task,write_task


crew = Crew(
    agents=[researcher,news_writer],
    tasks=[research_task,write_task],
    llm=geminai_llm,
    verbose=2,
)

result = crew.kickoff()  
print(result) 