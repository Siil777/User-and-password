from module1 import*


while True:
    print('would you like to register[1], login[2], exit[0]?')
    u=int(input('action:'))
    if u==0:
        print('!good-bye')
        break
    elif u==2:
        login=autoriz(input('login:'),input('password:'))
    elif u==1:
        generate=registration(input('login:'),input('password'))

