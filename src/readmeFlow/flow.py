from crewai.flow.flow import Flow, listen, start, or_, and_
# from litellm import completion
from dotenv import load_dotenv
import os
import asyncio
from crew import ReadmeCrew
from crew2 import ReadmeCrew2
import agentops
from agentops.enums import EndState

load_dotenv()

class ReadmeFlow(Flow):
    # model = "gpt-4o-mini",
    @start()
    def start_flow(self):
        print("Starting flow")
        inputs = {
            'directory_path': 'C:/Users/Luciano/PycharmProjects/crewai_readme/readme/src/readmeFlow'
        }
        result = ReadmeCrew().crew().kickoff(inputs=inputs)
        print(f"Folder successfully explored: {result}")
        return result

    @listen(start_flow)
    def listen_flow(self, result):
        print("Writing README")
        inputs = {
            'readme': result  # Cambiado de result a result.result
        }   
        readme = ReadmeCrew2().crew().kickoff(inputs=inputs)
        print(f"File successfully written")
        return readme
    
def run_flow():
    agentops.init(api_key=os.getenv('AGENTOPS_API_KEY'), auto_start_session=False)
    session = agentops.start_session()
    flow = ReadmeFlow()
    flow.kickoff()
    
    session.end_session(EndState.SUCCESS.value)

async def run_flow():
    flow = ReadmeFlow()
    return await flow.kickoff_async()  # Cambiado de kickoff() a kickoff_async()

if __name__ == "__main__":
    asyncio.run(run_flow())
