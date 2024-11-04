import streamlit as stx
import pandas as pdx
import numpy as npx
import matplotlib.pyplot as pltx
import json
from datetime import datetime

emission_factors_x = {
    "Tamil Nadu": {
        "Transportation": {"Car": 0.14, "Bus": 0.1, "Bike": 0.05},
        "Electricity": 0.6,  
        "Diet": {"Omnivore": 1.25, "Vegetarian": 0.8, "Vegan": 0.5},
        "Waste": 0.6  
    },
    "Delhi": {
        "Transportation": {"Car": 0.25, "Bus": 0.2, "Bike": 0.1},
        "Electricity": 0.82, 
        "Diet": {"Omnivore": 1.8, "Vegetarian": 1.0, "Vegan": 0.6},
        "Waste": 1.0  
    },
    "Mumbai": {
        "Transportation": {"Car": 0.22, "Bus": 0.18, "Bike": 0.09},
        "Electricity": 0.75, 
        "Diet": {"Omnivore": 1.7, "Vegetarian": 1.1, "Vegan": 0.6},
        "Waste": 0.8  
    },
    "Puducherry": {
        "Transportation": {"Car": 0.15, "Bus": 0.12, "Bike": 0.07},
        "Electricity": 0.8,  
        "Diet": {"Omnivore": 1.2, "Vegetarian": 0.8, "Vegan": 0.5},
        "Waste": 0.5  
    }
}

user_data = []

stx.set_page_config(layout="wide", page_title="The ")
stx.title("S.A.F.E: Sustainability Assessment Framework for the Environment")
stx.subheader("By Sai Bharath and Suriyaa")


if 'username' not in stx.session_state:
    stx.subheader("Create an Account")
    username = stx.text_input("Username")
    password = stx.text_input("Password", type='password')

    if stx.button("Create Account"):
        stx.session_state.username = username
        stx.success("Account created Successfully, You Are All Set!")

if 'username' in stx.session_state:
    stx.subheader(f"Welcome back, {stx.session_state.username}!")

    # User inputs
    stx.subheader("Select Your State")
    states = stx.selectbox("Select your State", list(emission_factors_x.keys()))

    col1, col2 = stx.columns(2)

    with col1:
        stx.subheader("Daily Travelling distance (in km)")
        transport_mode = stx.selectbox("Choose your mode of transport", list(emission_factors_x[states]["Transportation"].keys()))
        distance = stx.slider("Distance", 0.0, 100.0, key="distance_input")

        stx.subheader("Monthly electricity consumption (in kWh)")
        electricity = stx.slider("Electricity", 0.0, 1000.0, key="electricity_input")

    with col2:
        stx.subheader("Waste generated per week (in kg)")
        waste = stx.slider("Waste", 0.0, 100.0, key="waste_input")

        stx.subheader("Number of meals per day")
        diet_type = stx.selectbox("Choose your diet", list(emission_factors_x[states]["Diet"].keys()))
        meals = stx.number_input("Meals", 0, key="meals_input")

    
    distance = distance * 365 if distance > 0 else 0  
    electricity = electricity * 12 if electricity > 0 else 0  
    meals = meals * 365 if meals > 0 else 0  
    waste = waste * 52 if waste > 0 else 0  

    
    transportation_emissions = emission_factors_x[states]["Transportation"][transport_mode] * distance
    electricity_emissions = emission_factors_x[states]["Electricity"] * electricity
    diet_emissions = emission_factors_x[states]["Diet"][diet_type] * meals
    waste_emissions = emission_factors_x[states]["Waste"] * waste

    
    transportation_emissions = round(transportation_emissions / 1000, 2)
    electricity_emissions = round(electricity_emissions / 1000, 2)
    diet_emissions = round(diet_emissions / 1000, 2)
    waste_emissions = round(waste_emissions / 1000, 2)

    
    total_emissions = round(
        transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
    )

    if stx.button("Calculate"):
        stx.header("Results")

        col3, col4 = stx.columns(2)

        with col3:
            stx.subheader("Carbon Emissions by Category")
            stx.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
            stx.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
            stx.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
            stx.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

        with col4:
            stx.subheader("Total Carbon Footprint")
            stx.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
            stx.warning(f"In {states}, estimated CO₂ emissions per capita vary with major contributors being industrial (Tamil Nadu, Mumbai) and urban transport (Delhi) sectors; Pondicherry has a lower footprint driven by residential consumption [[❞]](https://www.statista.com/topics/8881/emissions-in-india/) [[❞]](https://www.ceew.in/publications/state-and-sector-wise-greenhouse-gases-and-carbon-emissions-india).")

        
        average_emissions = {
            "Tamil Nadu": 1.8,  
            "Delhi": 2.5,       
            "Mumbai": 2.2,     
            "Puducherry": 1.2 
        }
        
        stx.subheader("Comparison with National Averages")
        stx.write(f"Your emissions: {total_emissions} tonnes CO2/year")
        stx.write(f"Average emissions for {states}: {average_emissions[states]} tonnes CO2/year")
        if total_emissions > average_emissions[states]:
            stx.warning("You are above the average carbon footprint for your states.")
        else:
            stx.success("You are below the average carbon footprint for your states.")

        
        historical_data = {
            "Year": [2010, 2015, 2020, 2021],
            "Tamil Nadu": [1.2, 1.5, 1.7, 1.8],
            "Delhi": [2.0, 2.3, 2.4, 2.5],
            "Mumbai": [1.9, 2.1, 2.1, 2.2],
            "Puducherry": [0.9, 1.1, 1.1, 1.2]
        }
        df = pdx.DataFrame(historical_data)

        stx.subheader("Historical CO2 Emissions per Capita")
        fig, ax = pltx.subplots()
        for country_name in df.columns[1:]:
            ax.plot(df["Year"], df[country_name], marker='o', label=country_name)

        ax.set_title("CO2 Emissions per Capita Over Years")
        ax.set_xlabel("Year")
        ax.set_ylabel("Emissions (tonnes CO2)")
        ax.legend()
        stx.pyplot(fig)

        
        stx.subheader("Recommendations to Reduce Your Carbon Footprint")
        recommendations = [
            "1. Use public transport or cycle for short distances.",
            "2. Switch to renewable energy sources for electricity.",
            "3. Reduce meat consumption and opt for a plant-based diet.",
            "4. Minimize waste by recycling and composting.",
            "5. Consider carbon offsetting projects."
        ]
        for rec in recommendations:
            stx.write(rec)

        
        stx.subheader("Carbon Offset Options")
        stx.write("You can invest in the following types of projects to offset your carbon emissions:")
        offset_projects = {
            "Reforestation": "Plant trees to absorb CO2.",
            "Renewable Energy": "Support wind or solar energy projects.",
            "Energy Efficiency": "Invest in projects that improve energy use.",
        }
        for project, description in offset_projects.items():
            stx.write(f"- **{project}**: {description}")

        # Save user data
        user_profile = {
            "Username": stx.session_state.username,
            "State": states,
            "Transport Mode": transport_mode,
            "Distance": distance,
            "Electricity": electricity,
            "Waste": waste,
            "Diet": diet_type,
            "Meals": meals,
            "Total Emissions": total_emissions,
            "Date": datetime.now().strftime("%Y-%m-%d")
        }
        user_data.append(user_profile)

        stx.session_state.user_data = json.dumps(user_data)  

        
        stx.subheader("Educational Resources")
        stx.write("Learn more about carbon emissions and how to reduce them:")
        stx.markdown("[The Basics of Climate Change](https://www.ipcc.ch/report/ar6/wg1/)")
        stx.markdown("[Carbon Footprint Calculator Guide](https://www.epa.gov/ghgemissions/calculating-carbon-footprint)")

        
        stx.subheader("Carbon Footprint Goals!!!")
        goal = stx.number_input("Set a goal for your carbon footprint (tonnes CO2/year)", value=total_emissions, step=0.1)
        if stx.button("Set Goal"):
            stx.session_state.goal = goal
            stx.success(f"Goal set to {goal} tonnes CO2/year! Keep tracking your emissions to meet your goal.")

        
        if 'goal' in stx.session_state:
            if total_emissions > stx.session_state.goal:
                stx.warning("You are above your carbon footprint goal. Consider ways to reduce your emissions.")
            else:
                stx.success("Congratulations! You are meeting your carbon footprint goal.")

else:
    stx.warning("Please create an account to use the app.")
