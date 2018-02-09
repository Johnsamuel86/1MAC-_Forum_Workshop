def withdraw(mbalance,request):
    if mbalance < request:
        return "You don't have enough balance !! your balance now: {}".format(mbalance)
    elif request < 0:
        return "Your request can't be done !! check your requested money"
    else:
        global balance
        balance -= request
        while request>0:
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
        return balance



balance = 500

print(withdraw(balance, 277))
print(withdraw(balance, 30))
print(withdraw(balance, 5))
print(withdraw(balance, 500))
