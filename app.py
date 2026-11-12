import os
import gradio as gr
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
  base_url="https://mlapi.run/e55afb4c-afa7-4b64-b80f-937f9000573e/v1",
  api_key=os.getenv("OPENAI_API_KEY"),
  model="helpy-pro",
)

role="너는 친절하고 도움을 주는 AI 비서야."

def function(message,history):
  memory=role="/n"
  for user,ai in history:
    if user and ai:
      memory+=("사용자:" + user +"/n")
      memory +=("AI:" + ai + "/n")
  memory +=("사용자:" + message +"/n")
  response=llm.invoke(memory)
  return response.content
demo=gr.ChatInterface(
  fn=function,
  title="제목없음",
  theme=gr.themes.Soft(),
  description="설명없음",
)
demo.launch(share=True)
