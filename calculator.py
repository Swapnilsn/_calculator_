# Reconstruct the calcultor using user defined function

def add(x,y):       #define function
  return x+y
 
def sub(x,y):
  return (x-y)
 
def mul(x,y):
  return x*y
 
def div(x,y):
  return x/y 
 
print("Which opertion you want to perform")
print("+")
print("-")
print("*")
print("/")

choice=input("Enter your choice: +,-,*,/\n")
n1=int(input("Enter 1st Number : "))
n2=int(input("Enter 2nd Number : "))
 
if choice== '+':
  print(add(n1,n2))
elif choice=='-':
  print(sub(n1,n2))
elif choice=='*':
  print(mul(n1,n2))
elif choice=='/':
  print(div(n1,n2))  
else:
  print("Invalid opertor")
