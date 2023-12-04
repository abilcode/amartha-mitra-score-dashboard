import streamlit as st
import pandas as pd
import numpy as np

from helper.mitra_score_script_old import calculate_mitra_score
from helper.visualization import visualize_bar_chart
from helper.weight_adjustment import adjust_weight
from helper.threshold_adjustment import  adjust_threshold

def main():
    # Set page title
    st.set_page_config(page_title="Streamlit Dashboard", layout="wide")

    # Sidebar
    st.sidebar.title("Settings")

    # Main content
    st.title("Mitra Score Dashboard")

    # File upload in the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        # Read uploaded file
        data = pd.read_csv(uploaded_file)

        # Use the wide layout for the main content
        col1, col2 = st.columns(2)

        # Column 1 in the wide layout
        with col1:
            st.subheader("Weight adjustments")
            weight = adjust_weight()

        # Column 2 in the wide layout
        with col2:
            st.subheader("Threshold adjustments")
            threshold = adjust_threshold(data = data)

        button_to_calculate = st.button("Calculate")
        if button_to_calculate:
            # Calculate mitra score:
            aggregate = calculate_mitra_score(data, weight = weight, threshold = threshold)

            # Display the Plotly chart using st.plotly_chart
            fig = visualize_bar_chart(aggregate,  x="mitra_score", y="label")
            st.plotly_chart(fig)


# Run the app
if __name__ == "__main__":
    main()

