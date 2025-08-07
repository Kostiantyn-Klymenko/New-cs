import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

my_b_date = date(2006, 7, 13)
min_date = date(1900, 1, 1)
max_date = date.today()

with st.form(key="age_calculator", clear_on_submit=True):
    st.title("Age Calculator")
    st.write("Calculate your age based on your birth date.")
    
    birth_date = st.date_input("Select your birth date", min_value=min_date, max_value=max_date)
    
    submit_button = st.form_submit_button(label="Calculate Age")
    
    if submit_button:
        if birth_date == date.today():
            st.warning("You didn't change the default birth date.")
        else:
           st.write(f"Your birthday is {birth_date}")
           age = max_date.year - birth_date.year
           st.write(f"You are {age} years old.")
           my_age = max_date.year - my_b_date.year
           st.subheader("Your age compared to me")
           age_data = pd.DataFrame({"Age": [age, my_age]}, index=["You", "Me"])
           st.bar_chart(age_data)
        