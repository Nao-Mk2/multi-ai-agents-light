from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun

llm = Ollama(model="gemma3:4b")

tools = [DuckDuckGoSearchRun()]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

result = agent.invoke("明日の天気は？")
print(result)
