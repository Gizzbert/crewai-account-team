# AccountTeam Crew

Welcome to the AccountTeam Crew project, powered by [crewAI](https://crewai.com). 

Installing this repo will give you a team of highly skilled workers ready to go at a moments notice. They are specifically geared toward helping account and sales teams of consulting companies to prepare a first or follow-up client meeting.

In the current setup the crew will go out and gather inputs regardin the client, their long term outlook, their delivery strategies and your contact. Armed with this information they will synthesize a value proposition, a set of reports on the industry and a meeting agenda.

The crew consists of the following specialists:
- Strategic researcher, responsible for gathering and analyzing comprehensive information about the client, their role, company, and industry to inform the meeting strategy.
- Agile product delivery expert, tasked with developing a tailored agile product delivery strategy that aligns with the client's role and company bjectives.
- Meeting strategist, responsible for crafting an effective meeting strategy and agenda that maximizes the potential for a successful engagement with the client.
- Quality assurance specialist, ensuring the accuracy, coherence, and strategic alignment of all outputs produced by the team, providing critical feedback for refinement. (not engaged in the current setup)
- Project Manager, making sure the right roles do their task at the right moment and information is shared when applicable (not engaged in the current setup)


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI/Claude API_KEY` into the `.env` file** (note that the current install uses Claude 3.5 Sonnet LLM)

- Copy .env.example to .env and add in your API keys
- Modify `src/account_team/config/agents.yaml` to refine your agents
- Modify `src/account_team/config/tasks.yaml` to refine your tasks
- Modify `src/account_team/crew.py` and pay specific attention to the llm used (you need an api key)
- Copy & modify `src/account_team/config/client_details.yaml` to match your client

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the account_team Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a set of reports with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The account_team Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

