from logo import logo
from morse_code import encrypt, decrypt



is_on = True

def morse_code_run():
    """Runs user interface to converts text to morse code and back into text"""
    print(logo)
    print("Welcome to the MorseCode translator")
    global is_on
    is_continuing = True
    while is_on:
        option = input("Please choose an option (encrypt/decrypt): ").lower()

        if option in ["encrypt", "decrypt"]:
            while is_continuing:
                user_input = input("Please enter text: ")
                translate = encrypt(user_input) if option == "encrypt" else decrypt(user_input)
                action = "encoded" if option == "encrypt" else "decoded"
                print(f"Here is the {action} result: {translate}\n")
                while True:
                    continue_running = input(f"Would you like another message {action}. (yes/no): ").lower()

                    if continue_running == "no":
                        print("You have ended the program. Have a nice day")
                        is_continuing =  False
                        is_on = False
                        break
                    elif continue_running == "yes":
                        break
                    else:
                        print(f"Please type 'yes' or 'no' to continue.")



        elif option == "exit":
            print("You have ended the program. Have a nice day")
            is_on = False

        else:
            print("Please type 'encrypt', 'decrypt' or 'exit' to continue.\n")


morse_code_run()
