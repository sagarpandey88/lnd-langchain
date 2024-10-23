# System imports
import os

# Lang chain imports
from langchain_core.prompts import PromptTemplate
from langchain_openai import (
    AzureChatOpenAI,
)  # use ChatOpenAI if dont have Azure Open AI
from langchain_core.output_parsers import StrOutputParser

# custom imports
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from parsers.output_parser import summary_parser


def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(
        name=name
    )  # gets the url from tavily search / mock
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url
    )  # scrape the data using proxycurl / mock

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
     \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = AzureChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm | StrOutputParser() | summary_parser

    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":

    print("Ice Breaker Enter")
    ice_break_with(name="Eden Marco")
