
import os

#AVILABLE NOTES IN ATM SYSTEM:
no_amount={2000:0,500:0,200:0,100:0}

#ALL USER IN BANK:
all_user=[{'username':'tamil','pin':'1234','bank':'indian','balance':12000,'trans':[]},
          {'username':'kutti','pin':'1234','bank':'sbi','free_trans':5,'balance':15000,'trans':[]},
          {'username':'mani','pin':'1234','bank':'indian','balance':12000,'trans':[]},
          {'username':'deepika','pin':'1234','bank':'indian','balance':10000,'trans':[]},
          {'username':'arun','pin':'1234','bank':'sbi','free_trans':5,'balance':10000,'trans':[]},
          {'username':'kumar','pin':'1234','bank':'kvb','free_trans':5,'balance':10000,'trans':[]},
          {'username':'kavi','pin':'1234','bank':'hdfc','free_trans':5,'balance':10000,'trans':[]},
          {'username':'anu','pin':'1234','bank':'indian','balance':10000,'trans':[]},
          ]

#BANK TOTAL AMOUNT:
def balance_in_atm():
    sum=0
    for i in no_amount:
        sum+=(no_amount[i]*int(i))
    return sum  


#ADMIN FUNCTOIN:
def addmoney():
    os.system('cls')
    for i in no_amount:
        n=int(input("Enter the number of "+str(i)+" Notes: ")) 
        no_amount[i]+=n
    os.system('cls')
    print("**************************************")
    print("   amount added succesfully")
    print("**************************************") 
    input("\n\n\tPress enter continue!!!!")


def showamount():   
    os.system('cls') 
    for i in no_amount:
        print(i,"Number of the note:",no_amount[i])
    print("*********************************")
    print("Total atm amount is:",balance_in_atm())
    print("*********************************")    
    input("\n\n\tPress enter continue!!!")


def pinchange():
    os.system('cls')
    for i in all_user:

        new_pin= input("Enter the new pin:")
        if(i['pin']!=new_pin):
            new_pinn=input("cnformation new pin:")
            if(new_pinn!=new_pin):
                print("reenter password")
            else:
                i['pin']= new_pin
                print("*******************************")
                print("***       Saved pin          **")
                print("*******************************")
                input("\n\n\tPress enter continue")
                break


#CUSTMOR FUNCTION:              
def fundtransfer():
    os.system('cls')
    print("********************************")
    name=input("Enter receiver name:")
    for i in all_user:
        if name==i['username']:
            amount=int(input("Enter the amout:"))
            print("********************************")
            if i['bank'] !=i['bank']:
                amount+=20
                fi_amount=amount-20
            if i['balance'] >1000 and i['balance']>amount:
                if(i['balance']-amount)<=1000:
                    os.system('cls')
                    print("\n\nacount balance is low.")
                else:
                    os.system('cls')
                    fi_amount=(amount) 
                    i['balance']-=amount
                    print("************************************************")
                    print("Rs.",amount,"has been transferd to "+ i['username'])
                    print("account balance:",i['balance'])
                    print("*************************************************")
                    input("\n\n\tPress enter continue!!!!")
                    break
    else:
        os.system('cls')
        print("********************")
        print("account is not find")
        print("********************")



# WELCOME ATM SYSTEM IN 1 PAGE:        
while True:
    os.system('cls')
    print("************************************")
    print("*           ATM SYSTEM             *")
    print("*     WELCOME TO INDIAN BANK       *")
    print("************************************")
    print("1.ADMIN")
    print("2.CUSTMOR")
    print("3.EXIT")
    print("************************************")
    c=int(input("Enter the choice: "))
#ADMIN CHOISE AVILABLE IN ATM SYSTEMS:    
    if(c==1):
        os. system('cls')
        print("************************************")
        print("*     CONTINU WORK ADMIN           *")
        print("************************************")
        use=input("Enter the username:")
        paw=input("Enter the pin:")
        if(use=="admin" and paw=='1234'):
            while True:
                os.system('cls')
                print("***********************************") 
                print("****     LOGIN SUCCESFULLY     ****")
                print("****       CONTINU WORK        ****")
                print("****      WELCOME ADMIN        ****")
                print("***********************************") 
                print("1.LOAD")
                print("2.SHOW AMOUNT")
                print("3.EXIT")
                print("***********************************")
     
                ad=int(input("Enter the choice: "))
                if(ad==3):
                    break 
                elif(ad==1):
                    addmoney()
                elif(ad==2):
                    showamount()
                else:
                    os.system('cls')
                    print("**************************")
                    print("*     Invalid choice     *")
                    print("**************************")
                    input("\n\n\tPress enter continue!!!!")
                    continue
        else:
            os.system('cls')
            print("*****************************")
            print("  Invalid username and pin   ")
            print("*****************************") 
            input("\n\n\tpress enter continue!!!")
#CUSTAMER AVILABILE SYSTEM IN ATM:                             
    if(c==2):
        os.system('cls') 
        print("*****************************")
        print("*  CONTINUE WORK CUSTMAR    *")
        print("*****************************")
        user=input("Enter the username:")
        pas=input("Enter the pin:")

        for i in all_user:
            if user==i['username'] and pas==i['pin']:
                while True:
                    os.system('cls')
                    print("********************************")
                    print("*      LOGIN SUCCESFULLY       *")
                    print("*        CONTINUE WORK         *")
                    print("*        WELCOME USER          *")
                    print("********************************")
                    print("1.WITHDRAW")
                    print("2.DEPOSITE AMOUNT")
                    print("3.SHOW BALANCE")
                    print("4.PIN CHANGE")
                    print("5.FOUD TRANSFER")
                    print("6.EXIT")
                    print("********************************")
                    us=int(input("Enter the choice:"))
                    if(us==6):
                        os.system('cls')
                        break
# WITHDRAW IN ATM SYSTEM:               
                    elif(us==1):
                        os.system('cls')
                        c=int(input("Enter the amount to be withdraw:"))        
                        if c <= balance_in_atm():
                            v=c
                            for j in no_amount:
                                if i['balance']>c:
                                    no_notes = int(c/j)

                                if no_notes > no_amount[j]:
                                    c -= j*no_amount[j]
                                    no_amount[j] -= no_amount[j]
                                    i['balance'] -= j*no_notes
                                elif no_notes <= no_amount[j]:
                                    c = int(c%j)
                                    no_amount[j] -= no_notes
                                    i['balance'] -= (no_notes*j)



                            print("**********************************")
                            print("Rs.",v,"has been withdrawed")
                            print("**********************************")
                            print("Your account balance:",i['balance'])
                            print("**********************************")
                            input("\n\n\tPress enter continue!!!!")

                        else:
                            os.system('cls')
                            print("********************************")
                            print("**  Atm running out of money  **")
                            print("********************************")
                            input("\n\n\tPress enter continue!!!!")  
#DEPOSITED AMOUNT IN ATM:                           
                    elif(us==2):
                        os.system('cls')
                        dp_amount=int(input("Enter the deposited amount:"))
                        i['balance']+=dp_amount
                        print("*******************************************")
                        print("Rs.",dp_amount,"has been deposited in your account")
                        print("********************************************")
                        print("     Account balance:",i['balance'])
                        print("********************************************")
                        input("\n\n\tPress enter continue!!!!")

#SHOW BALANCE IN ATM:
                    elif(us==3):
                        os.system('cls')
                        print("****************************")
                        print("Holder name:",i['username'])
                        print("Account balance:",i['balance'])
                        print("*****************************")
                        input("\n\n\tPress enter continue!!!!")


                    elif(us==4):
                        pinchange()
                                    
                   
                    elif(us==5):
                        fundtransfer()



                    else:
                        os.system('cls')
                        print("**************************")
                        print("****  Invalid choice  ****")
                        print("**************************")
                        input("\n\n\tPress enter continue!!!!")
                    
                        
        else:
            os.system('cls')
            print("*******************************")
            print("  Invalid username and pin     ")
            print("*******************************")
            input("\n\n\tPress enter continue!!!!")


    if(c==3):
        os.system('cls')
        print("**********************")
        print("*** you take card  ***")
        print("***   THANK YOU    ***")
        print("**********************")
        input("\n\n\tPrees enter home page!!!!")
        exit()
    
            