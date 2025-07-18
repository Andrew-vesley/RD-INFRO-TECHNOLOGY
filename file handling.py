import pandas as pd
import os
import json
def create_csv(filename):
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [30, 25, 35],
        'Department': ['HR', 'IT', 'Finance'],
        'Salary': [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV created: {filename}")

def process_csv(csv_file, json_file):
    df = pd.read_csv(csv_file)
    avg_salary = df.groupby("Department")["Salary"].mean().to_dict()

    with open(json_file, 'w') as f:
        json.dump(avg_salary, f, indent=4)
    print(f"Average salaries saved to JSON: {json_file}")

def main():
    os.makedirs("data", exist_ok=True)
    csv_path = os.path.join("data", "employees.csv")
    json_path = os.path.join("data", "avg_salary.json")
    
    create_csv(csv_path)
    process_csv(csv_path, json_path)

if __name__ == "__main__":
    main()
