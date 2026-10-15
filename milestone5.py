import csv
import matplotlib.pyplot as plt

# Load the solar data
filename = "solar_data.csv"

times = []
voltages = []
currents = []
powers = []
weather = []

with open(filename, "r") as file:
    data = csv.DictReader(file)

    for row in data:
        times.append(row["Time"])
        voltages.append(float(row["Voltage"]))
        currents.append(float(row["Current"]))
        weather.append(row["Weather"])

        # This is gonna calculate power and then add it to the list
        power = float(row["Voltage"]) * float(row["Current"])
        powers.append(power)


# The start of my main menu in a loop
while True:

    print()
    print("====================================")
    print("       SOLAR CELL DATA ANALYZER")
    print("====================================")
    print("1. Plot Power vs. Time")
    print("2. Analyze Solar Patterns")
    print("3. Find Maximum Power")
    print("4. View Raw Data")
    print("5. Load a Different Data File")
    print("6. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    # Plot graph
    if choice == "1":

        plt.plot(times, powers)
        plt.xlabel("Time")
        plt.ylabel("Power (W)")
        plt.title("Solar Cell Power vs. Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Analyze patterns
    elif choice == "2":

        total_power = 0

        for power in powers:
            total_power += power

        average_power = total_power / len(powers)

        print()
        print("SOLAR PATTERN ANALYSIS")
        print("----------------------")
        print("Average Power:", average_power, "W")

        if average_power > 5:
            print("The solar cell produced a relatively high amount of power.")
        elif average_power > 2:
            print("The solar cell produced a moderate amount of power.")
        else:
            print("The solar cell produced a relatively low amount of power.")

        print()
        print("Average power at each time of day:")

        time_list = []

        for time in times:
            if time not in time_list:
                time_list.append(time)

        highest_time = ""
        highest_average = 0

        for time in time_list:
            total = 0
            count = 0

            for i in range(len(times)):
                if times[i] == time:
                    total += powers[i]
                    count += 1

            time_average = total / count

            print(time, ":", time_average, "W")

            if time_average > highest_average:
                highest_average = time_average
                highest_time = time

        print()
        print("The highest average power occurred at", highest_time)
        print("Average power at this time:", highest_average, "W")

        print()
        print("This shows that solar power changes throughout the day.")
        print("The solar cell generally produces more power around the")
        print("middle of the day and less power in the morning and evening.")
    # Find maximum power
    elif choice == "3":

        maximum_power = powers[0]
        maximum_index = 0

        for i in range(len(powers)):

            if powers[i] > maximum_power:
                maximum_power = powers[i]
                maximum_index = i

        print()
        print("MAXIMUM POWER")
        print("-------------")
        print("Maximum Power:", maximum_power, "W")
        print("Time:", times[maximum_index])
        print("Voltage:", voltages[maximum_index], "V")
        print("Current:", currents[maximum_index], "A")
        print("Weather:", weather[maximum_index])

    # View raw data
    elif choice == "4":

        print()
        print("RAW SOLAR DATA")
        print("--------------")

        for i in range(len(times)):
            print(times[i], voltages[i], currents[i], weather[i])

    # Load a different file
    elif choice == "5":

        filename = input("Enter the name of the new data file: ")

        times = []
        voltages = []
        currents = []
        powers = []
        weather = []

        with open(filename, "r") as file:
            data = csv.DictReader(file)

            for row in data:
                times.append(row["Time"])
                voltages.append(float(row["Voltage"]))
                currents.append(float(row["Current"]))
                weather.append(row["Weather"])

                power = float(row["Voltage"]) * float(row["Current"])
                powers.append(power)

        print("New data file loaded successfully.")

    # Exit
    elif choice == "6":

        print()
        print("Thank you for using Solar Cell Data Analyzer!")
        print("Program ended.")
        break

    # Invalid choice
    else:

        print()
        print("Invalid choice. Please enter a number from 1 to 6.")