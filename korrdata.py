from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number

# LangChain Models
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import OpenAI

# Standard Helpers
import pandas as pd
import requests
import time
import json
from datetime import datetime

# Text Helpers
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# For token counting
from langchain.callbacks import get_openai_callback

def printOutput(output):
    print(json.dumps(output,sort_keys=True, indent=3))

openai_api_key = 'SECRET KEY'


llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    max_tokens=2000,
    openai_api_key=openai_api_key
)


person_schema = Object(
    # This what will appear in your output. It's what the fields below will be nested under.
    # It should be the parent of the fields below. Usually it's singular (not plural)
    id="person",
    
    # Natural language description about your object
    description="Personal information about a person",
    
    # Fields you'd like to capture from a piece of text about your object.
    attributes=[
        Text(
            id="first_name",
            description="The first name of a person.",
        )
    ],
    
    # Examples help go a long way with telling the LLM what you need
    examples=[
        ("Alice and Bob are friends", [{"first_name": "Alice"}, {"first_name": "Bob"}])
    ]
)

chain = create_extraction_chain(llm, person_schema)

text = """
    My name is Bobby.
    My sister's name is Rachel.
    My brother's name Joe. My dog's name is Spot
"""
output = chain.predict_and_parse(text=(text))["data"]

printOutput(output)
# Notice how there isn't "spot" in the results list because it's the name of a dog, not a person.


