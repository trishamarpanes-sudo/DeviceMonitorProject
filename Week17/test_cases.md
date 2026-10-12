# Test Cases: Simulated Device Monitoring and Alert System

**Tested by:** Marian Trisha A. Panes  
**Date of testing:** October 12, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01: View initial readings | Choose `1` immediately after starting the program. | Five readings: 28, 31, 35, 37, 29. | The program displayed the five initial readings: 28, 31, 35, 37, and 29. | Pass |
| TC02: Add a valid reading | Choose `2`, then enter `33`. | Display “Reading added successfully.” and add 33 to the list. | The program accepted 33, displayed the success message, and added it to the readings list. | Pass |
| TC03: Non-numeric input | Choose `2`, then enter `abc`. | Reject the input and leave the list unchanged. | The program rejected `abc`, displayed an invalid-input message, and did not add it to the list. | Pass |
| TC04: Below valid range | Choose `2`, then enter `-5`. | Reject the value and leave the list unchanged. | The program rejected `-5` because it is outside the accepted range and did not add it to the list. | Pass |
| TC05: Above valid range | Choose `2`, then enter `120`. | Reject the value and leave the list unchanged. | The program rejected `120` because it is outside the accepted range and did not add it to the list. | Pass |
| TC06: Boundary 30 °C | Add `30`, then choose `3` to classify the readings. | Classify 30 °C as `WARNING`. | The program classified 30 °C as `WARNING`. | Pass |
| TC07: Boundary 35 °C | Choose `3` to classify the readings. | Classify 35 °C as `WARNING`. | The program classified 35 °C as `WARNING`. | Pass |
| TC08: Numerical summary | Choose `4` before adding any readings. | Total: 160; average: 32.00; minimum: 28; maximum: 37; overall status: `ATTENTION REQUIRED`. | The initial summary showed total 160, average 32.00, minimum 28, maximum 37, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), and overall status `ATTENTION REQUIRED`. | Pass |
| TC09: Invalid menu choice | Enter `9` at the main menu. | Display an error message and show the menu again. | The program displayed an invalid-choice message and returned to the menu. | Pass |
| TC10: Exit | Choose `5`. | Display the exit message and end the program. | The program displayed the exit message and ended. | Pass |

## Bugs Found and Fixed

No bugs were encountered during the terminal run. The most important test to check was the boundary classification, because both 30 °C and 35 °C must be classified as `WARNING`. The program's classification results matched the required rules.

## Additional Input Validation Checks

The activity also requires rejecting empty input and decimal input such as `3.5`. If these two inputs were not tested during the terminal run, test them before submitting and update this section if the observed results differ.
