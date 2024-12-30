#packages:
#1 langchain
#2 dotenv
#3 langchain_core
#4 langchain_google_genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

if __name__ =="__main__":
    prompt="Translate below sentance '{sentance}' into this language {language}"
    sentance=input("\n Type the sentance you want to translate and press enter :\n")
    lang=input("Enter the language you want to translate: \n")
    prompt_temp=PromptTemplate(input_variables=["sentance","language"],template=prompt)
    llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash')
    chain=prompt_temp | llm | StrOutputParser()
    response=chain.invoke({"sentance":sentance,"language":lang})
    print(response)


