import textwrap
import google.generativeai as genai
from IPython import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


try:
    GOOGLE_API_KEY='SECRET API KEY'

except ImportError:
    import os
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)

dict={}
def recognize(name:str, age:int, dob:str, father_name:str):
    dict["name"]=name
    dict["age"]=age
    dict["dob"]=dob
    dict["father_name"]=father_name
    return name,age,dob,father_name



model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              tools=[recognize])

chat = model.start_chat(enable_automatic_function_calling=True)
examplequery="Here is an Example prompt: Name Prajwal Hebbar Age 25 DOB 07-03-1999 Father Name Hebbar"
exampleanswer="Output: Name: 'Prajwal Hebbar' ; Age: 25 ; DOB: '07-03-1999'; Father Name: Hebbar"
query="Please extract the name, age, date of birth, and father's name from this text: "
OCRdata="Name @ Mitul Age 16 DOB 16-11-2002 Father Name Anurag"

response = chat.send_message(query+OCRdata+examplequery+exampleanswer)



# Example usage
input_string = "Name Mitul Age 16 DOB 16-11-2002 Father Name Anurag"

print(response.text)



