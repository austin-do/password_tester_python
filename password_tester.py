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
    print("Please retype to confirm passwords.")

def show_passwords(passwords):
    root = Tk()
    email = Label(root, text="Email Password: " + passwords[0])
    banking = Label(root, text="Banking Password: " + passwords[1])
    shopping = Label(root, text="Shopping Password: " + passwords[2])
    email.pack()
    banking.pack()
    shopping.pack()
    root.mainloop()

main();
