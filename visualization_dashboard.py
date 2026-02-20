import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_dataset():
    data = {
        "Math": [85, 78, 90, 88, 76],
        "Science": [90, 85, 88, 92, 80],
        "English": [75, 70, 80, 85, 78]
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = create_dataset()

    df.mean().plot(kind='bar')
    plt.title("Average Marks by Subject")
    plt.ylabel("Average Marks")
    plt.show()

    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()
