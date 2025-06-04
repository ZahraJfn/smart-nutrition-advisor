import streamlit as st
import json
import pandas as pd

# Load JSON data
with open("full_meal_data.json", "r") as f:
    meals = json.load(f)
df = pd.DataFrame(meals)

# Select meal type
meal_type = st.selectbox("Select meal type:", ["breakfast", "lunch", "dinner"])
filtered = df[df["type"] == meal_type]

# Select goal
goal = st.radio("Select your goal:", ["Muscle gain", "Weight loss", "Maintenance"])

# Recommendation logic
def recommend_meals(df, goal):
    if goal == "Muscle gain":
        return df[df["protein"] >= 30]
    elif goal == "Weight loss":
        return df[(df["fat"] <= 10) & (df["carbs"] <= 30)]
    else:  # Maintenance
        return df[(df["protein"] >= 15) & (df["fat"] <= 15) & (df["carbs"] <= 40)]

# Apply model
recommended = recommend_meals(filtered, goal)

# Display results
st.subheader("Recommended Meals for Your Goal")
st.dataframe(recommended[["name", "protein", "fat", "carbs"]])
st.bar_chart(recommended.set_index("name")[["protein", "fat", "carbs"]])
