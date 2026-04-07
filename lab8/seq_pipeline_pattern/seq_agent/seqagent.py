from google.adk.agents import SequentialAgent

from seq_agent.seq_exe_agent import agent2
from seq_agent.text_to_sql_agent import agent1

# Orchestrate the Pipeline
seq_agent = SequentialAgent(
    name="BiqQueryPipelineAgent",
    sub_agents=[agent1, agent2]
)

root_agent = seq_agent