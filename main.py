from tkinter import *
from tkinter import ttk
import  backend as back
#import sqlite3


 
window = Tk()
window.title('subd')
frame_change = Frame(window, width = 150, height = 150, bg='red') #блок для функционала субд
frame_view = Frame(window, width = 150, height = 150, bg='blue') #блок для просмотра базы данных
frame_change.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_view.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


# порядок элементов
heads = ['id', 'name', 'expenses']
table = ttk.Treeview(frame_view, show='headings') # дерево выполняющее свойство таблицы
table['columns'] = heads # длина таблицы

# заголовки столбцов и их расположение
for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

# добавление из бд в приложение
for row in back.information():
    table.insert('', END, values=row )
table.pack(expand=YES, fill=BOTH)
def create():
    create_table1 = """
    INSERT INTO
  table1 (id, name , expenses)
  VALUES
      ('5', 'kirin', 'yuhj'),
       ('6', 'kirinin', '17'),
        ('7', 'ki', '16'),
         ('8', 'kiri', '1'),
          ('9', 'kir', '22');
           """
    back.cursor.execute(create_table1)  
New=Button(text = 'New',fg='black', bg='yellow',command=create, height=2, width=8)
New.grid(row=1, column=1)


window.mainloop()