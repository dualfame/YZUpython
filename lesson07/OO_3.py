class account:
    name = ''   #公有變數
    __balance = 1000    #私有變數

    def __init__(self, name, money):    #建構式
        self.name = name
        self.__balance = money

    def __str__(self):
        return self. name + "有 $" + str(self.__balance)

    def addBalance(self, money):
        if money > 0:
            self.__balance = self.__balance + money

if __name__ == '__main__':
    account.bank = '中信銀'    #靜態變數
    acc = account('DW', 300)
    print(account.bank, acc)
    acc2 = account('Jessie', 500)
    print(account.bank, acc2)
#
# if __name__ == '__main__':
#     account.bank = '中信銀'    #靜態變數
#     acc = account()
#     acc.name = 'DW'
#     acc.addBalance(500)
#     print(account.bank, acc)
#     acc2 = account()
#     acc2.name = 'Mary'
#     print(account.bank, acc2)
#
