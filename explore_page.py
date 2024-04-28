import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

@st.cache_data
def load_data():
    data=pd.read_csv('salaries.csv')
    cols = ['salary','salary_currency','company_location','employee_residence']
    data.drop(cols,axis = 1,inplace = True) 

    job_map = shorten_categories(data['job_title'].value_counts(), 100)
    data['job_title'] = data['job_title'].map(job_map) 
    data=data[data['salary_in_usd'] <= 360000]
    data=data[data['salary_in_usd'] >= 10000 ]
    data=data[data['job_title'] != 'Other']     
    return data 

data = load_data()

def show_explore_page():
    st.title("Explore Data Science Jobs Salaries")

    st.write(
        """
    ### Stack Developer Survey
    """    
    )

    df = data['job_title'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(df, labels=df.index, autopct="%1.1f%%")
    ax1.axis("equal")

    st.write("""### Number of data from Different Job Titles""")

    st.pyplot(fig1)

    st.write(
        """
    ### Mean Salary Based on Jobs
    """    
    )

    df = data.groupby(["job_title"])["salary_in_usd"].mean().sort_values(ascending=True)
    st.bar_chart(df)
    

    st.write(
        """
    ### Mean Salary Based on Years
    """    
    )

    df = data.groupby(["work_year"])["salary_in_usd"].mean().sort_values(ascending=True)
    st.line_chart(df)
    
    

    