# Source https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88

#pip install openai
#pip install wget
#pip install pdfplumber

#import subprocess

#def install_dependencies():
#    dependencies = ['openai', 'wget', 'pdfplumber']
#    for dependency in dependencies:
#        subprocess.run(['pip', 'install', dependency])

#install_dependencies()
import openai
#import pdfplumber

#paperFilePath = "Test_2controls.pdf"
paperFilePath = "test2.pdf"
#paperContent = pdfplumber.open(paperFilePath).pages

#def displayPaperContent(paperContent, page_start=1, page_end=6):
#    for page in paperContent[page_start:page_end]:
#        print(page.extract_text())
#displayPaperContent(paperContent)

import pdfplumber

text= ""
# Open the PDF file
with pdfplumber.open(paperFilePath) as pdf:
    # Iterate through each page in the PDF
    for page in pdf.pages:
        # Extract the text from the page
        text =text + " " + page.extract_text()
        


def GPT_Completion(texts):
## Call the API key under your account (in a secure way)
  openai.api_key = "YOURKEY"
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.6,
    top_p = 1,
    max_tokens = 1000,
    frequency_penalty = 0,
    presence_penalty = 0
  )
  return print(response.choices[0].text)

query = 'With the following text, give me a list of NUMBER and TITLE. In the first example, NUMBER is 1.1 and TITLE is Ensure that Corporate Login Credentials are Used (Manual). In the second, NUMBER is 1.2 and TITLE is Ensure that Multi-Factor Authentication is Enabled for All Non-Service Accounts (Manual)  ' + text
GPT_Completion(query)