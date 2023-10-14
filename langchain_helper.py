from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.agents import load_tools
from langchain.agents import initialize_agent 
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()

def city_foods(city,food_allergy):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=["city","food_allergy"],
        template= "I am in {city} what are the top 3 foods I should eat and what should I drink with that, and my base these recommendations on my food allergy that is {food_allergy}"
        
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="city_name")
    response = name_chain({'city': city, 'food_allergy':food_allergy})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia"], llm = llm )

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run("I need to buy new sunglasses for hiking in japan what do you recommend ")

    print(result)

if __name__ == "__main__":
    print(langchain_agent())
    #print(city_foods("Hiroshima","wheat"))

