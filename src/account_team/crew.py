from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from litellm import completion

# Add this import
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

@CrewBase
class AccountTeamCrew():
	"""AccountTeam crew"""

	@agent
	def strategic_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['strategic_researcher'],
			verbose=True,
			#llm='perplexity/pplx-7b-chat',
			llm='claude-3-5-sonnet-20240620',
		)

	@agent
	def agile_product_delivery_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['agile_product_delivery_expert'],
			verbose=True,
			#llm='claude-3-opus-20240229',
			llm='claude-3-5-sonnet-20240620',
		)

	@agent
	def meeting_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['meeting_strategist'],
			verbose=True,
			#llm='o1-preview',
			llm='gpt-4o',
		)

	@agent
	def quality_assurance_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['quality_assurance_specialist'],
			verbose=True,
			#llm='o1-preview',
			llm='claude-3-5-sonnet-20240620',
		)

	@task
	def client_company_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['client_company_analysis'],
		)

	@task
	def client_role_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['client_role_analysis'],
		)

	@task
	def industry_trend_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['industry_trend_analysis'],
		)

	@task
	def review_initial_analyses(self) -> Task:
		return Task(
			description="Review the client company analysis, client role analysis, and industry trend analysis for accuracy and completeness.",
			agent=self.quality_assurance_specialist(),
		)

	@task
	def agile_strategy_development(self) -> Task:
		return Task(
			config=self.tasks_config['agile_strategy_development'],
		)

	@task
	def value_proposition_creation(self) -> Task:
		return Task(
			config=self.tasks_config['value_proposition_creation'],
		)

	@task
	def review_strategy_and_value_proposition(self) -> Task:
		return Task(
			description="Review the agile strategy and value proposition for effectiveness and alignment with client needs.",
			agent=self.quality_assurance_specialist(),
		)

	@task
	def meeting_agenda_creation(self) -> Task:
		return Task(
			config=self.tasks_config['meeting_agenda_creation'],
		)

	@task
	def engagement_strategy_formulation(self) -> Task:
		return Task(
			config=self.tasks_config['engagement_strategy_formulation'],
		)

	@task
	def review_meeting_strategy(self) -> Task:
		return Task(
			description="Review the meeting agenda and engagement strategy for effectiveness and alignment with overall objectives.",
			agent=self.quality_assurance_specialist(),
		)

	@task
	def final_briefing_compilation(self) -> Task:
		return Task(
			config=self.tasks_config['final_briefing_compilation'],
			output_file='final_briefing.md'
		)

	@task
	def final_briefing_review(self) -> Task:
		return Task(
			description="Perform a comprehensive review of the final briefing, ensuring all elements are accurate, cohesive, and aligned with the client's needs.",
			agent=self.quality_assurance_specialist(),
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
				self.review_initial_analyses(),
				self.agile_strategy_development(),
				self.value_proposition_creation(),
				self.review_strategy_and_value_proposition(),
				self.meeting_agenda_creation(),
				self.engagement_strategy_formulation(),
				self.review_meeting_strategy(),
				self.final_briefing_compilation(),
				self.final_briefing_review()
			],
			process=Process.sequential,
			verbose=True,
		)