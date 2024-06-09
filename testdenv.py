from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量获取 API 密钥
api_key = os.getenv('OPENAI_API_KEY')

# 使用 langchain-openai 包中的 OpenAI 类
from langchain_openai import OpenAI

# 初始化 OpenAI 对象
llm = OpenAI(api_key=api_key)

# 使用 invoke 方法进行预测
response = llm.invoke("Translate this text to Chinese: Hello, how are you?")

print(response)
