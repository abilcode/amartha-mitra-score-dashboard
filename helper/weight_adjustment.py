import streamlit as st

def adjust_weight():

    # Initial dictionary
    weight = {
        'max_dpd': 1,
        'total_presence': 1,
        'excess_repayment': 1,
        'sum_tr': 1,
        'total_amount_ppob': 1,
        'max_amount_saving': 1,
        'total_saving_frequency': 1
    }

    # Create a form using st.form
    with st.form(key='weight_form'):
        st.write('Weight Configuration')

        # Input fields for each key in the dictionary
        for key, value in weight.items():
            weight[key] = float(st.text_input(f'Weight for {key}', value=value, key=key, type='default'))
            st.write(f"Value: {key} = {weight[key]}")

        # Submit button to update the weights
        submitted = st.form_submit_button('Update Weights')

        return weight


if __name__ == "__main__":
    w = adjust_weight()
    st.write(w)

