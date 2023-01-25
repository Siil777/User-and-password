

login1=['user1','user2','user3']
password1=['123','345','567']

def autoriz(login:str,password:str):
    """
    :param password:str
    :param login:str
    """
    while login==str(login):
            if login in login1:
               login1.append(login)
                
            if password in password1:
               password1.append(password)
               print(f'hello {login}')
               break
            else:
               print('you ought to register for start')
               break
def registration(login:str,password:str):
    
   while True:
        if login in login1:
            print('that nusername is taken')
            break
        if len(password)<2:
            print('simple password')
            password=input('password')
            
        elif len(password)>=2:
            password1.append(password)
            print('you have registered')
            break

            return login,password
