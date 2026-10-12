
def get_initial_readings():
    """Return the initial simulated device temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True if the text represents a whole number."""
    if len(text) == 0:
        return False

    start = 0

    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True


def get_valid_reading(lowest, highest):
    """Keep asking until the user enters a valid reading."""
    while True:
        text = input("Enter new reading: ")

        if len(text) == 0:
            print("Invalid input. The reading cannot be empty.")
        elif not is_whole_number(text):
            print("Invalid input. Enter a whole number only.")
        elif int(text) < lowest or int(text) > highest:
            print(
                f"Invalid reading. Enter a value from "
                f"{lowest} to {highest}."
            )
        else:
            return int(text)


def display_menu():
    """Display the five available menu options."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Display all readings with their position numbers."""
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings):
    """Validate a new reading and add it to the list."""
    new_reading = get_valid_reading(0, 100)
    readings.append(new_reading)
    print("\nReading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the classification of one temperature reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings):
    """Display the classification of every stored reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, 30, 35)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Return the total of all temperature readings."""
    total = 0

    for reading in readings:
        total = total + reading

    return total


def compute_average(readings):
    """Return the average temperature of all readings."""
    total = compute_total(readings)
    return total / len(readings)


def find_minimum(readings):
    """Return the lowest temperature using a loop."""
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    """Return the highest temperature using a loop."""
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return the number of readings in a specified category."""
    count = 0

    for reading in readings:
        result = classify_reading(
            reading, warning_limit, critical_limit
        )

        if result == category:
            count = count + 1

    return count


def compute_percentage(count, total_count):
    """Return the percentage represented by a category count."""
    return count / total_count * 100


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    """Calculate and display the complete monitoring summary."""
    total_count = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    normal_percentage = compute_percentage(normal_count, total_count)
    warning_percentage = compute_percentage(warning_count, total_count)
    critical_percentage = compute_percentage(critical_count, total_count)

    status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {total_count}")
    print(f"Total of readings : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")

    print(
        f"\nNORMAL : {normal_count} "
        f"({normal_percentage:.2f}%)"
    )
    print(
        f"WARNING : {warning_count} "
        f"({warning_percentage:.2f}%)"
    )
    print(
        f"CRITICAL : {critical_count} "
        f"({critical_percentage:.2f}%)"
    )

    print(f"\nOverall Status: {status}")


def main():
    """Control the menu and the flow of the program."""
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print(
                "\nInvalid choice. Please enter a number from 1 to 5."
            )


main()
