from tkinter import *
from tkinter import messagebox as ms
import Backend as back

class Main:
    
    def __init__(self, master):
        self.master = master

        self.selected_tuple = None

        self.frame = None

        self.name = StringVar()
        self.price = IntVar()

        self.e1 = None
        self.e2 = None
        self.listbox = None

        self.db = None
        self.c = None

        self.widgets()

        back.db_items_create()
        self.view()

    # Functions
    def selected_row(self, event):
        global selected_tuple
        index = self.listbox.curselection()[0]

        self.selected_tuple = self.listbox.get(index)

        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])

    def view(self):
        self.listbox.delete(0, END)
        for row in back.db_view():
            self.listbox.insert(END, row)

    def add(self):
        back.db_insert(self.name.get(), self.price.get())
        
        self.listbox.delete(0, END)
        self.listbox.insert(END, (self.name.get(), self.price.get()))

        ms.showinfo('Sucesso', 'Item criado!')

        # Clear entrys
        self.e1.delete(0, END)
        self.e2.delete(0, END)

        self.view()

    def delete(self):
        back.db_delete(self.selected_tuple[0])
        ms.showinfo('Sucesso', 'Item deletado!')

        # Clear Entrys
        self.e1.delete(0, END)
        self.e2.delete(0, END)

        self.view()

    def update(self):
        back.db_update(self.selected_tuple[0], self.name.get(), self.price.get())
        ms.showinfo('Sucesso', 'Item atualizado!')

        # Clear Entrys
        self.e1.delete(0, END)
        self.e2.delete(0, END)

        self.view()

    # Frontend
    def widgets(self):
        self.frame = Frame(self.master, pady=25)

        # CRUD 
        Label(self.frame, text='Name:').grid(sticky=W)
        self.e1 = Entry(self.frame, textvariable=self.name)
        self.e1.grid(row=0, column=1)

        Label(self.frame, text='Price:', pady=5).grid(sticky=W)
        self.e2 = Entry(self.frame, textvariable=self.price)
        self.e2.grid(row=1, column=1)

        Button(self.frame, text='Criar', command=self.add).grid(row=2, column=1)
        Button(self.frame, text='Deletar', command=self.delete).grid(row=2, column=2)
        Button(self.frame, text='Atualizar', command=self.update).grid(row=2, column=3)

        # List
        Label(self.frame, text='Itens da loja:').grid(sticky=W)

        self.listbox = Listbox(self.frame, height=10)
        self.listbox.grid(row=4, column=0)
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.grid(row=4, column=1)

        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)

        self.listbox.bind('<<ListboxSelect>>', self.selected_row)

        self.frame.pack()

if __name__ == '__main__':
    root = Tk()
    root.title('Trabalho')
    width = 400
    height = 400

    running = Main(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    root.mainloop()