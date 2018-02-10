class ATM():
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self,request):
        # this section for a decorated msgs
        welcome_msg = "*** Welcome to {} ".format(self.bank_name)
        balance_msg = "*** Current balance = {} ".format(self.balance)
        print("***" * 10)
        print(welcome_msg + "*" * (30 - len(welcome_msg)))
        print(balance_msg + "*" * (30 - len(balance_msg)))
        print("***" * 10)

        # balance operation
        if self.balance < request:
            print("You don't have enough balance !! your balance now: {}".format(self.balance))
        elif request < 0:
            print("Your request can't be done !! check your requested money")
        else:
            self.balance -= request
            while request > 0:
                if request >= 100:
                    request -= 100
                    print("Given 100.")
                elif request >= 50:
                    request -= 50
                    print("Given 50.")
                elif request >= 10:
                    request -= 10
                    print("Given 10.")
                elif request >= 5:
                    request -= 5
                    print("Given 5.")
                else:
                    print("Given {}.".format(request))
                    request = 0
            return "Your Balance after the withdraw is {}.".format(self.balance)




balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(200)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(820)
atm2.withdraw(2000)
