#SIMPLE CALCULATOR

def add(x,y): 
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    if(y==0):
        return "INVALID"
    else:
        return x/y
def multiply(x,y):
    return x*y


print("WELCOME! PLEASE SELECT AN OPERATION .\n 1. ADD\n 2. SUBTRACT\n 3. MULTIPLY\n 4. DIVIDE\n 5. EXIT")


while True:
    choice = int(input("ENTER CHOICE {1,2,3,4,5}"))

    if(choice == 5):
        print("THANK YOU")
        break
    elif(choice>5):
        print("INVALID INPUT ! PLEASE ENTER CHOICE BETWEEN (1,2,3,4)")
        continue
    num1 = float(input("ENTER FIRST NUMBER"))
    num2 = float(input("ENTER SECOND NUMBER"))

    if(choice == 1):
        print("RESULT :" ,add(num1,num2))
    elif(choice == 2):
        print("RESULT :" , subtract(num1,num2))

    elif(choice == 3):
        print("RESULT :" , multiply(num1,num2))
    elif(choice == 4):
        print("RESULT :" , divide(num1,num2))
    

