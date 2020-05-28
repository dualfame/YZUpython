import lesson08.Exception.defexcept as my #自建exception class (例外資料庫)

def login(username, password):
    if username == 'admin' and password == '1234':
        pass
    else:
        raise my.LoginException('登入失敗')

if __name__ == '__main__':
    try:
        login('admin', '123')
    except my.LoginException as e:
        print(e)
        e.HowToDo()
