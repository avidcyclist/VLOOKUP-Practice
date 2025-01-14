# Mock Data Project

This project is designed to create and demonstrate mock data related to skills commonly found on resumes, particularly focusing on Excel functions such as VLOOKUP and INDEX. The project includes a Python script to generate the mock data, a CSV file containing the data, and an Excel sheet that illustrates how to use the functions with the mock data.

## Project Structure

```
mock-data-project
├── data
│   └── mock_data.csv          # Contains the mock data in CSV format
├── scripts
│   └── generate_data.py       # Python script to generate mock data
├── sheets
│   └── example.xlsx           # Excel file demonstrating VLOOKUP and INDEX usage
└── README.md                  # Documentation for the project
```

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (can be installed via `pip`):
  - pandas

### Running the Data Generation Script

1. Clone the repository to your local machine.
2. Navigate to the `scripts` directory.
3. Run the following command to generate the mock data:

   ```
   python generate_data.py
   ```

4. This will create the `mock_data.csv` file in the `data` directory.

### Using the Excel Sheet

- Open `example.xlsx` in Excel.
- The sheet contains examples of how to use the VLOOKUP and INDEX functions with the mock data.
- Follow the instructions in the Excel file to see practical applications of these functions.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features. 

## License

This project is open-source and available under the MIT License.