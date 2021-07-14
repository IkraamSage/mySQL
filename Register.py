# Ikraam Sage, Class 1
from tkinter import *
from tkinter import messagebox

import mysql.connector as mysql

register = Tk()
register.geometry("600x600")
register.config(bg="black")
register.resizable(width=False, height=False)
register.title("Life Choices Online")
lbl_register = Label(register, text="Registration", fg="white", bg="black", font=("MS sans serif", 18))
lbl_register.place(x=250, y=60)
lbl_details = Label(register, text="Personal Details", fg="white", bg="black", font=("MS sans serif", 18))
lbl_details.place(x=250, y=110)


lbl_name = Label(register, text="Name:",  fg="white", bg="black", font=("MS sans serif", 18))
lbl_name.place(x=250, y=150)
e_name = Entry(register)
e_name.place(x=250, y=200)
lbl_surname = Label(register, text="Surname:", fg="white", bg="black", font=("MS sans serif", 18))
lbl_surname.place(x=250, y=250)
e_surname = Entry(register)
e_surname.place(x=250, y=300)
lbl_idno = Label(register, text="ID Number:", fg="white", bg="black", font=("MS sans serif", 18))
lbl_idno.place(x=250, y=330)
e_id = Entry(register)
e_id.place(x=250, y=360)
lbl_contactno = Label(register, text="Contact No:", fg="white", bg="black", font=("MS sans serif", 18))
lbl_contactno.place(x=250, y=410)
e_contact = Entry(register)
e_contact.place(x=250, y=450)

def register():
        if e_name.get() == "" or e_id.get() == "" or e_contact.get() == "" or e_surname.get() == "":
            messagebox.showerror("Error!", "Please fill in ALL fields")
        else:
            try:
                if len(e_id.get()) != 13 or len(e_contact.get()) != 10:
                    print("Invalid Data Type")
                else:
                    db = mysql.connect(host="127.0.0.1",
                    user="root",
                    password="@Lifechoices1234",
                    database="lifechoices_online")
                    cursor = db.cursor()

                    row = cursor.fetchone()

                    if row is not None:
                        messagebox.showerror("Error", "This user already exists")
                        e_name.delete(0, END)
                        e_surname.delete(0, END)
                        e_id.delete(0, END)
                        e_contact.delete(0, END)

                    else:


                        cursor.execute(
                            "INSERT into Register values(null,'" + e_name.get() + "','" + e_surname.get() + "','" + e_id.get() + "','" + e_contact.get())
                        db.commit()

                        db.close()
#                       message to sya registration was successful AND to aks if the user would like to sign in
                        msg = messagebox.askquestion("REGISTRATION SUCCESSFUL",
                                                     "You are now Registered on Lifechoices Online \n Would you like to Sign In?")
                        if msg == "Yes":
                            register.destroy()
                            import signing_in

                        else:
                            register.destroy()
            except ValueError as x:
                messagebox.showerror("ERROR", "Enter Valid Entries")

        def clear():
            e_name.delete(0, END)
            e_surname.delete(0, END)
            e_id.delete(0, END)
            e_contact.delete(0, END)
            e_name.focus_set()



        def exit():
            msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
            if msg == "yes":
                register.destroy()
            else:
                e_name.delete(0, END)
                e_surname.delete(0, END)
                e_id.delete(0, END)
                e_contact.delete(0, END)



        btn_submit = Button(register, text="Register", fg="white", bg="blue", font="Arial 15 bold", command=register)
        btn_submit.place(x=200, y=500)
        btn_exit = Button(register, text="Exit", bg="red", fg="black", font="Arial 15 bold", command=exit)
        btn_exit.place(x=350, y=500, width=120)


        register.mainloop()
