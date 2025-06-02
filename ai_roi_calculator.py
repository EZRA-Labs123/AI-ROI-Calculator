
import streamlit as st

st.set_page_config(page_title="AI Training ROI Calculator", layout="centered")

st.title("🤖 AI Training ROI Calculator")
st.markdown("""
This tool helps estimate the return on investment (ROI) from increased productivity due to AI training.
Input your assumptions below to see the impact.
""")

# Input fields
salary = st.number_input("Annual Salary per Employee ($)", min_value=10000, max_value=500000, value=100000, step=1000)
hours_saved = st.number_input("Hours Saved per Week per Employee", min_value=0.0, max_value=40.0, value=2.0, step=0.5)
num_employees = st.number_input("Number of Employees Trained", min_value=1, max_value=10000, value=10, step=1)
program_cost = st.number_input("Total Program Cost ($)", min_value=0, max_value=1000000, value=10000, step=500)

# Calculations
cost_per_hour = salary / 2080
weekly_saving = hours_saved * cost_per_hour
yearly_saving_per_employee = weekly_saving * 52
total_saving = yearly_saving_per_employee * num_employees
roi_percent = ((total_saving - program_cost) / program_cost) * 100 if program_cost > 0 else 0
net_savings = total_saving - program_cost

# Output display
st.header("📊 Results")
st.metric("Cost per Hour", f"${cost_per_hour:,.2f}")
st.metric("Yearly Saving per Employee", f"${yearly_saving_per_employee:,.2f}")
st.metric("Total Group Saving", f"${total_saving:,.2f}")
st.metric("ROI", f"{roi_percent:.1f}%")
st.metric("Net Savings", f"${net_savings:,.2f}")

st.caption("*Based on 2080 work hours per year (40 hours/week x 52 weeks).*")
