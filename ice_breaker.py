import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import AzureOpenAI



if __name__ == '__main__':
    print("hello langchain")
    print(os.environ['AZURE_OPENAI_ENDPOINT'])

    subscription_key = os.environ["AZURE_OPENAI_API_KEY"]  
    BASE_URL =os.environ["AZURE_OPENAI_ENDPOINT"]  
 

    information = """
      Virat Kohli  is an Indian international cricketer who plays Test and ODI cricket for the Indian national team. A former captain in all formats of the game, Kohli retired from the T20I format following India's win at the 2024 T20 World Cup. He's a right-handed batsman and an occasional unorthodox right arm medium bowler. Kohli is regarded as one of the greatest batsmen of all time and the greatest in the modern era. He holds the highest IPL run-scorer record, ranks third in T20I, third in ODI, and stands the fourth-highest in international cricket.[4] He also holds the record for scoring the most centuries in ODI cricket and is second in the list of most international centuries scored.

Kohli was a key member of the Indian team that won the 2011 Cricket World Cup, 2013 Champions Trophy and 2024 T20 World Cup and captained India to win the ICC Test mace three consecutive times in 2017, 2018, and 2019.[5] He represents Royal Challengers Bengaluru in the Indian Premier League and Delhi in domestic cricket.

In 2013, Kohli was ranked number one in the ICC rankings for ODI batsmen. In 2015, he achieved the summit of T20I rankings.[6] In 2018, he was ranked top Test batsman, making him the only Indian cricketer to hold the number one spot in all three formats of the game. He is the first player to score 20,000 runs in a decade. In 2020, the International Cricket Council named him the male cricketer of the decade.[7]
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = AzureOpenAI(temperature=0, deployment_name="gpt-35-turbo")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print("=====================response starts here:-=====================")
    
    print(res)
   
