import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        df = pickle.load(file)
    return df 

df = load_model()

model_r = df['model']
le_expl = df['le_expl']
le_empt = df['le_empt']
le_jobtitle = df['le_jobtitle']
le_compz = df['le_compz']

def show_predict_page():
    st.title("SalarySavvy")

    st.write("""### We need information to predict salary""")

    job_title = {
        "Data Engineer",                     
        "Data Scientist",                    
        "Data Analyst",                      
        "Machine Learning Engineer",         
        "Applied Scientist",                
        "Research Scientist",                 
        "Analytics Engineer",                 
        "Data Architect",                     
        "Data Manager",                       
        "Research Engineer",                 
        "Business Intelligence Engineer",
        "Data Science Manager",
        "ML Engineer",
        "Machine Learning Scientist",
        "BI Developer",
        "Data Analytics Manager",
        "Data Specialist",
        "Decision Scientist",
        "Data Science Consultant",
        "Business Intelligence Analyst",
        "Head of Data",
        "Director of Data Science",
        "Computer Vision Engineer",
        "Research Analyst",
        "AI Engineer",
        "Machine Learning Infrastructure Engineer",
        "BI Analyst",
        "Data Science Lead",
        "AI Scientist",
        "Data Modeler"  
    }

    experience_level = {
        "EN",
        "MI",
        "SE",
        "EX",

    }
        
    

    employment_type={
        "CT",
        "FT",
        "PT",
        "FL",
    }

    company_size= {
        "L",
        "M",
        "S",
    }

    work_year={
        "2020",
        "2021",
        "2022",
        "2023",
    }



    job_title = st.selectbox("jobs", job_title)
    experience_level = st.selectbox("Experience Level", experience_level)
    employment_type = st.selectbox("Employment type", employment_type)
    company_size = st.selectbox("Company Size", company_size)
    work_year = st.selectbox("Work Year", work_year)
    remote_ratio=st.slider("Remote Ratio", 0, 100, 50)

    ok=st.button("Calculate Salary")
    if ok:
        p = np.array([[work_year, "experience_level", "employment_type", "job_title", remote_ratio, "company_size"]])
        p[:, 1] = le_expl.transform([experience_level])
        p[:, 2] = le_empt.transform([employment_type])
        p[:, 3] = le_jobtitle.transform([job_title])
        p[:, 5] = le_compz.transform([company_size])
        p=p.astype(float)

        salary = model_r.predict(p)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
        







