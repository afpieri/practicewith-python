#friend = {
 #   "name": "mike",
  #  "age": 26,
   # "is_male": True,
    #"weight" : 83.3,
#}
#print(list(friend.keys()))
#print(list(friend.keys())[0])

#numbers = list(range(5, 10, 2)) # se imprimen los numeros del 5  al 10 pero, subiendo de a 2.
#print(numbers)

friends=["alan", "john", "tom", "jack"]
best_friend = "tom"
#for friend in friends:
#   print(f"{friend} is my friend")

#if best_friend in friends:
 #    print(f"{best_friend} is in the list of friends")

for friend in friends:
    if friend == best_friend:
        print(f"{best_friend} is inside the list")
