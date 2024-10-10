#!/usr/bin/env python
import sys
from account_team.crew import AccountTeamCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load client details from client_details.yaml file
import yaml
def load_client_details(config_file):
	with open(config_file, 'r') as file:
		return yaml.safe_load(file)

# Load client configuration globally
client_config = load_client_details('src/account_team/config/client_details.yaml')

def run():
	"""
	Run the crew.
	"""
	inputs = {
		"client_name": client_config['client']['name'],
		"client_industry": client_config['client']['industry'],
		"contact_name": client_config['client']['contact']['name'],
		"contact_linkedin": client_config['client']['contact']['linkedin'],
		"contact_role": client_config['client']['contact']['role'],
	}

	try:
		AccountTeamCrew().crew().kickoff(inputs=inputs)
	except Exception as e:
		raise Exception(f"An error occurred while running the crew: {e}")

def train():
	"""
	Train the crew for a given number of iterations.
	"""
	inputs = {
		"client_name": client_config['client']['name'],
		"client_industry": client_config['client']['industry'],
		"contact_name": client_config['client']['contact']['name'],
		"contact_linkedin": client_config['client']['contact']['linkedin'],
		"contact_role": client_config['client']['contact']['role'],
	}
	try:
		AccountTeamCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

	except Exception as e:
		raise Exception(f"An error occurred while training the crew: {e}")

def replay():
	"""
	Replay the crew execution from a specific task.
	"""
	try:
		AccountTeamCrew().crew().replay(task_id=sys.argv[1])

	except Exception as e:
		raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
	"""
	Test the crew execution and returns the results.
	"""
	inputs = {
		"client_name": client_config['client']['name'],
		"client_industry": client_config['client']['industry'],
		"contact_name": client_config['client']['contact']['name'],
		"contact_linkedin": client_config['client']['contact']['linkedin'],
		"contact_role": client_config['client']['contact']['role'],
	}
	try:
		AccountTeamCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

	except Exception as e:
		raise Exception(f"An error occurred while replaying the crew: {e}")
