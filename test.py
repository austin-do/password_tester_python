from tkinter import *
import time

def Show_Passwords(passwords):
    global roots

    roots = Tk()
    roots.title('Passwords')
    label = Label(roots, text='Here are your passwords\n')
    label.grid(row=0, column=0, sticky=E)
    email_pass = Label(roots, text='Email: ' + passwords[0])
    bank_pass = Label(roots, text='Banking: ' + passwords[1])
    shop_pass = Label(roots, text='Shopping: ' + passwords[2])

    email_pass.grid(row=1, column=0, sticky=W)
    bank_pass.grid(row=2, column=0, sticky=W)
    shop_pass.grid(row=3, column=0, sticky=W)

    try:
        if rootA:
            signupButton = Button(roots, text='Ready', command=Destroy_Roots)
    except:
        signupButton = Button(roots, text='Ready', command=Confirm)

    signupButton.grid(row=4, column=2, columnspan=2, sticky=W)
    roots.mainloop()

def Confirm():
    global email_pass_attempt
    global bank_pass_attempt
    global shop_pass_attempt
    global rootA

    rootA = Tk()
    rootA.title('Confirmation')

    label = Label(rootA, text='Please Confirm Passwords\n')
    label.grid(columnspan=3,sticky=W)
    email_pass = Label(rootA, text='Email: ')
    bank_pass = Label(rootA, text='Banking: ')
    shop_pass = Label(rootA, text='Shopping: ')
    email_pass.grid(row=1, sticky=W)
    bank_pass.grid(row=2, sticky=W)
    shop_pass.grid(row=3, sticky=W)

    email_pass_attempt = Entry(rootA, show='*')
    bank_pass_attempt = Entry(rootA, show='*')
    shop_pass_attempt = Entry(rootA, show='*')
    email_pass_attempt.grid(row=1, column=1)
    bank_pass_attempt.grid(row=2, column=1)
    shop_pass_attempt.grid(row=3,column=1)

    checkbtn = Button(rootA, text='Ready', command=CheckLogin)
    checkbtn.grid(column=2,columnspan=2, sticky=E)

    showpassbtn = Button(rootA, text='Show Passwords', fg='red', command=Show) # This makes the deluser button. blah go to the deluser def.
    showpassbtn.grid(column=2,columnspan=2, sticky=E)
    roots.destroy()
    rootA.mainloop()

def CheckLogin():
    global r
    if email_pass_attempt.get() == passwords[0] and bank_pass_attempt.get() == passwords[1] and shop_pass_attempt.get() == passwords[2]:
        r = Tk()
        r.title(':D')

        r.geometry('150x50')
        rlbl = Label(r, text='\n Good Job.')
        rlbl.grid(row=1,column=1)
        continuebtn = Button(r, text="Continue", command=Test)
        continuebtn.grid(column=2,row=2, sticky=E)
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

def Test():
    #r.destroy()
    #rootA.destroy()
    order = RandomizeOrder()

    for i in order:
        print("start:")
        print(time.strftime('%H:%M:%S'))
        options[i]()
        print("end:")
        print(time.strftime('%H:%M:%S'))


def TestEmail():
    global root
    root = Tk()
    email_pass = Label(root, text='Email: ')
    email_pass_attempt = Entry(root, show='*')
    email_pass.grid(row=1, sticky=W)
    email_pass_attempt.grid(row=1, column=1)
    continuebtn = Button(root, text="Continue", command=Quit)
    continuebtn.grid(column=2,row=2, sticky=E)
    root.mainloop()

def BankEmail():
    global root
    root = Tk()
    bank_pass = Label(root, text='Banking: ')
    bank_pass_attempt = Entry(root, show='*')
    bank_pass.grid(row=1, sticky=W)
    bank_pass_attempt.grid(row=1, column=1)
    continuebtn = Button(root, text="Continue", command=Quit)
    continuebtn.grid(column=2,row=2, sticky=E)
    root.mainloop()

def ShopEmail():
    global root
    root = Tk()
    shop_pass = Label(root, text='Shopping: ')
    shop_pass_attempt = Entry(root, show='*')
    shop_pass.grid(row=1, sticky=W)
    shop_pass_attempt.grid(row=1, column=1)
    continuebtn = Button(root, text="Continue", command=Quit)
    continuebtn.grid(column=2,row=2, sticky=E)
    root.mainloop()

def RandomizeOrder():
    i = 0
    arr = [1,2,3]
    return arr

def Show():
    Show_Passwords(passwords)

def Destroy_Roots():
    roots.destroy()

def Quit():
    root.destroy()

def Generate_Passwords():
    global passwords
    passwords = ["god", "fucking", "damn it"]


options = {1 : TestEmail,
                  2 : BankEmail,
                  3 : ShopEmail
}
#Generate_Passwords()
#Show_Passwords(passwords)
Test()
