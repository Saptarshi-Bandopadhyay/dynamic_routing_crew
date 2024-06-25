from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from job_posting.tasks import Tasks
from job_posting.agents import Agents

tasks = Tasks()
agents = Agents()


# Create Agents
researcher_agent = agents.research_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

# Define Tasks for each agent
def create_tasks_crew(company_description):
    research_company_culture_task = tasks.research_company_culture_task(researcher_agent, company_description)
    industry_analysis_task = tasks.industry_analysis_task(researcher_agent, company_description)
    research_role_requirements_task = tasks.research_role_requirements_task(researcher_agent, company_description)
    draft_job_posting_task = tasks.draft_job_posting_task(writer_agent, company_description)
    review_and_edit_job_posting_task = tasks.review_and_edit_job_posting_task(review_agent, company_description)

    # Instantiate the crew with a sequential process
    jcrew = Crew(
        agents=[researcher_agent, writer_agent, review_agent],
        tasks=[
            research_company_culture_task,
            industry_analysis_task,
            research_role_requirements_task,
            draft_job_posting_task,
            review_and_edit_job_posting_task
        ]
    )

    return jcrew