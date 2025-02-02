def show_balance():
    print(f'Your balance is: ${balance:.2f}')


def deposit():
    amount=float(input(f'Enter an amount to be deposited:'))
    if amount<0:
        print('Invalid amount')
    else:
        return amount

def withdraw():
    amount=float(input(f'Enter an amount to be withdrawn:'))
    if amount>balance:
        print('Insufficient funds')
        return 0
    elif amount<0:
        print('amount must me more than zero!!!')
        return 0
    else:
        return amount


balance=0
is_running=True
name=input('Enter your name: ')
while is_running==True:
    print('*****************************************')
    print(f"**Welcome to the banking app, {name}! Here is the list of functions**")
    print('*****************************************')
    print('1. Show Balance')
    print('2. Make a deposit')
    print('3. Withdraw money')
    print('4. Exit')
    print('*****************************************')


    choice=input('Enter the number (1-4): ')
    if choice=='1':
        show_balance()
    elif choice=='2':
        balance+=deposit()
    elif choice=='3':
        balance-=withdraw()
    elif choice=='4':
        is_running=False
        print('Bye!')
    else:
        print('Wrong input')




