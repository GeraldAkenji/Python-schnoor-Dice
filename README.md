# Dice Scoring App

## Overview
The **Dice Scoring App** is a Streamlit-based web application designed to evaluate a set of dice rolls against different scoring categories. Users can input a dice roll, and the app will determine and display the highest scoring categories based on predefined scoring rules.

## Features
- Input a dice roll as a comma-separated list.
- Calculate scores for various categories such as:
  - Three of a Kind
  - Four of a Kind
  - Full House
  - Small Straight
  - Large Straight
  - All Different
  - Schooner
  - Chance
  - Individual face value categories (e.g., ONES, TWOS, etc.)
- Display the categories with the highest score.

## Scoring Categories
- **ONES, TWOS, THREES, etc.**: Sum of dice matching the specific face value.
- **THREE_OF_A_KIND**: Sum of all dice if at least three dice show the same number.
- **FOUR_OF_A_KIND**: Sum of all dice if at least four dice show the same number.
- **FULL_HOUSE**: Score 25 points if the dice roll contains three of one number and two of another.
- **SMALL_STRAIGHT**: Score 30 points for a sequence of four consecutive numbers.
- **LARGE_STRAIGHT**: Score 40 points for a sequence of five consecutive numbers.
- **ALL_DIFFERENT**: Score 35 points if all dice show different numbers.
- **SCHOONER**: Score 50 points if all dice show the same number.
- **CHANCE**: Sum of all dice.

## Installation and Usage

### Prerequisites
Ensure Python is installed on your system. Install required libraries using:
```bash
pip install streamlit
```

### Running the App
1. Save the provided code to a file named `app.py`.
2. Run the Streamlit app using the following command:
```bash
streamlit run app.py
```

### Using the App
- Open the provided local URL after running the command.
- Enter your dice roll as a comma-separated list (e.g., `1,2,3,4,5`).
- Click the **Calculate Top Categories** button to see the highest scoring categories and their scores.

## Example
**Input**: `3,3,3,6,7`

**Output**:
```
Top Categories with the highest score:
THREE_OF_A_KIND: 22
CHANCE: 22
```

## Notes
- The app checks for valid input and will display an error message for non-numeric or improperly formatted entries.
- The logic includes specific conditions for each scoring category to match the requirements outlined in the rules.


## Author
This project was developed using Python and Streamlit, with a focus on simplicity and functionality for dice scoring evaluation.

Enjoy using the Dice Scoring App!

GERALD AKENJI

