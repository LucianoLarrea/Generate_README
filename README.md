# Project README Generator

## Overview

The **Project README Generator** is a tool designed to automate the exploration, analysis, and documentation of software projects by generating README files automatically. This project leverages a series of intelligent agents to carry out specific tasks, including exploring the directory structure, analyzing its content, writing the README file, and even translating it into different languages if necessary.

## Purpose

The primary purpose of this project is to enhance the efficiency and accuracy of software documentation. By automating the README generation process, developers can save time and ensure that their documentation is comprehensive and up-to-date. This project is particularly useful for large codebases where manual documentation can be cumbersome and error-prone.

## Execution Logic

The execution of the Project README Generator starts with the `main.py` script, which initializes an instance of the `ReadmeCrew` class found in `crew.py`. This instance orchestrates a team of agents that work together to accomplish the README generation tasks. The primary functionalities include:

1. **Exploration:** The `explorer_agent` investigates the project directory, systematically listing all files and relevant information.
2. **Analysis:** The `analyzer_agent` processes the gathered data from the exploration phase to generate a comprehensive summary of the project's structure and its components.
3. **Documentation:** The `writer_agent` compiles the analysis into a structured README file.
4. **Translation (optional):** The `translator_agent` can provide a translation of the README into Spanish, facilitating broader accessibility and usage.

The execution is orchestrated through the `kickoff` method of the `ReadmeCrew`, which accepts a directory path as input and coordinates the tasks defined within the crew.

## Key Files and Components

- **`crew.py`:** Contains the implementation of the `ReadmeCrew` class, which integrates multiple agents responsible for exploring, analyzing, writing, and translating.
  
- **`main.py`:** The primary entry point that initializes the project and triggers the execution of the agents via the `kickoff` method.

- **`__init__.py`:** Designates the directory as a package, allowing Python to recognize it as such.

- **`config/agents.yaml`:** Configuration file that outlines the specific roles and objectives of the various agents deployed within the project.

- **`config/tasks.yaml`:** Defines the tasks to be executed by the agents along with their expected outcomes, ensuring clarity in the workflow.

- **`tools/custom_tool.py`:** Implements additional functionality that aids the agents in their roles by providing capabilities for reading files or directories.

- **`tools/__init__.py`:** Marks the tools directory as a package, allowing for structured imports and usage of the tools.

## Installation and Configuration

To set up the Project README Generator, you can use **Poetry** for dependency management. Here’s how to install and configure the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/project-readme-generator.git
   cd project-readme-generator
   ```

2. **Install Poetry (if not already installed):**
   Follow the instructions from the [official Poetry documentation](https://python-poetry.org/docs/#installation).

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Configuration:**
   - Modify the configuration files located in the `config` directory (`agents.yaml` and `tasks.yaml`) as needed to tailor the project to your specific requirements.

## Usage

To run the Project README Generator, use the following command:

```bash
poetry run python main.py /path/to/your/project
```

Replace `/path/to/your/project` with the actual path to the project you want to analyze and generate documentation for.

With this setup, you can efficiently generate a README file that not only outlines your project's purpose and structure but also adapts to your documentation needs quickly. Thank you for exploring the Project README Generator!
