
import openai
import pandas as pd


df = pd.read_csv('data/report_status.csv')

template = """
    You are an expert in analyzing aircraft accident reports. 
    You have been asked to categorize the following aircraft accident reason into one of the following categories: 
    
    'Pilot Error', 'Mechanical Failure', 'Weather Conditions', or 'Other'. Provide only the category name as a single word. Reason: {reason}
    
    Example : 
    Reason : Collapse of the landing gear due to worn left main landing gear components.
    
    Category : Mechanical Failure 
    
    Do not include any additional information or punctuation in your response. An only use the categries provided. 
    """

def get_llm_categorization(reason):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": template}
        ],
        max_tokens=5,
        temperature=0.0,
    )
    category = response['choices'][0]['message']['content'].strip()
    return category


df['Category'] = df['Report Status'].apply(get_llm_categorization)


df.to_csv('categorized_accident_reasons_llm.csv', index=False)





