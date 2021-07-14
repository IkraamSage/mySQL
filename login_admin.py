from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("650x650")
root.title("Admin Login")
root.config(bg="blue")


log_frame = LabelFrame(root, padx=130, pady=40, bg="green")
log_frame.place(x=85, y=145)

font_style = ("Sans Serif", 25, "bold", "italic")
Label(log_frame, text="Admin", bg="black", foreground="#FFFFFF", font=font_style).grid(column=2, row=1)


name_check = False
pass_check = False


def name_text(event):
    name_ent.configure(state=NORMAL)
    name_ent.delete(0, END)
    name_check = True

name_ent = Entry(log_frame)
name_ent.insert(0, 'Username')
name_ent.configure(state=DISABLED)
name_ent.bind('<Button-1>', name_text)
name_ent.grid(column=2, row=3, padx=10, pady=10)

def login():
    my_db = mysql.connector.connect(host="127.0.0.1",
                    user="root",
                    password="@Lifechoices1234",
                    database="lifechoices_online", auth_plugin="mysql_native_password")
    my_cursor = my_db.cursor()
    xy = my_cursor.execute("select * from Admin")

    for i in my_cursor:
        if name_ent.get() == i[0] :
            messagebox.showinfo("Login Successful", "Access Granted")
            root.destroy()
            import admin

            break
        if name_ent.get() == "":
            messagebox.showerror("No Entries", "Please Insert your username")
        elif name_ent.get() != i[0]:
            messagebox.showerror("Access Denied", "Incorrect username")
            name_ent.delete(0, END)



log_btn = Button(log_frame, text="Login", command=login, width=15, bg="#89db33")
log_btn.grid(column=2, row=5, padx=10, pady=10)
root.mainloop()