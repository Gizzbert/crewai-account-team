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

def run():
	"""
	Run the crew.
	"""
	inputs = {
		"company": "Port of Amsterdam",
		"clientname": "Andrew Woodham",
		"linkedin": "https://www.linkedin.com/in/andrewwoodham/",
		"role": "Head of IT",
		"industry": "Ports"
	}
	AccountTeamCrew().crew().kickoff(inputs=inputs)

def train():
	"""
	Train the crew for a given number of iterations.
	"""
	inputs = {
		"company": "Port of Amsterdam",
		"clientname": "Andrew Woodham",
		"linkedin": "https://www.linkedin.com/in/andrewwoodham/",
		"role": "Head of IT",
		"industry": "Ports"
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
		"topic": "Port of Amsterdam"
	}
	try:
		AccountTeamCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

	except Exception as e:
		raise Exception(f"An error occurred while replaying the crew: {e}")
