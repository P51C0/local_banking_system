# miras de cs
# CSGO-vQYJU-QjGRZ-hH84L-AaAnJ-DV43L



print('ejercicio de sistema bancario\n')

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
    print('The username only can be letter NO numbers and the password only can have numbers')

def menu2():
    print("""
What operation do u want realize?

1)ingres cash
2)retire cash
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
            print(f'Bienvenido {users.user}')
            menu2()
            opc2 = int(input(': '))
            if opc2 == 1:
                cuantity = int(input('how cash do u want ingress: '))
                result = cuantity + users.cash
                print(f'Your actually cash is: {result}')
                print('Do u wanna realize another operation? [1Yes][2NO]')
                reopc = int(input())
                if reopc == 1:
                    menu2()






