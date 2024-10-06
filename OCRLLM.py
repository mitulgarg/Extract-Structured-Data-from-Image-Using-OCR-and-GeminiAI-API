import pytesseract
from PIL import Image
import google.generativeai as genai
import re

img = Image.open('/Users/mitulgarg/Desktop/screenshot.png')
# Perform OCR
extracted_text = pytesseract.image_to_string(img)

cleaned_data = re.sub(r"[./\"|_\,;']", "", extracted_text)

print()
print(cleaned_data)
print()

OCRdata=cleaned_data

try:
    GOOGLE_API_KEY='YOUR-API-KEY'

except ImportError:
    import os
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)

dict={}
def recognize(name:str=None, 
              age:int=None, 
              dob:str=None, 
              father_name:str=None, 
              address:str=None,
              gender:str=None,
              parents_address:str=None,
              hospital_address:str=None):
    
    dict["name"]=name
    dict["age"]=age
    dict["dob"]=dob
    dict["father_name"]=father_name
    dict["gender"]=gender
    dict["address"]=address
    dict["parents_address"]=parents_address
    dict["hospital_address"]=hospital_address

    return dict

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              tools=[recognize])

chat = model.start_chat(enable_automatic_function_calling=True)
examplequery="Here is an Example prompt: Name Prajwal Hebbar Age 25 DOB 07-03-1999 Father Name Hebbar"
exampleanswer="Output: Name: 'Prajwal Hebbar' ; Age: 25 ; DOB: '07-03-1999'; Father Name: Hebbar ; Gender: Female ; Address of Parents: NGV,Koramanagala, Bengaluru ; Hospital Address : St. John's,Koramangala,Bengaluru"
query="Follow the Output format and please extract whatever is available from the following: name, age, date of birth, gender,address where the child was born and father's name in the format specified in the output example from this text : "
# OCRdata="Name RUTVU Sex Male Date of Birth 16/09/2015 Place Of Birth DIVKARS HOSPITAL Name of Mother GJAYASHREE Name Of Father MANIKANANDAN Address Of Parents at time of birth of child NO3,NGR LAYOUT, ROOPANA AGRAHARA, BANGALORE-560100 Permanent Address of parents NO3,NGR LAYOUT, ROOPANA AGRAHARA, BANGALORE-560100 Registration No. JAY/BYE0934 Date Of Registration 30/09/2015"

response = chat.send_message(query+OCRdata+examplequery+exampleanswer)

print()
print("Output: ")
LLM_answer=response.text

fields = LLM_answer.split(';')

# Print each field on a new line
for field in fields:
    if field.strip():  # This check ensures not to print empty lines
        print(field.strip())

#output is: Name: 'Mitul' ; Age: 16 ; DOB: '16-11-2002'; Father Name: Anurag ; Gender: Male


