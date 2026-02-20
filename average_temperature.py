def calculate_average_temperature():
    print("===== Average Temperature Analyzer =====")

    try:
        total_days = int(input("Enter number of days: "))

        if total_days <= 0:
            print("Number of days must be greater than 0.")
            return

        temperatures = []

        for day in range(1, total_days + 1):
            temp = float(input(f"Enter temperature for Day {day}: "))
            temperatures.append(temp)

        print("\n----- Temperature Summary -----")
        print("Temperatures Entered:", temperatures)
        print("Highest Temperature:", max(temperatures))
        print("Lowest Temperature:", min(temperatures))
        print("Average Temperature:", round(sum(temperatures) / total_days, 2))

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    calculate_average_temperature()
