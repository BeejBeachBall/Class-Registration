#I did required fun 1
from registration import section_lists, sections, counter, most_popular
import random
print("Welcome to Class Registration\n")

#Class registration
total = section_lists(sections())


#Seeing value of each index(Sections)
print("\n")
print(total)



#Class Counter
print("\n\n\n---CLASS REGISTRATION SUMMARY---\n")

counter(total)
print("----------------------------------------")
most_popular(total)

#required fun 1 output
"""Welcome to Class Registration

Signup for 0 is for section 1
Signup for 1 is for section 1
Signup for 2 is for section 3
Signup for 3 is for section 3
Signup for 4 is for section 3
Signup for 5 is for section 1
Signup for 6 is for section 1
Signup for 7 is for section 1
Signup for 8 is for section 3
Signup for 9 is for section 2


[5, 1, 4]



Class Registration Summary

In section 1 there are 5 students that are enrolled. There are 0 people waitlisted. 
In section 2, only 1 person has enrolled, I guess nobody likes that class
In section 3 there are 4 students that are enrolled. There are 0 people waitlisted. 

The most popular secion is section 1 with 5 students enrolled. With 16.67% students enrolled. 
"""

#normal 30 student output
"""Welcome to Class Registration

Signup for 0 is for section 3
Signup for 1 is for section 1
Signup for 2 is for section 1
Signup for 3 is for section 3
Signup for 4 is for section 1
Signup for 5 is for section 2
Signup for 6 is for section 1
Signup for 7 is for section 2
Signup for 8 is for section 1
Signup for 9 is for section 2
Signup for 10 is for section 1
Signup for 11 is for section 3
Signup for 12 is for section 2
Signup for 13 is for section 2
Signup for 14 is for section 3
Signup for 15 is for section 3
Signup for 16 is for section 1
Signup for 17 is for section 1
Signup for 18 is for section 2
Signup for 19 is for section 3
Signup for 20 is for section 1
Signup for 21 is for section 3
Signup for 22 is for section 3
Signup for 23 is for section 1
Signup for 24 is for section 1
Signup for 25 is for section 2
Signup for 26 is for section 1
Signup for 27 is for section 1
Signup for 28 is for section 2
Signup for 29 is for section 2
Signup for 30 is for section 3


[13, 9, 9]



Class Registration Summary

In section 1 there are 10 students that are enrolled with 3 students that are waitlisted.
In section 2 there are 9 students that are enrolled. There are 0 people waitlisted. 
In section 3 there are 9 students that are enrolled. There are 0 people waitlisted. 

The most popular secion is section 1 with 13 students enrolled. With 43.33% students enrolled. """