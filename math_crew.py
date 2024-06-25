from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
ollama_llama3 = Ollama(model="llama3")


general_agent = Agent(role = "Math Professor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
                      allow_delegation = False,
                      llm = ollama_llama3,
                      memory=True)
task = Task (description="""{prompt}""",
             agent = general_agent,
             expected_output="A numerical answer.")

mcrew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=2
        )