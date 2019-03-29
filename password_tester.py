from tkinter import *

def main():
    initiate();

def initiate():
    x = False
    while x == False:
        u_input = input("Start Testing? (y/n): ")
        if (u_input == "y"):
            break;
    #passwords = generate_passwords();
    passwords = ["piece", "of", "shit"]
    show_passwords(passwords)
    print("\nPlease retype to confirm passwords...")
    email_check(passwords)

def show_passwords(passwords):
    root = Tk()
    email = Label(root, text="Email Password: " + passwords[0])
    banking = Label(root, text="Banking Password: " + passwords[1])
    shopping = Label(root, text="Shopping Password: " + passwords[2])
    email.pack(); banking.pack(); shopping.pack(); root.mainloop()

def email_check(passwords):
    attempt = input("Email Password :")
    if passwords[0] == attempt:
        return
    else:
        choice = input("\nIncorrect Password! \n    1.Try Again? \n    2.View Passwords.\n")
        if choice == "1":
            email_check(passwords)
        elif choice == "2":
            show_passwords(passwords)
            email_check(passwords)
main();
