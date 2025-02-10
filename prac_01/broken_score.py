"""
CP1404/CP5632 - Practical
Broken program to determine score status

Prompt "Enter score: "
Read score
score = ConvertToFloat(score)

If score < 0 OR score > 100 Then
    result = "Invalid score"
Else If score > 90 Then
    result = "Excellent"
Else If score > 50 Then
    result = "Passable"
Else
    result = "Bad"
End If

Output result
"""

# TODO:Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    result = "Invalid score"
elif score > 90:
    result = "Excellent"
elif score > 50:
    result = "Passable"
else:
    result = "Bad"
print(result)
