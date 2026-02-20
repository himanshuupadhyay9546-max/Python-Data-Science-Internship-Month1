import pandas as pd

def create_dataset():
    data = {
        "Student": ["Amit", "Rahul", "Priya", "Amit", "Priya"],
        "Subject": ["Math", "Science", "Math", "Math", "Science"],
        "Marks": [85, 90, None, 85, 95]
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = create_dataset()

    print("Original Dataset:\n", df)

    df = df.dropna().drop_duplicates()

    print("\nCleaned Dataset:\n", df)

    print("\nAverage Marks by Subject:\n",
          df.groupby("Subject")["Marks"].mean())
