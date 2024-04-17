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
def recognize(name:str, age:int, dob:str, father_name:str, gender:str):
    dict["name"]=name
    dict["age"]=age
    dict["dob"]=dob
    dict["father_name"]=father_name
    dict["gender"]=gender

    return dict



model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              tools=[recognize])

chat = model.start_chat(enable_automatic_function_calling=True)
examplequery="Here is an Example prompt: Name Prajwal Hebbar Age 25 DOB 07-03-1999 Father Name Hebbar"
exampleanswer="Output: Name: 'Prajwal Hebbar' ; Age: 25 ; DOB: '07-03-1999'; Father Name: Hebbar ; GenderFemale"
query="Please extract the name, age, date of birth, gender and father's name from this text: "
# OCRdata="Name @ Mitul DOB 16-11-2002 Age **16 Father NameAnurag GenderMale"
"""Name RUTVU Sex Male Date of Birth 16/09/2015 Place Of Birth DIVKARS HOSPITAL Name of Mother GJAYASHREE Name Of Father 
MANIKANANDAN Address Of Parents at time of birth of child NO3,NGR LAYOUT, ROOPANA AGRAHARA, BANGALORE-560100 Permanent Address of parents NO3,
NGR LAYOUT, ROOPANA AGRAHARA, BANGALORE-560100 Registration No. JAY/BYE0934 Date Of Registration 30/09/2015"""

OCRdata=str(input("Enter The OCR data: "))

response = chat.send_message(query+OCRdata+examplequery+exampleanswer)


print()
print("Output: ")
print(response.text)

#output is: Name: 'Mitul' ; Age: 16 ; DOB: '16-11-2002'; Father Name: Anurag ; Gender: Male
