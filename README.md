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
* [memory.py](memory.py) 是 [3-add-memory](https://langchain-ai.github.io/langgraph/tutorials/get-started/3-add-memory/) 的实现
* [human.py](human.py) 是 [4-human-in-the-loop](https://langchain-ai.github.io/langgraph/tutorials/get-started/4-human-in-the-loop/) 的实现
* [customize_state.py](customize_state.py) 是 [5-customize-state](https://langchain-ai.github.io/langgraph/tutorials/get-started/5-customize-state/) 的实现

## .env 配置说明

```
PYTHONPATH=/opt/anaconda3/envs/langgraph/lib/python3.11/site-packages
DEEPSEEK_API_KEY=<deepseek api key>
TAVILY_API_KEY=<tavily api key>
```
* PYTHONPATH conda环境包路径，用于vscode正确跳转，结合settings.json中的python.envFile
* DEEPSEEK_API_KEY 填写自己的 deepseek api key
* TAVILY_API_KEY 填写自己的 tavily api key