
import pandas as pd

from langchain_community.chat_models import ChatOllama

df = pd.read_csv('data/report_status.csv')

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
        """
        You are an expert in analyzing aircraft accident reports. You have been asked to categorize the following aircraft accident reason into one of the following categories: 'Pilot Error', 'Mechanical Failure', 'Weather Conditions', or 'Other'. Provide only the category name as a single word. Reason: {reason}
    
    Example : 
    Reason : Collapse of the landing gear due to worn left main landing gear components.
    
    Category : Mechanical Failure 
    
    Do not include any additional information or punctuation in your response. An only use the categries provided. ,
        """
        )
    ]
)

llm = ChatOllama(
            model="llama3",
            temperature=0,
        )

chain = prompt | llm


def get_llm_categorization(reason):
    x = chain.invoke(
    {
        "reason": reason,
        
    }
    )
    
    category = x.content.strip()
    return category


df['Category'] = df['Report Status'].apply(get_llm_categorization)


df.to_csv('categorized_accident_reasons_llm.csv', index=False)





