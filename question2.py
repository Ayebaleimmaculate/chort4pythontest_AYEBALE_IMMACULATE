# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F


# Function to determine the grade based on the score
def determine_grade(score):
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    elif score >= 60:
        return "Grade D"
    elif score >= 40:
        return "Grade E"
    else:
        return "Grade F"

# Function to get scores for 5 course units and determine grades
def get_scores_and_grades():
    for i in range(1, 6):
        try:
            score = float(input(f"Enter the mark scored in course unit {i} (out of 100): "))
            if 0 <= score <= 100:
                grade = determine_grade(score)
                print(f"You have obtained in course unit {i}: {grade}")
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Call the function to execute
get_scores_and_grades()
