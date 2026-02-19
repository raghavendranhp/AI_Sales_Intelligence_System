import sqlite3
import pandas as pd
import os


DB_PATH = os.path.join("data", "sales_data.db")

def get_connection():
    #Return a new database connection
    return sqlite3.connect(DB_PATH)

def get_sales_summary(start_date, end_date):
    #Fetch aggregated sales data for a specific date range
    conn = get_connection()
    
    #Total revenue and units
    totals_query = f"""
    SELECT 
        SUM(net_amount) as total_revenue,
        SUM(quantity_sold) as total_units_sold
    FROM sales
    WHERE sale_date BETWEEN '{start_date}' AND '{end_date}'
    """
    totals = pd.read_sql(totals_query, conn)
    
    #Top categories
    cat_query = f"""
    SELECT category, SUM(net_amount) as revenue 
    FROM sales 
    WHERE sale_date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY category ORDER BY revenue DESC LIMIT 5
    """
    categories = pd.read_sql(cat_query, conn)
    
    #Best selling products
    prod_query = f"""
    SELECT product_name, SUM(quantity_sold) as units_sold, SUM(net_amount) as revenue
    FROM sales
    WHERE sale_date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY product_name ORDER BY units_sold DESC LIMIT 5
    """
    products = pd.read_sql(prod_query, conn)
    
    #City-wise performance
    city_query = f"""
    SELECT city, SUM(net_amount) as revenue
    FROM sales
    WHERE sale_date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY city ORDER BY revenue DESC
    """
    cities = pd.read_sql(city_query, conn)
    
    conn.close()
    
    return {
        "totals": totals.to_dict(orient='records')[0],
        "top_categories": categories.to_dict(orient='records'),
        "best_products": products.to_dict(orient='records'),
        "city_performance": cities.to_dict(orient='records')
    }

def get_underperforming_products():
    #Identify products with low sales volume and revenue
    conn = get_connection()
    query = """
    SELECT product_name, category, brand, SUM(quantity_sold) as total_quantity, SUM(net_amount) as total_revenue
    FROM sales
    GROUP BY product_name
    ORDER BY total_revenue ASC, total_quantity ASC
    LIMIT 10
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient='records')

def get_recommendation_data():
    #Fetch data needed for generating business recommendations
    conn = get_connection()
    
    #Category performance for focus
    cat_query = "SELECT category, SUM(net_amount) as revenue FROM sales GROUP BY category ORDER BY revenue ASC"
    categories = pd.read_sql(cat_query, conn)
    
    #City growth opportunity
    city_query = "SELECT city, SUM(net_amount) as revenue FROM sales GROUP BY city ORDER BY revenue ASC"
    cities = pd.read_sql(city_query, conn)
    
    #Payment modes usage
    payment_query = "SELECT payment_mode, COUNT(*) as transaction_count, SUM(net_amount) as revenue FROM sales GROUP BY payment_mode"
    payments = pd.read_sql(payment_query, conn)
    
    conn.close()
    return {
        "underperforming_categories": categories.to_dict(orient='records'),
        "city_opportunities": cities.to_dict(orient='records'),
        "payments": payments.to_dict(orient='records')
    }

def get_all_data_for_query():
    #Fetch sample data and schema context for the natural language LLM queries
    conn = get_connection()
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)
    conn.close()
    return df