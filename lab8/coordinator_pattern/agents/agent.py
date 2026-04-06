from google.adk.agents import SequentialAgent

from agents.order_agent import order_agent
from agents.inventory_agent import inventory_agent

# Orchestrate the Order Approval Workflow
root_agent = SequentialAgent(
    name="OrderApprovalWorkflowAgent",
    sub_agents=[order_agent, inventory_agent]
)
