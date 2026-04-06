from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams, McpToolset
from google.genai import types

load_dotenv()
tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://localhost:5001/mcp",
    )
)

inventory_agent = LlmAgent(
    name="InventoryServiceAgent",
    model="gemini-2.5-flash-lite",
    description="Agent that manage product inventories. ",
    instruction="You are an inventory management expert specializing in filling the inventory by adding products,"
                " checking product inventories, updating the available quantity or inventory level of products. "
                "Use the correct tools to perform your tasks.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,  # More deterministic output
        max_output_tokens=1000,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            )
        ],
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(
                initial_delay=1.0,
                attempts=10,
                http_status_codes=[408, 429, 500, 502, 503, 504],
            ),
            timeout=120 * 1000,
        )
    ),
    tools=[tools],
)