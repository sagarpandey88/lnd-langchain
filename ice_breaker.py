import os
from langchain_core.prompts import PromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    print("hello langchain")
    print(os.environ["AZURE_OPENAI_ENDPOINT"])

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = AzureChatOpenAI(temperature=0, deployment_name="gpt-35-turbo")

    linkedIn_Profile = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True
    )

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedIn_Profile})

    print("=====================response starts here:-=====================")

    print(res)
