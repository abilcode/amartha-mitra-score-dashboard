import streamlit as st
import pandas as pd

def adjust_threshold(data=None):
    # Add widgets to the sidebar
    st.sidebar.write("Select calculation input:")
    option = st.sidebar.selectbox("Select an option", ["Exact Value", "Quantile"])
    if option == "Exact Value":
        # Initial dictionary with exact value
        threshold = {
            'max_dpd':7,
            'total_presence':0.5,
            'excess_repayment':9,
            'sum_tr':670000,
            'total_amount_ppob':220000,
            'max_amount_saving':0,
            'total_saving_frequency':22
        }
    else:
        # Initial dictionary with quantile calculation
        threshold = {
            'max_dpd':0.2,
            'total_presence': 0.8,
            'excess_repayment': 0.8,
            'sum_tr': 0.2,
            'total_amount_ppob': 0.8,
            'max_amount_saving': 0.8,
            'total_saving_frequency': 0.8,

        }
        threshold_quantile = {
            'max_dpd': data['max_dpd'].quantile(threshold['max_dpd']),
            'total_presence': data['total_presence'].astype('float').quantile(threshold['total_presence']),
            'excess_repayment': data['excess_repayment'].quantile(threshold['excess_repayment']),
            'sum_tr': data['sum_tr'].quantile(threshold['sum_tr']),
            'total_amount_ppob': data['total_amount_ppob'].quantile(threshold['total_amount_ppob']),
            'max_amount_saving': data['max_amount_saving'].quantile(threshold['max_amount_saving']),
            'total_saving_frequency': data['total_saving_frequency'].quantile(threshold['total_saving_frequency'])
        }

    # Create a form using st.form
    with st.form(key='threshold_form'):
        st.write('Threshold Configuration')
        if option:

            # Input fields for each key in the dictionary
            for key, value in threshold.items():
                st.write(f"Default value: {key} = {threshold[key]}")
                threshold[key] = float(st.text_input(f'Threshold for {key}', value=value, key=f"{key}_t", type='default'))
                try:
                    if option == "Quantile":
                        threshold_quantile[key] = threshold[key]
                except UnboundLocalError:
                    pass

            # Submit button to update the weights
            submitted = st.form_submit_button('Update Thresholds')

            return threshold


if __name__ == "__main__":
    t = adjust_threshold()
    st.write(t)

