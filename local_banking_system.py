print('Local Banking system\n')

def menu():
    print("""
Put the option what u want:
1)Register
2)Login
    """) 
menu()
opc = int(input(''))


class users:
    def __init__(self,user,psw,cash):
        self.user = user
        self.psw = psw
        self.cash = cash
    # user = 'psico'
    # psw = 'psico123'
    # cash = 1000

def advicment():
    print('The username and the password must init with a letter')

def menu2():
    print("""
What operation do u want realize?

1)deposit money
2)withdraw money
    """)

error = 'Error'
if opc == 1:
    advicment()
    user = input('user: ')
    psw = input('password: ')
    userlist = [user,psw]
elif opc == 2:
    advicment()
    userr = input('User: ')
    if userr in users.user:
        psw = input('Password: ')
        if psw in users.psw:
            print(f'Welcome {users.user}')
            menu2()
            opc2 = int(input(': '))
            if opc2 == 1:
                cuantity = int(input('how much money do you want to deposit: '))
                result = cuantity + users.cash
                print(f'Your actually money is: {result}')
                print('Do u wanna realize another operation? [1Yes][2NO]')
                reopc = int(input())
                if reopc == 1:
                    menu2()






