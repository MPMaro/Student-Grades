import random

#List
grades = []
x=35
for i in range(x):
    grades.append(random.randint(0,100))
    


# Menu
loop = True
while loop:
    print(" ")
    print("1. Display All Grade")
    print("2. Display Honours")
    print("3. Stats")
    print("4. Randomize Grades")
    print("5. Exit")
    print(" ")

    sel = int(input("Enter selection 1-5: "))
    print(" ")

    if sel == 1:
        # Option 1
        print("ALL GRADES")
        for i in range(len(grades)):
            print( f"{grades[i]}%")
            
    elif sel == 2:
        # Option 2 
        honours = 0
        print("HONOURS")
        for i in range(len(grades)):
            if grades[i] >= 80:
                print(grades[i])
                honours += 1
        print(" Students with honours:", honours)
        
    elif sel == 3:
        # Option 3
        print("STATS")
        print(f"Highest grade: {max(grades)}%")
        print(f"Lowest Grades: {min(grades)}%")       
        print("Average Grade:",round(sum(grades) / len(grades)))
        
    elif sel == 4:
        # Option 4 
        # Makes a new array/reset
        grades = []
        for i in range(x):
            grades.append(random.randint(0,100))
        print("Grades Randomized")
        
    elif sel == 5:
        # Option 5
        print("Exited")
        loop = False
        