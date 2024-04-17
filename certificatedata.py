import os
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain

os.environ['OPENAI_API_KEY'] = 'SECRET KEY'


schema = {
    "properties":{
        "name":{"type":"string"},
        "age":{"type":"int"},
        "DOB":{"type":"string"},
        "father_name":{"type":"string"},
    },
    "required":["name","age","DOB"],
}

OCRdata=""" Name Bob Age 10 Height 5.5ft Date Of Birth 10-1-2001 Father Name Chris """

llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
chain= create_extraction_chain(schema,llm)
chain.run(OCRdata)
