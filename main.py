"""
Pushpita Monir
IS 250-01
PyCharm and GitHub Setup Activity
24th November, 2025
"""
"""
Pseudocode:

1. Ask the user for the first score
2. Ask the user for the second score
3. Ask the user for the third score
4. Create a function that takes the three scores and find their average
5. Use the function to get the average
6. Print the first score on its own line
7. Print the second score on its own line
8. Print the third score on its own line
9. Print the average on its own line
"""

# Your Python code begins below this line.
# Every line you write must have a comment directly above it.

#ask the user for the first score
score1 = float(input("Enter your first score: "))
#ask the user for the second score
score2 = float(input("Enter your second score: "))
#ask the user for the third score
score3 = float(input("Enter your third score: "))
#create a function that finds the average of all three scores
def calculate_average(score1, score2, score3):
    #add the three scores and divide it by three
    return (score1 + score2 + score3) / 3
#Use the function to get the average score
average = calculate_average(score1, score2, score3)

#print the first score
print("First Score =", score1)
#print the second score
print("Second Score =", score2)
#print the third score
print("Third Score =", score3)
#print the average score
print("Average =", average)
  
