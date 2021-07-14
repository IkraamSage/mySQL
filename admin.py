import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("180x450")
root.title("Admin")
root.config(bg="blue")

clicked = True
un_clicked = False


table = ttk.Treeview(root)
my_db = mysql.connector.connect(host="127.0.0.1",
                    user="root",
                    password="@Lifechoices1234",
                    database="lifechoices_online", auth_plugin="mysql_native_password")
my_cursor = my_db.cursor()


def table_reg():
    if clicked:
        remove_btn.config(state=NORMAL)
        my_cursor.execute("select * from Register")

        table["show"] = "headings"

        style = ttk.Style(root)
        style.theme_use("clam")

        style.configure(".", font=("sans serif", 11))
        style.configure("Treeview.Heading", foreground="#89db33", bg="#0F0F0F", font=("sans serif", 11, "bold"))
        table["columns"] = ("ID", "Name", "Surname", "UserName", "Role", "Password", "Cell")

        table.column("ID", width=150, minwidth=150, anchor=tkinter.CENTER)
        table.column("Name", width=150, minwidth=150, anchor=tkinter.CENTER)
        table.column("Surname", width=150, minwidth=150, anchor=tkinter.CENTER)
        table.column("UserName", width=100, minwidth=100, anchor=tkinter.CENTER)
        table.column("Role", width=100, minwidth=100, anchor=tkinter.CENTER)
        table.column("Password", width=150, minwidth=150, anchor=tkinter.CENTER)
        table.column("Cell", width=120, minwidth=120, anchor=tkinter.CENTER)


        table.heading("ID", text="ID Number", anchor=tkinter.CENTER)
        table.heading("Name", text="Name", anchor=tkinter.CENTER)
        table.heading("Surname", text="Surname", anchor=tkinter.CENTER)
        table.heading("UserName", text="Username", anchor=tkinter.CENTER)
        table.heading("Role", text="Role", anchor=tkinter.CENTER)
        table.heading("Password", text="Password", anchor=tkinter.CENTER)
        table.heading("Cell", text="Cell Number", anchor=tkinter.CENTER)


        i = 0
        for row in my_cursor:
            table.insert("", i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            i = i + 1

        scrollh = ttk.Scrollbar(root, orient="horizontal")
        scrollh.configure(command=table.xview)
        table.configure(xscrollcommand=scrollh.set)
        scrollh.pack(fill=X, side=BOTTOM)

        scrollv = ttk.Scrollbar(root, orient="vertical")
        scrollv.configure(command=table.yview)
        table.configure(yscrollcommand=scrollv.set)
        scrollv.pack(fill=Y, side=RIGHT)

        table.pack(side=BOTTOM)

    if un_clicked:
        table.destroy()


rt_btn = Button(root, text="Registered Users", width=14, foreground="white", bg="#0F0F0F", command=table_reg)
rt_btn.place(x=10, y=100)


def add():
    add_frame = LabelFrame(root, width=450, height=280, bg="#89db33")
    add_frame.place(x=160, y=100)
    Label(add_frame, text="ID Number", bg="#89db33", foreground="#0F0F0F").place(x=10, y=10)
    Label(add_frame, text="Name", bg="#89db33", foreground="#0F0F0F").place(x=10, y=60)
    Label(add_frame, text="Surname", bg="#89db33", foreground="#0F0F0F").place(x=10, y=110)
    Label(add_frame, text="Username", bg="#89db33", foreground="#0F0F0F").place(x=10, y=160)
    Label(add_frame, text="Role", bg="#89db33", foreground="#0F0F0F").place(x=230, y=10)
    Label(add_frame, text="Password", bg="#89db33", foreground="#0F0F0F").place(x=10, y=210)
    Label(add_frame, text="Cell Number", bg="#89db33", foreground="#0F0F0F").place(x=230, y=60)


    id_ent = Entry(add_frame, width=24)
    id_ent.place(x=10, y=30)
    name_ent = Entry(add_frame, width=24)
    name_ent.place(x=10, y=80)
    surname_ent = Entry(add_frame, width=24)
    surname_ent.place(x=10, y=130)
    username_ent = Entry(add_frame, width=24)
    username_ent.place(x=10, y=180)
    password_ent = Entry(add_frame, width=24)
    password_ent.place(x=10, y=230)
    role_ent = Entry(add_frame, width=24)
    role_ent.place(x=230, y=30)
    cell_ent = Entry(add_frame, width=24)
    cell_ent.place(x=230, y=80)

    def register():
        if id_ent.get() == "" or name_ent.get() == "" or surname_ent.get() == "" or username_ent.get() == "" or cell_ent.get() == "":
            messagebox.showerror("No Entries", "Please fill all fields")
        else:
            messagebox.showinfo("Successful", "You have registered a new user")

            insert = "INSERT INTO Register (ID, Name, Surname, UserName, Role) VALUES (%s, %s, %s, %s, %s)"
            entries = (id_ent.get(), name_ent.get(), surname_ent.get(), username_ent.get(), role_ent.get())
            my_cursor.execute(insert, entries)
            my_db.commit()
            add_frame.destroy()

    reg_btn = Button(add_frame, text="Register", command=register, fg="white", bg="#0F0F0F", width=21)
    reg_btn.place(x=230, y=220)


add_btn = Button(root, text="Add User", command=add, width=14, fg="white", bg="#0F0F0F")
add_btn.place(x=10, y=150)


def remove():
    r = table.selection()[0]
    table.delete(r)
    messagebox.showinfo("User removed", "Successfully removed a User")


remove_btn = Button(root, text="Remove User", command=remove, state=DISABLED, width=14, fg="#89db33", bg="#0F0F0F")
remove_btn.place(x=10, y=200)
edit_btn = Button(root, text="Edit User", command=None, width=14, fg="#89db33", bg="#0F0F0F")
edit_btn.place(x=10, y=250)


def table_log():

    my_cursor.execute("select * from Log")

    table2 = ttk.Treeview(root)
    table2["show"] = "headings"

    style2 = ttk.Style(root)
    style2.theme_use("clam")

    style2.configure(".", font=("sans serif", 11))
    style2.configure("Treeview.Heading", foreground="#89db33", bg="#0F0F0F", font=("sans serif", 11, "bold"))
    table2["columns"] = ("UserName", "Password", "Date", "TimeIn", "TimeOut")

    table2.column("UserName", width=150, minwidth=150, anchor=tkinter.CENTER)
    table2.column("Password", width=150, minwidth=150, anchor=tkinter.CENTER)
    table2.column("Date", width=130, minwidth=130, anchor=tkinter.CENTER)
    table2.column("TimeIn", width=100, minwidth=100, anchor=tkinter.CENTER)
    table2.column("TimeOut", width=100, minwidth=100, anchor=tkinter.CENTER)

    table2.heading("UserName", text="Username", anchor=tkinter.CENTER)
    table2.heading("Password", text="Password", anchor=tkinter.CENTER)
    table2.heading("Date", text="Date", anchor=tkinter.CENTER)
    table2.heading("TimeIn", text="Time In", anchor=tkinter.CENTER)
    table2.heading("TimeOut", text="Time Out", anchor=tkinter.CENTER)

    z = 0
    for row2 in my_cursor:
        table2.insert("", z, text="", values=(row2[0], row2[1], row2[2], row2[3], row2[4]))
        z = z + 1

    scrolls = ttk.Scrollbar(root, orient="horizontal")
    scrolls.configure(command=table2.xview)
    table2.configure(xscrollcommand=scrolls.set)
    scrolls.pack(fill=X, side=BOTTOM)

    scrollu = ttk.Scrollbar(root, orient="vertical")
    scrollu.configure(command=table2.yview)
    table2.configure(yscrollcommand=scrollu.set)
    scrollu.pack(fill=Y, side=RIGHT)

    table2.pack(side=BOTTOM)


log_btn = Button(root, text="Logged Users", command=table_log, width=14, fg="#89db33", bg="#0F0F0F")
log_btn.place(x=10, y=300)


def quite():
    root.destroy()
    import main


q_btn = Button(root, text="Quit", command=quite, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
q_btn.place(x=10, y=350)

root.mainloop()