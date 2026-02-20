def clean_data(raw_data):
    cleaned_data = [item for item in raw_data if item is not None]
    unique_data = sorted(list(set(cleaned_data)))
    return unique_data


if __name__ == "__main__":
    sample_data = [23, 45, 23, None, 67, 89, 45, 100, None, 67]
    final_data = clean_data(sample_data)

    print("Original Data:", sample_data)
    print("Cleaned Data:", final_data)
