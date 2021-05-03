shopitems= {
	"name": "Clark",
	"age": 19,
	"cart": {"Books": 300, "Electronics": 2000, "Stationary": 100, "Sports Item": 1000}
  }
def discount(shopitems):
    Final_billing_amount=0
    if(shopitems['age']<20):
        shopitems['cart']['Books']=shopitems['cart']['Books']-shopitems['cart']['Books']*0.25
        shopitems['cart']['Sports Item']=shopitems['cart']['Sports Item']-shopitems['cart']['Sports Item']*0.25
        shopitems['cart']['Electronics']=shopitems['cart']['Electronics']-shopitems['cart']['Electronics']*0.10
        Final_billing_amount=int(shopitems['cart']['Books']+shopitems['cart']['Electronics']+shopitems['cart']['Stationary']+shopitems['cart']['Sports Item'])
        print("age < 20\n\t25% discount on books and 25% discount on sport item\nElectronics 10% discount")
    #If Age is between 20 to 40, there is 25% discount on Home Supp
    elif(shopitems['age']>=20 and shopitems['age']<=40):
        shopitems['cart']['Books']=shopitems['cart']['Home Supplies']-shopitems['cart']['Home Supplies']*0.25
        print('20 <=age <= 40\n\t\t25% discount on home supplies')
        Final_billing_amount=int(shopitems['cart']['Fruits']+shopitems['cart']['Home Supplies']+shopitems['cart']['Toys'])
    else:
       shopitems['cart']['Electronics']=shopitems['cart']['Electronics']-shopitems['cart']['Electronics']*0.10
       Final_billing_amount=int(shopitems['cart']['Gardening Tools']+shopitems['cart']['Electronics']+shopitems['cart']['Vegetables'])
    print("Discounted Cart =",shopitems['cart'],'\nFinal billing amount =',Final_billing_amount)
discount(shopitems)
