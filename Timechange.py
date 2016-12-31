import time

def changeTime(num):
    print(time.localtime(num))
    print(time.asctime(time.localtime(num)))

if __name__ == '__main__':
    select = 'N'
    while not(select == 'Y'):
        NUM = int(input('Input Number: '))
        changeTime(NUM)
        select = input("Do you want to Quit? [Y/N]")