from datetime import date
import random
import time
class Account:
    trans = {}
    Acc = {}
    Balance = {}
    def Number(self,Acc):
    #    mini = pow(10,9)
    #    maxi = pow(10,10)-1
    #    return random.randint(mini,maxi)
        Acc_Number = 0
        if(len(Acc)==0):
            Acc_Number = 1000
            return Acc_Number
        else:
            Acc_Number +=1
            return Acc_Number
    
    def createAccount(self):
        username = input("Create Your User Name \n")
        Account_Number = self.Number(self.Acc)
        password = input("Create your Password \n")
        AmountDeposit = int(input("Deposit Minimum Balance To your Account \n"))
        self.Acc[Account_Number] = {"Username":username,"Balance":AmountDeposit,'Password':password}


    def deposit(self):
        Acc_Number = int(input("Enter Your Account Number\n"))
        Amount = int(input("Enter Amount to deposit\n"))
        if (Acc_Number in self.Acc):
            self.Acc[Acc_Number]['Balance'] +=Amount
            tm=time.strftime("%H:%M:%S", time.localtime())
            #dt=datetime.now()
            dtt=date.today()
            self.trans[tm]=[str(dtt),"Credited "+str(Amount)]
            self.Acc[Acc_Number]['Transaction']=self.trans
        else:
            print("Account Doesn't exist\n")


    def withdraw(self):
        Acc_Number = int(input("Enter Your Account Number\n"))
        Amount = int(input("Enter an Amount to withdraw\n"))
        if (Acc_Number in self.Acc):
            self.Acc[Acc_Number]['Balance'] -=Amount
            tm=time.strftime("%H:%M:%S", time.localtime())
            dtt=date.today()
            self.trans[tm]=[str(dtt),"Debited "+str(Amount)]
            self.Acc[Acc_Number]['Transaction']=self.trans
        else:
            print("Account Doesn't exist")


    def transfer(self):
        Acc_Number1 = int(input("Enter Your Account Number\n"))
        Acc_Number2 = int(input("Enter Account Number to which the fund should be transfered\n"))
        Amount = int(input("Enter Amount to transfer\n"))
        if(self.Acc[Acc_Number1]['Balance']<Amount):
            print("Insufficient Funds")
        else:
            tm=time.strftime("%H:%M:%S", time.localtime())
            dtt=date.today()
            self.Acc[Acc_Number1]['Balance'] -= Amount
            self.trans[tm]=[str(dtt),"Debited " + str(Amount)]
            self.Acc[Acc_Number1]['Transaction']=self.trans
            self.Acc[Acc_Number2]['Balance'] += Amount
            self.trans[tm]=[str(dtt),"Credited "+str(Amount)]
            self.Acc[Acc_Number2]['Transaction']=self.trans
            print("Amount Sent Successfully")


    def accountDetails(self):
        Acc_Number = int(input("Enter Your Account Number"))
        if(Acc_Number in self.Acc):
            print(self.Acc[Acc_Number])
        else:
            print("Account Doesn't exist")

    def transaction(self):
            Acc_Number = int(input("Enter Your Account Number"))
            if(Acc_Number in self.Acc):
                print(self.Acc[Acc_Number]['Transaction'])
        
    def services(self):
        while(1):
            print("**************************")
            print(" 1.Create Account \n 2.Deposit \n 3.Withdraw \n 4.Fund Transfer \n 5.View Account details by accno \n 6.Transaction Details\n 7.Exit")
            print("**************************")
            c = int(input("Please enter the required service\n"))
            if(c==1):
                self.createAccount()
                print(self.Acc)
            elif(c==2):
                self.deposit()
            elif(c==3):
                self.withdraw()
            elif(c==4):
                self.transfer()
            elif(c==5):
                self.accountDetails()
            elif(c==6):
                self.transaction()
            else:
                break
Acc = Account()
Acc.services()