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
class ReadmeCrew2():
	"""Readme crew 2"""
 
	agents_config = "config/agents2.yaml"   
	tasks_config = "config/tasks2.yaml"

	@agent
	def writer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['writer_agent'],
			tools=[DirectoryReadTool(), FileReadTool()],
			verbose=True
		)
  
	@agent
	def translator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['translator_agent'],
			tools=[DirectoryReadTool(), FileReadTool()],
			verbose=True
		)

	@task
	def write_readme_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_readme_task'],
			tools=[DirectoryReadTool(), FileReadTool()],
			output_file='README.md'
		)

	@task
	def translate_readme_task(self) -> Task:
		return Task(
			config=self.tasks_config['translate_readme_task'],
			tools=[DirectoryReadTool(), FileReadTool()],
			output_file='README_es.md'
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