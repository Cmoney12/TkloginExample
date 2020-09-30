import sqlite3
from tkinter import Tk, Label, Button, Entry, Frame, Toplevel


class Login:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        master.title("Login")

        self.label = Label(master, text="Login")
        self.label.place(x=250, y=100)

        self.user_name = Entry(master)
        self.user_name.place(x=200, y=150)

        self.user_pass = Entry(master)
        self.user_pass.place(x=200, y=200)

        self.loginbutton = Button(master, text="Login", command=lambda: self.Login())
        self.loginbutton.place(x=240, y=250)

        self.registerbutton = Button(master, text="Register", command=lambda: self.Register())
        self.registerbutton.place(x=240, y=300)

        self.label2 = Label(master)
        self.label2.place(x=240, y=350)

    def Register(self):
        conn = sqlite3.connect("Your_Database_name.sqlite")
        try:
            c = conn.cursor()
        except sqlite3.Error as e:
            print(e)

        c.execute('SELECT * FROM user_login WHERE (username=? AND password=?)', (
            self.user_name.get(), self.user_pass.get()))
        entry = c.fetchone()

        if entry is None:
            c.execute('INSERT INTO user_login(username, password) VALUES (?, ?);', (
                self.user_name.get(), self.user_pass.get()))
        elif self.user_pass.get() is None or self.user_pass.get() is None:
            print('None')
        else:
            print("You are already registered")

        conn.commit()
        conn.close()

    def Login(self):
        conn = sqlite3.connect("my_database 1.sqlite")
        try:
            c = conn.cursor()
        except sqlite3.Error as e:
            print(e)
        c.execute('SELECT * FROM user_login WHERE (username=? AND password=?)', (
            self.user_name.get(), self.user_pass.get()))
        entry = c.fetchone()
        if entry is None:
            self.label2.config(text="Sorry that is incorrect")
        elif self.user_pass.get() is None or self.user_pass.get() is None:
            self.label2.config(text="You must enter text")
        else:
            self.master.withdraw()
            self.Login = Toplevel(self.master)
            self.app = Window2(self.Login)


class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk()
    root.geometry('500x500')
    app = Login(root)
    root.mainloop()


if __name__ == '__main__':
    main()
