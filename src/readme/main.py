#!/usr/bin/env python
import sys
from crew import ReadmeCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'directory_path': 'C:/path/to/your/project'
    }
    ReadmeCrew().crew().kickoff(inputs=inputs)

run()
