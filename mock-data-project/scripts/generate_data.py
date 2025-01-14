import pandas as pd
import random

def generate_mock_data():
    # Define the mock data
    data = {
        "ID": [i for i in range(1, 101)],
        "Name": [f"Product {i}" for i in range(1, 101)],
        "Category": [random.choice(["Electronics", "Clothing", "Home", "Books", "Toys"]) for _ in range(100)],
        "Price": [round(random.uniform(10, 500), 2) for _ in range(100)],
        "Stock": [random.randint(0, 100) for _ in range(100)]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Export to CSV
    df.to_csv('../data/mock_data.csv', index=False)

if __name__ == "__main__":
    generate_mock_data()