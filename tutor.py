import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Set API Key
os.environ["TOGETHER_API_KEY"] = "ff4b9f7386b2863ee05da857e4c23d08c6d867d819ff40f7319f2c5489962911"

# Initialize Mistral-7B Model
llm = ChatOpenAI(
    model_name="mistralai/Mistral-7B-Instruct-v0.1",
    openai_api_key=os.getenv("TOGETHER_API_KEY")
)

# ✅ Fix: Correctly import and initialize memory
memory = ConversationBufferMemory(return_messages=True)

# Define Prompt
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question in a detailed manner:\n{question}"
)

# Streamlit UI
st.title("🤖 AI-Powered Personal Tutor")
st.write("Ask me anything about coding, math, or science!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your Question:")

if user_input:
    response = llm.invoke(prompt.format(question=user_input))  # Invoke model directly
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Tutor", response))

# Display Chat History
for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")
