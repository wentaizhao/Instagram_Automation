from bot import FollowerBot

DRIVER_PATH = DRIVER_PATH
TARGET_ACCOUNT = TARGET_ACCOUNT
USERNAME = USERNAME
PASSWORD = PASSWORD

bot = FollowerBot(DRIVER_PATH)
bot.login(USERNAME, PASSWORD)


def print_options():
    print('Here are your options')
    print('\t0) Quit')
    print('\t1) Follow followers of account')
    print('\t2) Find people that don\'t follow me back')
    print('\t3) Find my followers')
    print('\t4) Find my following')


def print_list(my_list):
    print()
    print()
    print()
    print('------ACCOUNTS------')
    for i in my_list:
        print(i)


isTrue = True
while isTrue:
    print_options()
    choice = input()
    print()
    if choice == '0':
        isTrue = False
    elif choice == '1':
        num = int(input("How many followers"))
        bot.follow_followers(TARGET_ACCOUNT, num)
    elif choice == '2':
        account_list = bot.get_not_following_back(TARGET_ACCOUNT)
        print_list(account_list)
    elif choice == '3':
        account_list = bot.get_followers(TARGET_ACCOUNT)
        print_list(account_list)
    elif choice == '4':
        account_list = bot.get_following(TARGET_ACCOUNT)
        print_list(account_list)
    else:
        print('Invalid input. Try again')
    print()

bot.quit()
print("Exiting program")
