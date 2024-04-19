import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os

def transform_data():
    # Assuming 'data/loan_data.csv' is relative to the AIRFLOW_HOME directory
    # Modify this path as necessary based on your Airflow setup
    base_path = os.environ.get('AIRFLOW_HOME', '')
    data_file_path = os.path.join(base_path, 'dags/data', 'loan_data.csv')
    output_file_path = os.path.join(base_path, 'dags/data', 'transformed_loan_data.csv')

    data = pd.read_csv(data_file_path)
    print(data[:2])

    # One-Hot Encode the 'purpose' column
    encoder = OneHotEncoder(sparse_output=False)
    purpose_encoded = encoder.fit_transform(data[['purpose']])
    purpose_encoded_df = pd.DataFrame(purpose_encoded, columns=encoder.get_feature_names_out(['purpose']))

    # Binning the 'fico' scores into categories
    bins = [0, 650, 700, 750, 850]
    labels = ['Poor', 'Fair', 'Good', 'Excellent']
    data['fico_category'] = pd.cut(data['fico'], bins=bins, labels=labels, right=False)

    # Creating an interaction term between 'fico' and 'int.rate'
    data['fico_int_rate_interaction'] = data['fico'] * data['int.rate']

    # Concatenate the one-hot encoded 'purpose' dataframe back to the original dataframe
    data_transformed = pd.concat([data, purpose_encoded_df], axis=1)
    data_transformed.to_csv(output_file_path)

if __name__ == "__main__":
    transform_data()