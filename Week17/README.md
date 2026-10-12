# Simulated Device Monitoring and Alert System

## Student Name
Marian Trisha A. Panes

## Student Number
2600697

## Section
1CPE-A

## Project Description
This project is a menu-driven Python program that simulates monitoring device-temperature readings. It stores readings in a list, accepts additional valid readings, classifies readings, calculates a numerical summary, and determines the overall device status.

The program starts with the readings `28, 31, 35, 37, 29`. Readings below 30 °C are classified as `NORMAL`, readings from 30 °C to 35 °C inclusive are classified as `WARNING`, and readings above 35 °C are classified as `CRITICAL`. New readings must be whole numbers from 0 to 100 inclusive.

## Features
- Displays all current readings with their position numbers.
- Allows the user to add a valid reading.
- Rejects empty input, non-numeric input, decimal input, negative values, and values above 100.
- Classifies readings as `NORMAL`, `WARNING`, or `CRITICAL`.
- Calculates the total, average, minimum, and maximum readings.
- Counts each classification and calculates its percentage.
- Determines the overall status based on the readings.
- Repeats the menu until the user selects Exit.

## Requirements
- Python 3
- No external packages are required.
- The program uses a list, functions, loops, conditional statements, and input validation.

## How to Run
1. Make sure Python 3 is installed.
2. Open a terminal or command prompt.
3. Navigate to the folder containing `device_monitor.py`.
4. Run:

   ```bash
   python device_monitor.py
   ```

   If your computer uses `python3` to run Python 3, use:

   ```bash
   python3 device_monitor.py
   ```

5. Choose a menu option from 1 to 5. Select option `5` to exit.

## Sample Output
Expected summary for the initial readings before any new readings are added:

```text
Total readings: 5
Total: 160
Average: 32.00
Minimum: 28
Maximum: 37

NORMAL: 2 (40.00%)
WARNING: 2 (40.00%)
CRITICAL: 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

The overall status is `ATTENTION REQUIRED` because the initial readings include a `CRITICAL` reading.

## Test Cases
The ten required tests and their results are listed in [test_cases.md](test_cases.md).

## Known Limitations
- Readings are stored in memory and return to the initial list when the program is restarted.
- The program simulates readings and is not connected to a real device or sensor.
- The accepted range and classification thresholds are fixed for this activity.

## Reflection
This activity helped me practice using functions, lists, loops, conditional statements, input validation, and return values in Python. It also helped me understand how functions can work together to process readings and display a summary. Testing the program in the terminal helped me check the menu, input validation, classification rules, and calculations.
