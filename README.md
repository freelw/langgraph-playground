# langgraph-playground

## install

```
conda create --name langgraph python=3.11 -y
conda activate langgraph
pip install langchain-deepseek
pip install langgraph
pip install dotenv
pip install langsmith
pip install IPython
pip install -U langchain-tavily
```

## 例子说明
* [deepseek.py](deepseek.py) 是 [1-build-basic-chatbot](https://langchain-ai.github.io/langgraph/tutorials/get-started/1-build-basic-chatbot/) 的实现
* [tavily.py](tavily.py) 是 [2-add-tools](https://langchain-ai.github.io/langgraph/tutorials/get-started/2-add-tools/) 的实现
* [tavily_with_prebuilt.py](tavily_with_prebuilt.py) 是 [2-add-tools](https://langchain-ai.github.io/langgraph/tutorials/get-started/2-add-tools/) 的 prebuilt实现