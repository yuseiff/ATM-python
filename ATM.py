def main():
    os.system('cls')
    CheckPass()
   
    

def CheckPass():
    try:
        pin=input("Enter You Password: ")
    except ValueError:
        os.system('cls')
        print("Wrong input, Try again")
        main()
        
    with open('pass.txt','r+') as file:
        data=file.read()
    if data == pin:
        menu()
    else:
        os.system('cls') 
        print('Wrong Password!!')
        time.sleep(1)
        main()


def menu():

    os.system('cls')

    print("1)Check Account \n2)Deposite Cash \n3)Withdraw Cash \n4)Change Pin \n5)Quit")
    try:
        choice = int(input("Please Enter Your Choice: "))
    except ValueError:
        os.system('cls')
        print("Wrong input, Try again")
        menu()

    match choice:
        case 1:
            CheckAccount()

        case 2:
            DepositeCash()

        case 3:
            WithdrawCash()

        case 4:
            ChangePin()
    
        case 5:
            os.system('cls')
            exit(0)

        case _:
            os.system('cls')
            print("Wrong input, Try again")
            menu()


def CheckAccount():
    os.system('cls')
    with open("Account.txt",'r') as file:
        data = file.read()
    print(f"Cash = {data}")
    choice = input('are want to back? (y/n):').lower()

    if choice in ['y','yes']:
        os.system('cls')
        menu()
    else : 
        CheckAccount()

def DepositeCash():

    os.system('cls')
    file=open('Account.txt','r+') 
    olddata = float(file.read())
    print(f"Cash= {olddata}")
    newdata = float(input("Enter Amount To Deposite: "))
    data = str(olddata + newdata)
    file.seek(0)
    file.truncate(0)
    file.write(data)
    file.close()
    menu()

def WithdrawCash():
    os.system('cls')
    file=open('Account.txt','r+') 
    olddata = float(file.read())
    print(f"Cash= {olddata}")
    newdata = float(input("Enter Amount To Withdraw: "))
    data = str(olddata - newdata)
    file.seek(0)
    file.truncate(0)
    file.write(data)
    file.close()
    menu()

def ChangePin():
    os.system('cls')
    pin=input('Enter your current password: ')
    with open('pass.txt','r+') as file:
        data = file.read()

        while(pin != data):
            print("Worng Password")
            pin=input('Enter your current password: ')
        os.system('cls')
        Newpin = input('Enter the new password: ')
        conpin = input('Confirm the password: ')

        while(conpin != Newpin):
            conpin = print('Confirm the pin: ')

        file.seek(0)
        file.truncate(0)
        file.write(Newpin)

    menu()



import os,time



main()