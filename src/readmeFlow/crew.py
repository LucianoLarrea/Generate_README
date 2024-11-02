import os	
import agentops
# from dotenv import load_dotenv
# load_dotenv()
# agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool, FileReadTool
# Uncomment the following line to use an example of a custom tool
# from readme.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ReadmeCrew():
	"""Readme crew"""

	@agent
	def explorer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['explorer_agent'],
			tools=[DirectoryReadTool(), FileReadTool()],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def analyzer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['analyzer_agent'],
			tools=[DirectoryReadTool(), FileReadTool()],
			verbose=True
		)


	@task
	def explore_task(self) -> Task:
		return Task(
			config=self.tasks_config['explore_task'],
			tools=[DirectoryReadTool(), FileReadTool()],
			expected_output='Directorio analizado con archivos listados'
		)

	@task
	def analyze_project_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_project_task'],
			tools=[DirectoryReadTool(), FileReadTool()],
			expected_output='Resumen del proyecto'
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Readme crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)