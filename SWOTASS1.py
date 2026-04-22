import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from  langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm= ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="nvidia/nemotron-3-super-120b-a12b:free",
    temperature=0.2,
)
st=StrOutputParser()
chain=llm|st
def perform():
    while True:
        s=str(input("Q: ").strip())
        if "quit" in s.lower() or "exit" in s.lower():
            break
        if s:
            try:
                res=chain.invoke(s)
                print(f"\n{res}\n")
            except Exception as e:
                print(f"Error: {e}")
                
if __name__=="__main__":
    perform()
                
    
    