from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import backend as back 

class Main:

    def __init__(self, master):
        self.master = master

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        self.logf = None
        self.regf = None
        self.listf = None

        self.db = None
        self.c = None

        self.widgets()

        back.db_users_create()
        self.db_connection()

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


    def login(self):
        if self.verify_fields(self.username.get(), self.password.get()):
            find_user = 'SELECT * FROM user WHERE username = ? and password = ?'
            self.c.execute(find_user, [(self.username.get()), (self.password.get())])
            result = self.c.fetchall()

            if result:
                self.logf.pack_forget()
                ms.showinfo('Sucesso', f'Login feito com sucesso. Bem-vindo {self.username.get()}.')
                self.list()

            else:
                ms.showerror('Erro no login', 'Usuário não encontrado.')

    def new_user(self):
        if self.verify_fields(self.n_username.get(), self.n_password.get()):
            find_user = 'SELECT username FROM user WHERE username = ?'
            self.c.execute(find_user, [(self.n_username.get())])

            if self.c.fetchall():
                ms.showerror('Erro ao registrar', 'Usuário já existe, tente um diferente.')
            else:
                ms.showinfo('Sucesso', 'Conta criada!')
                self.log()

            back.db_insert(self.n_username.get(), self.n_password.get())

    def log(self):
        self.username.set('')
        self.password.set('')
        self.regf.pack_forget()
        self.logf.pack()

    def dlog(self):
        self.username.set('')
        self.password.set('')
        self.listf.pack_forget()
        self.logf.pack()
        ms.showinfo('Deslogado', f'Deslogou com sucesso')

    def reg(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.regf.pack()

    def list(self):
        self.logf.pack_forget()
        self.listf.pack()

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

        # List Frame
        self.listf = Frame(self.master, pady=25)

        Label(self.listf, text='Lista de Souls Like zerados.', pady=5).grid(row=0, column=0)
        self.menu_bttn = Menubutton(self.listf, text='Lista de Jogos', relief=RAISED)
        self.menu_bttn.grid(row=1, column=0)

        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()
        self.var4 = BooleanVar()
        self.var5 = BooleanVar()

        self.menu1 = Menu(self.menu_bttn, tearoff=0)
        self.menu1.add_checkbutton(label='Dark Souls I', variable=self.var1)
        self.menu1.add_checkbutton(label='Dark Souls II', variable=self.var2)
        self.menu1.add_checkbutton(label='Dark Souls III', variable=self.var3)
        self.menu1.add_checkbutton(label='Elden Ring', variable=self.var4)
        self.menu1.add_checkbutton(label='Bloodborne', variable=self.var5)

        self.menu_bttn['menu'] = self.menu1

        self.frame_bttn = Frame(self.listf, pady=30)
        self.frame_bttn.grid()
        Button(self.frame_bttn, text='Deslogar', width=25, relief=RAISED, command=self.dlog).grid(row=4, column=0)

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