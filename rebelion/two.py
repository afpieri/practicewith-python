# booleans

#print(5==5)
#print(5!=5)
#print(5>5)
#print(5<5)
#print(5>=5)
#print(5>=5)

#if the grade is greater than 70, the exam is approved
#grade_pieri = 80
#if grade_pieri > 70:
 #   print("congrats!")
#else:
 #   print("try again later!")
#print ("good luck in the other exams!")

#people = ["austin", "fer", "juan", "luis"]
  #            0      1      2      3
#print(people[3])
#print(len(people))
#print(people[-1])
#print(people[0:3])
#print(people[1:])
#print(people[:2])

#people = ["austin", "fer", "juan", "luis"]
#people.pop(2)                                    #saca nombres de la lista
#people.remove("luis")                            # saca nombres de la lista
#people.sort()                                    #ordena alfabeticamente o numericamente dependiendo de la lista
#print(people)

import random                                 #seleccion aleatoria
people = ["austin", "fer", "juan", "luis"]
chosen_name = random.choice(people)
people.remove(chosen_name)
print(f"The chosen name is: {chosen_name}")
print(f"The length of people is: {len(people)}")

