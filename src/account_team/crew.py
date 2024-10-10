from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from litellm import completion
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

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
			verbose=True,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=True,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def agile_product_delivery_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['agile_product_delivery_expert'],
			verbose=True,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=True,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def meeting_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['meeting_strategist'],
			verbose=True,
			llm='claude-3-5-sonnet-20240620',
			allow_delegation=True,
			tools = [scrape_tool, search_tool]
		)

	@agent
	def quality_assurance_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['quality_assurance_specialist'],
			verbose=True,
			llm='claude-3-5-sonnet-20240620',
			tools = [scrape_tool, search_tool]
		)

	@task
	def client_company_analysis(self) -> Task:
		return Task(config=self.tasks_config['client_company_analysis'])

	@task
	def review_client_company_analysis(self) -> Task:
		return Task(config=self.tasks_config['review_client_company_analysis'])

	@task
	def revise_client_company_analysis(self) -> Task:
		return Task(config=self.tasks_config['revise_client_company_analysis'])

	@task
	def client_role_analysis(self) -> Task:
		return Task(config=self.tasks_config['client_role_analysis'])

	@task
	def review_client_role_analysis(self) -> Task:
		return Task(config=self.tasks_config['review_client_role_analysis'])

	@task
	def revise_client_role_analysis(self) -> Task:
		return Task(config=self.tasks_config['revise_client_role_analysis'])

	@task
	def industry_trend_analysis(self) -> Task:
		return Task(config=self.tasks_config['industry_trend_analysis'])

	@task
	def review_industry_trend_analysis(self) -> Task:
		return Task(config=self.tasks_config['review_industry_trend_analysis'])

	@task
	def revise_industry_trend_analysis(self) -> Task:
		return Task(config=self.tasks_config['revise_industry_trend_analysis'])

	@task
	def agile_strategy_development(self) -> Task:
		return Task(config=self.tasks_config['agile_strategy_development'])

	@task
	def review_agile_strategy(self) -> Task:
		return Task(config=self.tasks_config['review_agile_strategy'])

	@task
	def revise_agile_strategy(self) -> Task:
		return Task(config=self.tasks_config['revise_agile_strategy'])

	@task
	def value_proposition_creation(self) -> Task:
		return Task(config=self.tasks_config['value_proposition_creation'])

	@task
	def review_value_proposition(self) -> Task:
		return Task(config=self.tasks_config['review_value_proposition'])

	@task
	def revise_value_proposition(self) -> Task:
		return Task(config=self.tasks_config['revise_value_proposition'])

	@task
	def meeting_agenda_creation(self) -> Task:
		return Task(config=self.tasks_config['meeting_agenda_creation'])

	@task
	def review_meeting_agenda(self) -> Task:
		return Task(config=self.tasks_config['review_meeting_agenda'])

	@task
	def revise_meeting_agenda(self) -> Task:
		return Task(config=self.tasks_config['revise_meeting_agenda'])

	@task
	def engagement_strategy_formulation(self) -> Task:
		return Task(config=self.tasks_config['engagement_strategy_formulation'])

	@task
	def review_engagement_strategy(self) -> Task:
		return Task(config=self.tasks_config['review_engagement_strategy'])

	@task
	def revise_engagement_strategy(self) -> Task:
		return Task(config=self.tasks_config['revise_engagement_strategy'])

	@task
	def final_briefing_compilation(self) -> Task:
		return Task(
			config=self.tasks_config['final_briefing_compilation'],
			output_file='final_briefing.md'
		)

	@task
	def review_final_briefing(self) -> Task:
		return Task(config=self.tasks_config['review_final_briefing'])

	@task
	def revise_final_briefing(self) -> Task:
		return Task(config=self.tasks_config['revise_final_briefing'])

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
				self.review_client_company_analysis(),
				self.revise_client_company_analysis(),
				self.client_role_analysis(),
				self.review_client_role_analysis(),
				self.revise_client_role_analysis(),
				self.industry_trend_analysis(),
				self.review_industry_trend_analysis(),
				self.revise_industry_trend_analysis(),
				self.agile_strategy_development(),
				self.review_agile_strategy(),
				self.revise_agile_strategy(),
				self.value_proposition_creation(),
				self.review_value_proposition(),
				self.revise_value_proposition(),
				self.meeting_agenda_creation(),
				self.review_meeting_agenda(),
				self.revise_meeting_agenda(),
				self.engagement_strategy_formulation(),
				self.review_engagement_strategy(),
				self.revise_engagement_strategy(),
				self.final_briefing_compilation(),
				self.review_final_briefing(),
				self.revise_final_briefing()
			],
			process=Process.sequential,
			verbose=True,
		)