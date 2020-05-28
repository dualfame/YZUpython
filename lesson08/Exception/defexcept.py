class LoginException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()

    def HowToDo(self):
        print('請重新登入')
        print('電洽02-15625412')