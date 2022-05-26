#Faculty software engineering project
class ATM:
    def showBalance(obj):
        print(f"[INFO] Balance available for account ID:{obj.id} {obj.firstName} {obj.lastName}: {obj.balance}$") 

    def addBalance(obj):
        usrAdd = input(f"[INFO] How much do you want to add?:")
        if ATM.validateInput(usrAdd, False):
            obj.balance += int(usrAdd)
            print(f"[SUCCESS] Successfully added {usrAdd}$.")

    def substractBalance(obj):
        #If we were to test if the amount provided was bigger than the balance before checking the input we could miss malicious input.
        usrSub = input(f"[INFO] How much do you want to substract?:")
        if ATM.validateInput(usrSub, False):
            usrSub = int(usrSub)
            if usrSub > obj.balance:
                print(f"[ERROR] The amount requested {usrSub}$ is greater than the acount's balance {obj.balance}.")
                tryAgain = input("[INFO] Do you want to try again? (y/n):?")
                if ATM.validateInput(tryAgain) and tryAgain == 'y':
                    ATM.substractBalance(obj)
                else:
                    print(f"[+] Goodbye {obj.firstName} {obj.lastName}!")
                    exit(0)
            obj.balance -= int(usrSub)
            print(f"[SUCCESS] Successfully substracted {usrSub}$.")

    def cardStatus(obj):
        if obj.is_active:
            print("[INFO] Card is active.")
        else:
            print("[INFO] Card is inactive.")

    def activateCard(obj, activationCode):
        if activationCode == ACTIVATION_CODE:
            obj.is_active = True
            print("[SUCCESS] Card activated/burnt successfully.")
        else:
            print("Activation code invalid.")

    def changePin(obj, secretCode):
        if secretCode == SECRETCODE:
            newPin = input("Input new pincode:")
            if ATM.validateInput(newPin, True):
                obj.pin = newPin
        else:
            print("Secret code invalid.")

    #Possibly recursive ATM main function caller
    def showOptions(obj):
        print("[INFO] What option do you choose?\n   [1] Show balance.\n   [2] Add balance.\n   [3] Substract balance.\n   [4] Card status.\n   [5] Activate card.\n   [6] Change pin.\n   [7] Exit.\n")
        usrValue = input("[INPUT] Choose option: ")
        if ATM.validateInput(usrValue, False):
            if int(usrValue) == 1:   
                ATM.showBalance(obj)
            elif int(usrValue) == 2:
                ATM.addBalance(obj)
            elif int(usrValue) == 3:
                ATM.substractBalance(obj)
            elif int(usrValue) == 4:
                ATM.cardStatus(obj)
            elif int(usrValue) == 5:
                ATM.activateCard(obj, ACTIVATION_CODE)
            elif int(usrValue) == 6:
                ATM.changePin(obj, SECRETCODE)
            elif int(usrValue) == 7:
                print(f"[+] Goodbye {obj.firstName} {obj.lastName}!")
                exit(0)
            else:
                print("[ERROR] Option non-existent.")
        try_again = input("[INFO] Do you want another option? (y/n): ")
        if try_again == 'y':
            ATM.showOptions(obj)
        else:
            print("[INFO] Goodbye!")
            exit(0)

    #Validate input for pins and choices
    #This function DOES NOT convert a variable's type, it just tests if it can be converted into an integer.
    #E.g "a" would not be true and trigger the error but "123" would be true thus validating the input checks.
    def validateInput(usrInput, ispin):
        if ispin:
            try:
                usrInput = int(usrInput)
            except Exception:
                print("[ERROR] Insert an integer please!")
                exit(0)
            if type(usrInput) == int and len(str(usrInput)) == 4:
                return True
        else:
            try:
                usrInput = int(usrInput)
            except Exception:
                print("[ERROR] Insert an integer please!")
                exit(0)
            return True


    class user:
        def __init__(self, id, firstName, lastName, pin, balance, is_active):
           self.id = id
           self.firstName = firstName
           self.lastName = lastName
           self.pin = pin
           self.balance = balance
           self.is_active = is_active

if __name__ == "__main__":
    #list of objects of class type user 
    database = [ATM.user(190803,"Sorin","Sav",9999,100000,True), ATM.user(925932,"Marius","Andronescu",1984,17403,True), ATM.user(749253,"Fechete","Denis",7498,32000,True),
    ATM.user(938724,"Alex","Savu",9439,300026,True), ATM.user(521643,"Alin","Cioanescu",1293,2698,True), ATM.user(359125,"Marinela","Tiriac",5271,832645,False)]
    SECRETCODE = 1928382453
    ACTIVATION_CODE = 1844282455
    
    print("[INFO] Welcome!\n[INFO] Enter the pin in order to access your account.\n[INFO] You have only 3 tries.\n[INFO] If you fail all 3 tries your card will be blocked.")

    trial = 0
    while trial < 3:
        pin = input("[INPUT] Enter pincode: ")
        if ATM.validateInput(pin, True):
            for obj in database:
                if int(pin) == obj.pin:
                    print(f"\n[INFO] Account ID:{obj.id} {obj.firstName} {obj.lastName}.")
                    ATM.showOptions(obj)                         
            trial+=1
            print(f"[WARNING] You have {abs(3-trial)}  tries left.")
        else:
            print("[ERROR] Insert an integer with exactly 4 numbers please.")
            trial += 1
            print(f"[WARNING] You have {abs(3-trial)}  tries left.")
    if trial == 3:
        print("[INFO] Card blocked.")
        exit(0)