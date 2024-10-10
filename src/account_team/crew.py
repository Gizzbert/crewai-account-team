from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from litellm import completion
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from IPython.display import Markdown

# Warning control
import warnings
warnings.filterwarnings('ignore')

# Add this import
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

@CrewBase
class AccountTeamCrew():
	"""AccountTeam crew"""

	@agent
	def strategic_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['strategic_researcher'],
			verbose=False,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=False,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def agile_product_delivery_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['agile_product_delivery_expert'],
			verbose=False,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=False,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def meeting_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['meeting_strategist'],
			verbose=False,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=False,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def quality_assurance_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['quality_assurance_specialist'],
			verbose=False,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=True,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['project_manager'],
			verbose=False,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=True,
		)

	@task
	def client_company_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['client_company_analysis'],
			output_file='{client_name}_client_company_analysis_output.md',
		)

	@task
	def client_role_analysis(self) -> Task:
		return Task(config=self.tasks_config['client_role_analysis'],
			output_file='{client_name}_client_role_analysis_output.md',
		)

	@task
	def industry_trend_analysis(self) -> Task:
		return Task(config=self.tasks_config['industry_trend_analysis'],
			output_file='{client_name}_industry_trend_analysis_output.md',
		)

	@task
	def agile_strategy_development(self) -> Task:
		return Task(config=self.tasks_config['agile_strategy_development'],
			output_file='{client_name}_agile_strategy_output.md',
		)

	@task
	def value_proposition_creation(self) -> Task:
		return Task(config=self.tasks_config['value_proposition_creation'],
			output_file='{client_name}_value_proposition_output.md',
		)

	@task
	def meeting_agenda_creation(self) -> Task:
		return Task(config=self.tasks_config['meeting_agenda_creation'],
			output_file='{client_name}_meeting_agenda_output.md',
		)

	@task
	def engagement_strategy_formulation(self) -> Task:
		return Task(config=self.tasks_config['engagement_strategy_formulation'],
			output_file='{client_name}_engagement_strategy_output.md',
		)

	@task
	def final_briefing_compilation(self) -> Task:
		return Task(
			config=self.tasks_config['final_briefing_compilation'],
			output_file='{client_name}_final_briefing_output.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Client Meeting Preparation crew"""
		return Crew(
			agents=[
				self.strategic_researcher(),
				self.agile_product_delivery_expert(),
				self.meeting_strategist(),
				self.quality_assurance_specialist()
			],
			tasks=[
				self.client_company_analysis(),
				self.client_role_analysis(),
				self.industry_trend_analysis(),
				self.agile_strategy_development(),
				self.value_proposition_creation(),
				self.meeting_agenda_creation(),
				self.engagement_strategy_formulation(),
				self.final_briefing_compilation(),
			],
			process=Process.sequential,
#			process=Process.hierarchical,
#			manager_agent=self.project_manager(),
			verbose=True,
		)

