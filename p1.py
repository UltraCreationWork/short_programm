# calculator
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    
    def substraction(self):
        if self.num1>self.num2:
            return self.num1 - self.num2
        else:
             return self.num2 - self.num1
    
    def multipication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return "zeor in divisor"
        else:
            return self.num1/self.num2

    def flore_division(self):
        if self.num2 == 0:
            return "zeor in divisor"
        else:
            return self.num1// self.num2

    def exponent(self):
        return self.num1 ** self.num2

    def remainder(self):
        return self.num1 % self.num2
    

while True:
    q = str(input("press any key to strat program q for quit:")).upper()
    if q == "Q":
        break
    else:
        try:
            print("""
            1 for addition
            2 for substraction
            3 for multipication
            4 for division
            5 for flore division
            6 for exponent
            7 for remainder""")
            user_choise = int(input("select your option from above:"))
            if user_choise==1:
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.addition()
                print(result)
            elif user_choise==2:
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.substraction()
                print(result)
            elif user_choise==3:
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.multipication()
                print(result)
            elif user_choise==4:  
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.division()
                print(result)
            elif user_choise==5:
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.flore_division()
                print(result)
            elif user_choise==6:
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.exponent()
                print(result)  
            elif user_choise==7:
                num1 = float(input("enter the first number:"))
                num2 = float(input("enter the second number:"))
                calcu = Calculator(num1,num2)
                result = calcu.remainder()
                print(result) 
            else:
                print("This is not valid choise")
        except:
            print("please enter number not alphabet")

    

        
        

