import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)  # Remove missing values
    df['Price'] = df['Price'].apply(lambda x: round(x, 2))  # Round prices to 2 decimal places
    df.to_csv('../data/cleaned_data.csv', index=False)

if __name__ == "__main__":
    clean_data('../data/mock_data.csv')