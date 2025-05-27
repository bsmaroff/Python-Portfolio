#AP Create Project
import random
correct = 0
president_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
                   26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

president_names=["Washington","Adams","Jefferson","Madison","Monroe","Quincy Adams",
                 "Jackson","Van Buren","Harrison","Tyler","Polk","Taylor","Fillmore",
                 "Pierce","Buchanan","Lincoln","Johnson","Grant","Hayes","Garfield",
                 "Arthur","Cleveland","Harrison","Cleveland","McKinley","Roosevelt",
                 "Taft","Wilson","Harding","Coolidge","Hoover","Roosevelt","Truman",
                 "Eisenhower","Kennedy","Johnson","Nixon","Ford","Carter","Reagan",
                 "Bush","Clinton","Bush","Obama","Trump","Biden", "Trump"]

president_terms=["1789-1797","1797-1801","1801-1809","1809-1817","1817-1825","1825-1829",
                 "1829-1837","1837-1841","1841-1841","1841-1845","1845-1849","1849-1850",
                 "1850-1853","1853-1857","1857-1861","1861-1865","1865-1869","1869-1877",
                 "1877-1881","1881-1881","1881-1885","1885-1889","1889-1893","1893-1897",
                 "1897-1901","1901-1909","1909-1913","1913-1921","1921-1923","1923-1929",
                 "1929-1933","1933-1945","1945-1953","1953-1961","1961-1963","1963-1969",
                 "1969-1974","1974-1977","1977-1981","1981-1989","1989-1993","1993-2001",
                 "2001-2009","2009-2017","2017-2021","2021-2025","2025-Present"]
#Function
def introduction():
     print("\nWelcome to the Ultimate President Quiz Guide!")
     print("This program will help you to know your presidents before your next test!\n")
     print("Make sure to only enter the presidents last name")
     print("If you get stuck, try pressing 1 for a hint on the term years\n")
     print("Good luck!\n")

def quiz(questions):
    global correct
    for i in range(questions):
         term_number=random.choice(president_numbers)
         answer = input("\nWho is president number " + str(term_number) + "? Press 1 for a hint (.5 points)")
         if answer == president_names[term_number-1]:
              print("Correct")
              correct = correct + 1
         elif answer == "1":
              print(president_terms[term_number-1])
              hint_answer = input("What is your answer?")
              if hint_answer == president_names[term_number-1]:
                  print("Correct")
                  correct = correct + .5
              else:
                  print("Incorrect")
         else:
              print("Incorrect")
    print("\nYou got " + str(correct) + " out of " + str(questions) + " correct!")
    if correct>=questions-1:
         print("\nGreat job!")
    else:
         print("\nYou need to keep studying")

#Main
introduction()
quiz(int(input("How many presidents would you like to quiz yourself on?")))

#Data for all 3 arrays: https://www.whitehouse.gov/about-the-white-house/presidents/

