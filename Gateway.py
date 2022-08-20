from khayyam import jalali_datetime
from singleton import *
import threading

def mellat():
    return f"youre being directed to mellat Pay Gateway at {jalali_datetime.datetime.now()}"

def sepah():
    return f"youre being directed to sepah Pay Gateway at {jalali_datetime.datetime.now()}"


class product :
    pricelist = None

    def __init__(self , product , price):
        self.product = product
        self.price = price
        self.store(self)



    def __str__(self):
        return f"Youre Looking at {self.product}"




    @classmethod
    def store(cls,obj):
        if cls.pricelist == None:
            cls.pricelist = list()
        cls.pricelist.append(obj)


    @classmethod
    def bill(cls):
        total_price = sum(p.price for p in cls.pricelist)
        return f"Your Total Price is {total_price} Rials"



    @classmethod
    def pay(cls):
        sabad = list(p.product for p in cls.pricelist)
        mybill = sum(p.price for p in cls.pricelist)
        if mybill <= 1000:
            return sepah()
        return mellat()



if __name__ == "__main__":
    p1 = product('galaxyBudds', price=500)
    p2 = product('Apple_AirPod', 9)
    p3 = product('Haylou5', 55)
    p4 = proposition('Helipad')
    p6 = proposition('Hivi')
    p7 = proposition('LittleBird')
    p8 = proposition()
    t = threading.Thread(target=product.pay , args=3)
    t.start()
    #print(product.bill())
    #print(product.pay())
    #print(id(p4))
    #print(id(p6))
    #print(id(p7))
    #print(id(p8))
    #print(type(p1),type(p2),type(p3),type(p4),type(p6),type(p7),type(p8))
