

login1=['user1','user2','user3']
password1=['123','345','567']

def registration(login:str,password:str):
    """
    :param password:str
    :param login:str
    """
    while login==str(login):
        if login in login1:
            login1.append(login)
            """thanks to append we have tied a list login1 to login
            at registration
            """
            if password in password1:
                password1.append(password)
                print(f'hello {login}')
                break
            elif password not in password1:
                print('incorrect password')
                password=input('password:')
            elif login not in login1:
                print('incorrect login')
                login=input('login:')
def make(login:str,password:str):
    login1.append(login)
    while True:
        if len(password)<2:
            print('simple password')
            password=input('password')
            
        elif len(password)>=2:
            password1.append(password)
            print('you have registered')

            return login,password
