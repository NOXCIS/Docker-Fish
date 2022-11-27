import random   
import string  
import secrets # import package  
  
def genApass():
    num = 142 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
# print the Secure string   
    return (res)
