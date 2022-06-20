import random

def sections():
    sections = [1,2,3]

    return sections

def section_lists(section_choice):
    #Replaced 3 variables with one list
    list_sections = [0,0,0]
    for n in range(1,31):
        rand = random.choice(section_choice)
        print(f"Signup for {n} is for section {rand}")
        if rand == 1:
            list_sections[0] += 1
        elif rand == 2:
            list_sections[1] += 1
        elif rand == 3:
            list_sections[2] += 1
        else:
            print("Invalid")
        

    return list_sections

def counter(total):
    if total[0] > 10:
        print(f"In section 1 there are 10 students that are enrolled with {total[0] - 10} students that are waitlisted.")
    elif total[0] == 1:
        print("In section 1, only 1 student has enrolled, I guess nobody likes that class")
    else:
        print(f"In section 1 there are {total[0]} students that are enrolled. There are 0 people waitlisted. ")
    if total[1] > 10:
        print(f"In section 2 there are 10 students that are enrolled with {total[1] - 10} students that are waitlisted.")
    elif total[1] == 1:
        print("In section 2, only 1 person has enrolled, I guess nobody likes that class")
    else:
        print(f"In section 2 there are {total[1]} students that are enrolled. There are 0 people waitlisted. ")
    if total[2] > 10:
        print(f"In section 3 there are 10 students that are enrolled with {total[2] - 10} students that are waitlisted.")
    elif total[2] == 1:
        print("In section 3, only 1 person has enrolled into the class, I guess nobody likes that class")
    else:
        print(f"In section 3 there are {total[2]} students that are enrolled. There are 0 people waitlisted. ")

    
    return [total]

def most_popular(total):
    maxed = max(total)
    highest_index = total.index(maxed)
    percent = ((maxed / 30) * 100)
    print(f"\nThe most popular secion is section {highest_index + 1} with {maxed} students enrolled. With {percent:.2f}% of the total students enrolled. ")