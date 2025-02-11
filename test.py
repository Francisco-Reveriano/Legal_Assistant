from openai import OpenAI
import streamlit as st
import os
import time
from dotenv import load_dotenv
from src.prompts import *

# Load environment variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Conversations
conversations = [{'role': 'user', 'content': 'Are customer identification procedures aligned with 31 U.S.C. 5318(l)?'}]
initial_message = [{"role": "user", "content": instruction_prompt}]
combined_conversations = initial_message + conversations

# Create a new thread with the conversation messages.
thread = client.beta.threads.create(messages=combined_conversations)