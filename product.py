class Product(object):
    def __init__(self,price,name,weight,brand,cost):
         self.price = price
         self.name = name
         self.weight = weight
         self.brand = brand 
         self.cost = cost
         self.status="for sale"
         self.tax= 0
         
    def sell(self):
        self.status="sold"
        print "Status for 1st sale: ", self.status
        return self
    def addTax(self,percent):
        tax = self.price * percent
        totalPrice = self.price + tax
        print "Total Price: ", totalPrice
        return totalPrice
    def returnReason(self,reason):
        print "Product is being returned: check reason and see if it can be put back for sale!!!"
        if (reason=="defective"):
            self.status= "defective"
            self.price= 0
            print "reason: ",reason
            print "self.stat: ",self.status
            print "price: ", self.price
        elif(reason=="like new"):
            self.status="for sale"
            print "reason: ",reason
            print "self.stat: ",self.status
            print "price: ", self.price
        elif(reason=="opened box"):
            discount = self.price *.20
            print "Discount for a open box is :", discount
            self.status="used"
            self.price =  self.price - discount 
            print "reason: ",reason
            print "self.stat: ",self.status
            print "price: ", self.price  
        return self
    def dispayInfo(self):
        print "Price:", self.price
        print "name:", self.name
        print "weight:", self.weight
        print "brand:", self.brand
        print "cost:", self.cost
        print "status:", self.status


chair = Product(500,"Arm Chair","50 pound","Rooms To Go", 300 )
chair.sell()
chair.dispayInfo()
chair.addTax(.10)
chair.returnReason("like new")

sofa = Product(2500,"Sofa","150 pounds","Rooms To Go", 1700 )
sofa.sell()
sofa.dispayInfo()
sofa.addTax(.10)
sofa.returnReason("defective")


loveseat = Product(2500,"Love Seat","100 pounds","Rooms To Go", 1300 )
loveseat.sell()
loveseat.dispayInfo()
loveseat.addTax(.10)
loveseat.returnReason("opened box")
