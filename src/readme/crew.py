from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool, FileReadTool


@CrewBase
class ReadmeCrew():
	"""Readme crew"""

	@agent
	def explorer_agent(self) -> Agent:
		"""Agent to explore the project directory and list its files."""
		return Agent(
			config=self.agents_config['explorer_agent'],
			tools=[DirectoryReadTool(), FileReadTool()],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def analyzer_agent(self) -> Agent:
		"""Agent to analyze the project directory and generate a summary."""
		return Agent(
			config=self.agents_config['analyzer_agent'],
			tools=[DirectoryReadTool(), FileReadTool()],
			verbose=True
		)

	@agent
	def writer_agent(self) -> Agent:
		"""Agent to write the README file."""
		return Agent(
			config=self.agents_config['writer_agent'],
			verbose=True
		)
  
	@agent
	def translator_agent(self) -> Agent:
		"""Agent to translate the README file to Spanish."""
		return Agent(
			config=self.agents_config['translator_agent'],
			verbose=True
		)

	@task
	def explore_task(self) -> Task:
		"""Task to explore the project directory and list its files."""
		return Task(
			config=self.tasks_config['explore_task'],
			tools=[DirectoryReadTool(), FileReadTool()],
			expected_output='Directory analyzed with files listed and described',
			output_file='1-Directory_content.md'
		)

	@task
	def analyze_project_task(self) -> Task:
		"""Task to analyze the project directory and generate a summary."""
		return Task(
			config=self.tasks_config['analyze_project_task'],
			tools=[DirectoryReadTool(), FileReadTool()],
			expected_output='Project summary with execution logic and purpose explained',
			output_file='2-Project_summary.md'
		)

	@task
	def write_readme_task(self) -> Task:
		"""Task to write the README file."""
		return Task(
			config=self.tasks_config['write_readme_task'],
			output_file='3-README.md'
		)

	@task
	def translate_readme_task(self) -> Task:
		"""Task to translate the README file to Spanish."""
		return Task(
			config=self.tasks_config['translate_readme_task'],
			output_file='4-README_es.md'
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
