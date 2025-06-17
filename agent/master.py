from langchain_ollama.llms import OllamaLLM
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
# from langchain_community.tools import DuckDuckGoSearchRun

@tool
def echo_text(text: str) -> str:
    """Echo the input text."""
    return text

def wake_up():
    """Initialize the agent with the necessary tools and prompt template."""

    llm = OllamaLLM(model="gemma3:4b")

    tools = [echo_text]

    prompt_template = PromptTemplate.from_template("""Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}""")

    agent = create_react_agent(
        llm,
        tools,
        prompt_template
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,
        early_stopping_method="generate"
    )

    return agent_executor


