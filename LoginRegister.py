from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import Backend as back
import os

class Main:

    def __init__(self, master):
        self.master = master

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        self.logf = None
        self.regf = None

        self.db = None
        self.c = None

        self.widgets()

        back.db_users_create()
        self.db_connection()

    # Database connection
    def db_connection(self):
        with sqlite3.connect('users.sqlite') as self.db:
            self.c = self.db.cursor()

    def db_close(self):
        self.c.close()

    def verify_fields(self, username, password):
        if not username or not password:
            ms.showerror("Campo obrigatório", "Campos não podem estar em branco.")
            return False

        return True

    # Login 
    def login(self):
        if self.verify_fields(self.username.get(), self.password.get()):
            find_user = 'SELECT * FROM user WHERE username = ? and password = ?'
            self.c.execute(find_user, [(self.username.get()), (self.password.get())])
            result = self.c.fetchall()

            if result:
                self.logf.pack_forget()
                ms.showinfo('Sucesso', f'Login feito com sucesso. Bem-vindo {self.username.get()}.')
                root.destroy()

                # Open second window
                current_dir = os.path.dirname(os.path.abspath(__file__))
                SECOND_WINDOW_PATH = os.path.join(current_dir, 'PrincipalPage.py')
                os.system(f'python {SECOND_WINDOW_PATH}')

            else:
                ms.showerror('Erro no login', 'Usuário não encontrado.')

    # Register
    def new_user(self):
        if self.verify_fields(self.n_username.get(), self.n_password.get()):
            find_user = 'SELECT username FROM user WHERE username = ?'
            self.c.execute(find_user, [(self.n_username.get())])

            if self.c.fetchall():
                ms.showerror('Erro ao registrar', 'Usuário já existe, tente um diferente.')
            else:
                ms.showinfo('Sucesso', 'Conta criada!')
                self.log()

            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            self.c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
            self.db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.regf.pack_forget()
        self.logf.pack()

    def reg(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.regf.pack()

    # Frontend
    def widgets(self):
        # Login Frame
        self.logf = Frame(self.master, pady=25)

        Label(self.logf, text='Usuário', pady=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, width=40).grid(row=0, column=1)


        Label(self.logf, text='Senha', pady=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, width=40, show='*').grid(row=1, column=1)

        Button(self.logf, text='Login', width=25, bg='blue', fg='white', relief=FLAT, command=self.login).grid(row=2, column=1)
        Button(self.logf, text='Não tem uma conta? Clique aqui!', width=25, fg='blue', relief=FLAT, command=self.reg).grid(row=3, column=1)

        self.logf.pack()

        # Register Frame
        self.regf = Frame(self.master, pady=25)

        Label(self.regf, text='Usuário', pady=5).grid(sticky=W)
        Entry(self.regf, textvariable=self.n_username, width=40).grid(row=0, column=1)


        Label(self.regf, text='Senha', pady=5).grid(sticky=W)
        Entry(self.regf, textvariable=self.n_password, width=40, show='*').grid(row=1, column=1)

        Button(self.regf, text='Registrar-se', width=25, bg='blue', fg='white', relief=FLAT, command=self.new_user).grid(row=2, column=1)
        Button(self.regf, text='Voltar a tela de login', width=25, fg='blue', relief=FLAT, command=self.log).grid(row=3, column=1)

if __name__ == '__main__':
    root = Tk()
    root.title('Trabalho')
    width = 400
    height = 200

    running = Main(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    root.mainloop()

    running.db_close()