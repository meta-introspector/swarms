import os
from swarms import Agent, OpenAIChat
from dotenv import load_dotenv
load_dotenv()
import logging
import contextlib
from http.client import HTTPConnection
from dotenv import load_dotenv
from swarm_models import OpenAIChat
from swarms import Agent
from swarms.prompts.finance_agent_sys_prompt import (
    FINANCIAL_AGENT_SYS_PROMPT,
)

HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

for x in (
        "httpcore",
        "requests.packages.urllib3"):
    alog = logging.getLogger(x)
    alog.setLevel(logging.DEBUG)
    alog.propagate = True


load_dotenv()

# Get the OpenAI API key from the environment variable
#api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAIChat class
model = OpenAIChat(
    openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0.1
)
#    llm=OpenAIChat(        model_name = "petals-sauerkraut",    ),

# Initialize the agent
agent = Agent(
    agent_name="Financial-Analysis-Agent",
    system_prompt=FINANCIAL_AGENT_SYS_PROMPT,
    llm=model,
    max_loops="auto",
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="finance_agent.json",
    user_name="swarms_corp",
    retry_attempts=1,
    streaming_on=True,
    context_length=200000,
    return_step_meta=True,
    output_type="json",  # "json", "dict", "csv" OR "string" soon "yaml" and
    auto_generate_prompt=False,  # Auto generate prompt for the agent based on name, description, and system prompt, task
    artifacts_on=True,
    artifacts_output_path="roth_ira_report",
    artifacts_file_extension=".txt",
    max_tokens=8000,
    return_history=True,

#    stopping_token="<DONE>",
#    interactive=True,
#    state_save_file_type="json",
#    saved_state_path="transcript_generator.json",


)

agent.run(
    "How can I establish a ROTH IRA to buy stocks and get a tax break? What are the criteria. Create a report on this question.",
    all_cores=True,
)
