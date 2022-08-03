#name = "alan" # son iterables: string, lists, tuple, dictionary


#for r in name:
 #   print(r)

                            #elevator program

#while True:
#    answer = input("please enter the number of the floor")
#    if answer == " out":
#        print("exiting..")
#        break
#    else:
#        answer_floor = int(answer)
#        if answer_floor >= 0 and answer_floor <= 20:
#         print(f"you are on floor number{answer}")
 #       else:
  #          print(f"{answer_floor} does not exist" )


#def special_count(stop_count, step=1):
 #   for i in range(1, stop_count + 1, step):
  #      print(f"special count {i}")

#special_count(stop_count=5)
#special_count(stop_count=10, step=2)
#special_count(stop_count=20)

#def teo_pitagoras (a, b, c):
 #   numb_ab = a ** 2 + b ** 2
  #  numb_c = c ** 2
   # if numb_ab == numb_c:
    #    print(f"la combinacion de {a},{b},{c} cumplen el teorema de pitagoras!")
    #else:
     #   print(f"la combinacion de {a},{b},{c} NO cumplen el teorema de pitagoras!")

#teo_pitagoras(3, 4, 5)
#teo_pitagoras(4, 5, 9)

#def hide_digits(card_number):
 #   last_four_digits = card_number[-4:]
  #  return f'**** **** **** {last_four_digits}'

#card = hide_digits('1111222233330099')
#print(card)

def hide_digits(card_numbers):
    cards_list = []
    for card_number in card_numbers:
        last_digits = card_number [-4:]
        formatted_card = f'**** **** **** {last_digits}'
        cards_list.append(formatted_card)
    return cards_list




cards= hide_digits(['1111222233330099', '1212565689897474', '8787545421213636'])
print(cards)












