import streamlit as st
from datetime import date
import pandas as pd
from modules import database
from modules import llm_engine

#Set page configuration
st.set_page_config(page_title="SeShat AI Sales Intelligence", layout="wide")

#Main title
st.title("SeShat AI Sales Intelligence System")

#Create tabs for different features
tab1, tab2, tab3, tab4 = st.tabs([
    "Sales Summary", 
    "Low Performance Detection", 
    "Smart Business Query", 
    "Recommendations"
])

#Tab1:Sales Summary Generator
with tab1:
    st.header("AI Sales Summary Generator")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", date(2026, 1, 1))
    with col2:
        end_date = st.date_input("End Date", date(2026, 2, 15))
        
    if st.button("Generate Summary"):
        with st.spinner("Fetching data and analyzing..."):
            #Fetch aggregated data from SQLite
            data_context = database.get_sales_summary(start_date, end_date)
            
            #Pass context to LLM
            ai_summary = llm_engine.generate_sales_summary(data_context)
            
            st.subheader("Executive AI Summary")
            st.write(ai_summary)
            
            #Display raw data context for transparency
            with st.expander("View Aggregated Data Context"):
                st.json(data_context)

#Tab2:Low Performance Detection
with tab2:
    st.header("AI Low Performance Detection")
    if st.button("Analyze Underperforming Products"):
        with st.spinner("Identifying and analyzing low performers..."):
            #Fetch low performance data
            underperforming_data = database.get_underperforming_products()
            
            #Pass to LLM for reasoning
            ai_analysis = llm_engine.analyze_underperformance(underperforming_data)
            
            st.subheader("Performance Analysis")
            st.write(ai_analysis)
            
            with st.expander("View Product Data"):
                st.dataframe(pd.DataFrame(underperforming_data))

#Tab3:Smart Business Query
with tab3:
    st.header("AI Smart Business Query")
    user_query = st.text_input("Ask a business question in natural language:")
    
    if st.button("Ask SeShat AI"):
        if user_query:
            with st.spinner("Thinking..."):
                #Fetch generalized context to help answer the query
                general_context = database.get_recommendation_data()
                answer = llm_engine.answer_business_query(user_query, general_context)
                
                st.subheader("Answer")
                st.write(answer)
        else:
            st.warning("Please enter a question first.")

#Tab4:Recommendations
with tab4:
    st.header("AI Sales Recommendation Engine")
    if st.button("Get Recommendations"):
        with st.spinner("Generating strategic insights..."):
            #Fetch metrics for recommendations
            rec_data = database.get_recommendation_data()
            
            #Pass to LLM
            ai_recommendations = llm_engine.generate_recommendations(rec_data)
            
            st.subheader("Strategic Recommendations")
            st.write(ai_recommendations)