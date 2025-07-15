from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

import getpass
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv()
from langchain_tavily import TavilySearch

tool = TavilySearch(max_results=2)
tools = [tool]
res = tool.invoke("What's a 'node' in LangGraph?")
print(res)