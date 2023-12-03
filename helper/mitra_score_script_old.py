import pandas as pd
import numpy as np

def calculate_mitra_score(data, threshold = None, weight = None):
    """
       Calculate Mitra Score for the given data based on specified thresholds and weights.

       Parameters:
       - data (DataFrame): Input data containing various features.
       - threshold (dict, optional): Dictionary specifying feature-specific threshold values.
         If not provided, default quantile-based thresholds will be calculated from the input data.
       - weight (dict, optional): Dictionary specifying feature-specific weights.
         If not provided, default weights of 1 for each feature will be used.

       Returns:
       - aggregate (DataFrame): Aggregated Mitra Scores with corresponding label mean.
       """
    df_ready = data

    # threshold = {
    #     'max_dpd':7,
    #     'total_presence':0.5,
    #     'excess_repayment':9,
    #     'sum_tr':670000,
    #     'total_amount_ppob':220000,
    #     'max_amount_saving':0,
    #     'total_saving_frequency':22
    # }
    # Default Threshold
    if threshold is None:
        threshold = {
            'max_dpd':df_ready['max_dpd'].quantile(0.2),
            'total_presence':df_ready['total_presence'].astype('float').quantile(0.8),
            'excess_repayment':df_ready['excess_repayment'].quantile(0.8),
            'sum_tr':df_ready['sum_tr'].quantile(0.2),
            'total_amount_ppob':df_ready['total_amount_ppob'].quantile(0.8),
            'max_amount_saving':df_ready['max_amount_saving'].quantile(0.8),
            'total_saving_frequency':df_ready['total_saving_frequency'].quantile(0.8)
        }
    if weight is None:
        # Default Weight
        weight = {
            'max_dpd':1,
            'total_presence':1,
            'excess_repayment':1,
            'sum_tr':1,
            'total_amount_ppob':1,
            'max_amount_saving':1,
            'total_saving_frequency':1
        }

    df_ready['max_amount_saving'] = df_ready['max_amount_saving'].fillna(0)
    df_ready['total_saving_frequency'] = df_ready['total_saving_frequency'].fillna(0)

    df_score = df_ready.copy()
    # Calculate scores for each feature based on thresholds and weights
    for c in weight.keys():
      df_score[f"score_{c}"] = df_score[c].apply(lambda x: 0 if x > threshold[c] else 1 * weight[c])

    # Calculate the overall Mitra Score for each row (weighted sum)
    df_score['mitra_score'] = df_score.apply(
        lambda x: ((x.score_max_dpd + x.score_total_presence + x.score_excess_repayment +
                    x.score_sum_tr + x.score_total_amount_ppob + x.score_max_amount_saving +
                    x.score_total_saving_frequency)/7)*10,axis=1
                    )

    aggregate = df_score.groupby('mitra_score').agg({'label':'mean'}).reset_index()
    aggregate['label'] = aggregate['label'].round(2)


    return aggregate


if __name__ == "__main__":
    data = pd.read_csv("/Users/abilfad/Downloads/mitra_score_preprocessed.csv")
    aggregate = calculate_mitra_score(data)

    print(aggregate)

