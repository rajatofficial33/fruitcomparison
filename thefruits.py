import streamlit as st
# --- Nutritional data ---
nutritional_data = {
...     "apple": {"minerals": {"Calcium": 6, "Potassium": 107, "Magnesium": 5}},
...     "banana": {"minerals": {"Potassium": 358, "Magnesium": 27, "Manganese": 0.27}},
...     "orange": {"minerals": {"Calcium": 40, "Potassium": 181, "Phosphorus": 14}},
...     "mango": {"minerals": {"Potassium": 168, "Magnesium": 10, "Copper": 0.11}},
...     "grapes": {"minerals": {"Copper": 0.13, "Potassium": 191, "Manganese": 0.07}},
... }
... 
... def compare_minerals(fruit1, fruit2):
...     minerals1 = nutritional_data[fruit1]["minerals"]
...     minerals2 = nutritional_data[fruit2]["minerals"]
... 
...     all_minerals = set(minerals1.keys()).union(set(minerals2.keys()))
...     comparison = {}
...     for mineral in all_minerals:
...         val1 = minerals1.get(mineral, 0)
...         val2 = minerals2.get(mineral, 0)
...         if val1 > val2:
...             better = fruit1
...         elif val2 > val1:
...             better = fruit2
...         else:
...             better = "Equal"
...         comparison[mineral] = {fruit1: val1, fruit2: val2, "higher": better}
...     return comparison
... 
... # --- Streamlit UI ---
... st.title("🍎🥦 Fruit & Vegetable Mineral Comparison App")
... 
... fruit1 = st.selectbox("Choose first fruit/vegetable:", list(nutritional_data.keys()))
... fruit2 = st.selectbox("Choose second fruit/vegetable:", list(nutritional_data.keys()))
... 
... if st.button("Compare"):
...     result = compare_minerals(fruit1, fruit2)
...     st.write("### Mineral Comparison")
...     st.table(result)
