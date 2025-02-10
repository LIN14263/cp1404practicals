"""
FOR i FROM 1 TO 20 STEP 2
    PRINT i followed by a space
PRINT a new line

FOR i FROM 0 TO 100 STEP 10
    PRINT i followed by a space
PRINT a new line

FOR i FROM 20 TO 1 STEP -1
    PRINT i followed by a space
PRINT a new line

INPUT star

FOR rows FROM 0 TO star
    FOR columns FROM 0 TO rows - 1
        PRINT "*" followed by a space
    PRINT a new line

"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star = int(input("Number of stars:"))
for rows in range(star+1):
    for columns in range(rows):
        print("*", end=' ')
    print()