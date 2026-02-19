import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

#Load environment variables from .env file
load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=1024
)

def generate_sales_summary(data_dict):
    #Generates an executive summary based on aggregated sales data
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are SeShat AI, an expert business analyst. Provide an executive sales summary, analyze trends, and highlight growth opportunities based on the provided data context. Do not output raw data, just business insights."),
        ("human", "Here is the sales data context:\n{context}\n\nPlease provide the executive summary.")
    ])
    chain = prompt | llm
    response = chain.invoke({"context": str(data_dict)})
    return response.content

def analyze_underperformance(data_dict):
    #Explains why products might be underperforming and suggests actions
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are SeShat AI. Analyze the given list of underperforming products. Explain possible business reasons for their low sales and suggest actionable steps to improve performance."),
        ("human", "Underperforming products data:\n{context}\n\nProvide your analysis.")
    ])
    chain = prompt | llm
    response = chain.invoke({"context": str(data_dict)})
    return response.content

def answer_business_query(question, data_context):
    #Answers a specific natural language query based on the data context
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are SeShat AI, a data-driven business advisor. Answer the user's question accurately based ONLY on the provided context. Keep it business-friendly. If the answer is not in the context, state that you cannot determine it."),
        ("human", "Context:\n{context}\n\nQuestion: {question}\n\nAnswer:")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "context": str(data_context),
        "question": question
    })
    return response.content

def generate_recommendations(data_dict):
    #Generates strategic business recommendations
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are SeShat AI. Based on the provided performance metrics, suggest products to promote, categories needing focus, cities with growth opportunity, and payment mode optimization insights."),
        ("human", "Business metrics:\n{context}\n\nProvide your recommendations.")
    ])
    chain = prompt | llm
    response = chain.invoke({"context": str(data_dict)})
    return response.content