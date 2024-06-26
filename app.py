# app.py
from flask import Flask, request, jsonify
from crewai import Agent, Task, Crew
from math_crew import mcrew
from job_posting.job_crew import create_tasks_crew
from langchain.llms import Ollama
ollama_llama3 = Ollama(model="llama3")

app = Flask(__name__)

@app.route('/route_prompt', methods=['POST'])
def route_prompt():
    data = request.get_json()
    general_agent = Agent(role = "Prompt Analyser",
                      goal = """Analyses whether a given prompt is for performing mathematical operation or generating job description or neither of the two, the answer should be always between the three words - 'math' or 'job' or 'none'""",
                      backstory = """You are an excellent prompt analyser who can figure out a prompt is meant for which task - 'math' for prompts meant for performing mathematical operation, 'job' for prompts meant for generating job description and 'none' for neither of the two""",
                      allow_delegation = False,
                      llm = ollama_llama3,
                      memory=True)
    task = Task (description="""{prompt}""",
                agent = general_agent,
                expected_output="Answer in a single word - 'math' or 'job' or 'none'")

    crew = Crew(
                agents=[general_agent],
                tasks=[task],
                verbose=2
            )

    result = crew.kickoff(inputs=data)
    
    if result=='math':
        result = mcrew.kickoff(inputs=data)
    elif result=='job':
        jcrew = create_tasks_crew(data["prompt"])
        result = jcrew.kickoff()
    else:
        result = {"error": "The prompt does not match any known task. Please provide a mathematical expression or request a job description."}
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
