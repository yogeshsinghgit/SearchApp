# Icons made by <a href="https://www.flaticon.com/free-icon/search_639426" title="Dimitry Miroliubov">Dimitry Miroliubov</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
from tkinter.ttk import Combobox
from tkinter.messagebox import askokcancel
import threading
# function ...

def search():
    search_data = ent.get()
    text.delete(0.0, END)
    text.insert(END,'Searching for {}'.format(search_data))
    try:
        data = wiki.summary(search_data, sentences=8)
    except Exception as e:
        data = e

    # delete current data ..
    ent.set('')
    text.delete(0.0,END)
    # insert data
    search_lbl['text'] = "Searching result for :{}".format(search_data)
    text.insert(0.0,data)

def call_search(*args):
    x = threading.Thread(target=search)
    x.start()

def callbackforroot():
    if askokcancel('Quit','Do you really want to quit?'):
        root.quit()



root = Tk()
root.title('Search Application')
root.geometry('320x480')
root.protocol("WM_DELETE_WINDOW",callbackforroot)
root.configure(bg='white')

# test variable
ent = StringVar()
lang = StringVar()
search_entry = Entry(root,width=21,font=('arial',14),bd=2,relief=RIDGE,textvariable=ent)
search_entry.bind('<Return>',call_search)
search_entry.place(x=15,y=20)

img = PhotoImage(file='search.png')

search_button =Button(root,image=img,bd=2,relief=GROOVE,command=call_search)
search_button.place(x=250,y=20)

search_lbl = Label(root,text='Searching result for :  ',font=('arial',12,'bold'),bg='white')
search_lbl.place(x=15,y=70)

text = ScrolledText(root,font=('times',12),bd=4,relief=SUNKEN,wrap =WORD)
text.place(x=15,y=100,height=300,width=300)

lang_list= ['English','Hindi','Gujrati','French','German','Arabic']
lang.set(lang_list[0])
language = OptionMenu(root,*lang_list,lang)
language.place(x=10,y=420)

clear_btn = Button(root,text='Clear',font=('arial',12,'bold'),width=10,
                   command=lambda :text.delete(0.0,END))
clear_btn.place(x=105,y=420)

exit_btn = Button(root,text='Exit',font=('arial',12,'bold'),width=10,command=root.quit)
exit_btn.place(x=200,y=420)


root.mainloop()