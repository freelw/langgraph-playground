import json
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_deepseek import ChatDeepSeek
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
from dotenv import load_dotenv
load_dotenv()

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "1"}}

try:
    # 假设 graph.get_graph().draw_mermaid_png() 返回 PNG 字节流
    img_data = graph.get_graph().draw_mermaid_png()
    
    # 将字节流写入文件
    with open("graph.png", "wb") as f:
        f.write(img_data)
except Exception:
    # This requires some extra dependencies and is optional
    print ("Graph visualization is not available in this environment.")

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}, config=config, stream_mode="values"):
        event["messages"][-1].pretty_print()

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break