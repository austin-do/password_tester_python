from tkinter import *
import time
import random

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

    showpassbtn = Button(rootA, text='Show Passwords', fg='red', command=Show)
    showpassbtn.grid(column=2,columnspan=2, sticky=E)
    roots.destroy()
    rootA.mainloop()

def CheckLogin():
    global r
    if email_pass_attempt.get() == passwords[0] and bank_pass_attempt.get() == passwords[1] and shop_pass_attempt.get() == passwords[2]:
        r = Tk()
        r.title(':D')

        r.geometry('150x100')
        rlbl = Label(r, text='\n Good Job.')
        rlbl.grid(row=1,column=1)
        continuebtn = Button(r, text="Continue", command=Test)
        continuebtn.grid(column=2,row=2, sticky=E)
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x100')
        rlbl = Label(r, text='\n[!] Invalid Password Detected.')
        rlbl.pack()
        r.mainloop()

def Test():
    #r.destroy()
    #rootA.destroy()
    order = RandomizeOrder()
    for i in order:
        t1 = time.strftime('%H:%M:%S')
        options[i]()
        t2 = time.strftime('%H:%M:%S')
        #print(t2-t1)


def TestEmail():
    global root
    global email_pass_attempt
    global failcount
    failcount = 0
    root = Tk()
    email_pass = Label(root, text='Email: ')
    email_pass_attempt = Entry(root, show='*')
    email_pass.grid(row=1, sticky=W)
    email_pass_attempt.grid(row=1, column=1)
    continuebtn = Button(root, text="Continue", command=CheckEmail)
    continuebtn.grid(column=2,row=2, sticky=E)
    root.mainloop()

def TestBank():
    global root
    global bank_pass_attempt
    global failcount
    failcount = 0
    root = Tk()
    bank_pass = Label(root, text='Banking: ')
    bank_pass_attempt = Entry(root, show='*')
    bank_pass.grid(row=1, sticky=W)
    bank_pass_attempt.grid(row=1, column=1)
    continuebtn = Button(root, text="Continue", command=CheckBank)
    continuebtn.grid(column=2,row=2, sticky=E)
    root.mainloop()

def TestShop():
    global root
    global shop_pass_attempt
    global failcount
    failcount = 0
    root = Tk()
    shop_pass = Label(root, text='Shopping: ')
    shop_pass_attempt = Entry(root, show='*')
    shop_pass.grid(row=1, sticky=W)
    shop_pass_attempt.grid(row=1, column=1)
    continuebtn = Button(root, text="Continue", command=CheckShop)
    continuebtn.grid(column=2,row=2, sticky=E)
    root.mainloop()

def CheckEmail():
    global r
    if email_pass_attempt.get() == passwords[0]:
        Quit()
    else:
        global failcount
        failcount = failcount + 1
        if failcount == 3:
            r = Tk()
            r.title('D:')
            r.geometry('400x50')
            rlbl = Label(r, text='\nYou have FAILED.')
            rlbl.pack()
            r.mainloop()
            Restart()

        else:
            r = Tk()
            r.title('D:')
            r.geometry('400x50')
            rlbl = Label(r, text='\n[!] Invalid Password: ' + str(3-failcount) + ' Attempt(s) Remaining')
            rlbl.pack()
            r.mainloop()

def CheckBank():
    global r
    if bank_pass_attempt.get() == passwords[1]:
        Quit()
    else:
        global failcount
        failcount = failcount + 1
        if failcount == 3:
            r = Tk()
            r.title('D:')
            r.geometry('400x50')
            rlbl = Label(r, text='\nYou have FAILED.')
            rlbl.pack()
            r.mainloop()
            Restart()

        else:
            r = Tk()
            r.title('D:')
            r.geometry('400x50')
            rlbl = Label(r, text='\n[!] Invalid Password: ' + str(3-failcount) + ' Attempt(s) Remaining')
            rlbl.pack()
            r.mainloop()

def CheckShop():
    global r
    if shop_pass_attempt.get() == passwords[2]:
        Quit()
    else:
        global failcount
        failcount = failcount + 1
        if failcount > 2:
            r = Tk()
            r.title('D:')
            r.geometry('400x50')
            rlbl = Label(r, text='\nYou have FAILED.')
            rlbl.pack()
            r.mainloop()
            Restart()

        else:
            r = Tk()
            r.title('D:')
            r.geometry('400x50')
            rlbl = Label(r, text='\n[!] Invalid Password: ' + str(3-failcount) + ' Attempt(s) Remaining')
            rlbl.pack()
            r.mainloop()

def RandomizeOrder():
    i = 0
    arr = [1,2,3]
    random.shuffle(arr)
    return arr


def Show():
    Show_Passwords(passwords)

def Destroy_Roots():
    roots.destroy()

def Quit():
    root.destroy()

def Restart():
    root.destroy()
    root.update()
    Main()

def Generate_Passwords():
    global passwords
    passwords = ["god", "fucking", "damn it"]


options = {1 : TestEmail,
                  2 : TestBank,
                  3 : TestShop
}

def Main():
    Generate_Passwords()
    #Show_Passwords(passwords)
    Test()

Main()
