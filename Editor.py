import tkinter as tk
from tkinter import Tk, Button, Label, Listbox, Text, Menubutton, Menu


class GUI():

    def __init__(self):
        master = Tk()
        master.title('Text Editor', )
        master.geometry('750x500')
        master.resizable(0, 0)

        back = tk.Frame(master=master, bg='gray')
        back.pack_propagate(0)
        back.pack(fill='both', expand = True)

        txt_box = Text(master=back, bg='pale green', fg='black', font=('Helvetica', '12'))
        txt_box.place(height='480', width='750', x='0', y='30')

        file_name = Text(master=back, bg='white')
        file_name.place(x='110', y='5', height='20', width='150')

        file_btn = Menubutton(master=back, bg='gray', text='File')
        file_btn.menu = Menu(file_btn)
        file_btn['menu'] = file_btn.menu
        file_btn.menu.add_command(label='Open', command=lambda: open_file(file_name, txt_box))
        file_btn.place(x='0', y='0', height='30', width='50')

        save_btn = Menubutton(master=back, bg='gray', text='Save')
        save_btn.menu = Menu(save_btn)
        save_btn['menu'] = save_btn.menu
        save_btn.menu.add_command(label='Save')
        save_btn.place(x='50.5', y='0', height='30', width='50')



        master.mainloop()




def open_file(file_name, txt_box):
    input = file_name.get(1.0, 'end-1c')
    with open(input, 'r') as f:
        txt_box.insert('insert', f.read())
    f.close()

def save_file():
    

    pass





if __name__ == '__main__':
    Window = GUI()