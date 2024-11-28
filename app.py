from enum import Enum
from collections import Counter
import streamlit as st

# Define the categories
class Category(Enum):
    ONES = "ONES"
    TWOS = "TWOS"
    THREES = "THREES"
    FOURS = "FOURS"
    FIVES = "FIVES"
    SIXES = "SIXES"
    SEVENS = "SEVENS"
    EIGHTS = "EIGHTS"
    THREE_OF_A_KIND = "THREE_OF_A_KIND"
    FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
    FULL_HOUSE = "FULL_HOUSE"
    SMALL_STRAIGHT = "SMALL_STRAIGHT"
    ALL_DIFFERENT = "ALL_DIFFERENT"
    LARGE_STRAIGHT = "LARGE_STRAIGHT"
    SCHOONER = "SCHOONER"
    CHANCE = "CHANCE"

# Map each category to its corresponding dice face value
category_to_value = {
    Category.ONES: 1,
    Category.TWOS: 2,
    Category.THREES: 3,
    Category.FOURS: 4,
    Category.FIVES: 5,
    Category.SIXES: 6,
    Category.SEVENS: 7,
    Category.EIGHTS: 8,
}

# Score for a specific category
def score(category, dice_roll):
    count = Counter(dice_roll)
    unique_values = sorted(count.keys())

    if category == Category.THREE_OF_A_KIND:
        if any(v >= 3 for v in count.values()):
            return sum(dice_roll)
    elif category == Category.FOUR_OF_A_KIND:
        if any(v >= 4 for v in count.values()):
            return sum(dice_roll)
    elif category == Category.FULL_HOUSE:
        if set(count.values()) == {2, 3}:
            return 25
    elif category == Category.SMALL_STRAIGHT:
        if any(set(straight).issubset(dice_roll) for straight in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8])):
            return 30
    elif category == Category.ALL_DIFFERENT:
        if len(count) == 5:
            return 35
    elif category == Category.LARGE_STRAIGHT:
        if unique_values in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]):
            return 40
    elif category == Category.SCHOONER:
        if len(count) == 1:
            return 50
    elif category == Category.CHANCE:
        return sum(dice_roll)
    elif category in category_to_value:
        target_value = category_to_value[category]
        return target_value * count.get(target_value, 0)

    return 0

# Determine the top scoring categories
# def top_categories(dice_roll):
#     category_scores = {category: score(category, dice_roll) for category in Category}
#     max_score = max(category_scores.values())
#     return [category.name for category, score_value in category_scores.items() if score_value == max_score]
def top_categories(dice_roll):
    category_scores = {category: score(category, dice_roll) for category in Category}
    max_score = max(category_scores.values())
    # Return a dictionary of categories with the maximum score
    return {category.name: score_value for category, score_value in category_scores.items() if score_value == max_score}

# Example Usage
# dice_roll_1 = [1, 1, 1, 7, 7]
# print("Score for Full House:", score(Category.FULL_HOUSE, dice_roll_1))  # Expected output: 25

# dice_roll_2 = [3, 3, 3, 6, 7]
# print("Top Categories:", top_categories(dice_roll_2))  # Expected output: [Category.THREE_OF_A_KIND, Category.CHANCE]


st.title("Dice Scoring App")

dice_roll_input = st.text_input("Enter the dice roll (comma-separated, e.g., 1,2,3,4,5): ")

try:
    dice_roll = [int(num.strip()) for num in dice_roll_input.split(",") if num.strip()]
except ValueError:
    st.error("Invalid input. Please enter numbers separated by commas.")
else:
    # Calculate and display top categories only if input is valid
    if st.button("Calculate Top Categories"):
        top_categories_dict = top_categories(dice_roll)
        st.write("Top Categories with the highest score:")
        for category, score_value in top_categories_dict.items():
            st.write(f"{category}: {score_value}")