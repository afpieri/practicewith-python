#class tarjetaCD:
 #   pass
#TCD_1 = tarjetaCD()
#TCD_1.num = "4545787896963232"
#TCD_1.limit = 10000
#TCD_1.company = 'Uala'

#print(TCD_1.limit)

#class Creditcard:
 #   def __init__(self, number, company, limit = 1000):
  #      self.number = number
   #     self.company = company
    #    self.limit = limit

#c1 = Creditcard(number="4545656532321212", company="Uala")
#c2 = Creditcard(number="4545656532301010", company="cordobesa")
#c3 = Creditcard(number="4545656532324444", company="patagonia", limit= 5000)

#print(c1.number)
#print(c1.company)
#print(c1.limit)
#print(c2.number)
#print(c2.company)
#print(c2.limit)
#print(c3.number)
#print(c3.company)
#print(c3.limit)

class Creditcard:
    limit_raise_amount = 1.5

    def __init__(self, number, company, limit = 1000):
       self.number = number
       self.company = company
       self.limit = limit
    def hide(self):
        self.number = f"**** **** **** {self.number[-4:]}"
    def raise_limit(self):
        self.limit = Creditcard.limit_raise_amount * self.limit
        print(f'New limit raised to {self.limit}')



c1 = Creditcard(number="4545656532321212", company="Uala", limit=1000)
c1.raise_limit()



