
# import modules ..
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
from tkinter.messagebox import askokcancel
import threading

# main gui ..
root = Tk()

def search():
    search_data = ent.get()
    try:
        data = wiki.summary(search_data,sentences=5)
    except Exception as e:
        data = e

    # delete data .
    ent.set('')
    text.delete(0.0,END)

    search_lbl['text'] = 'Searching For : {}'.format(search_data)
    text.insert(END,data)

def call_search(*args):
    x = threading.Thread(target=search)
    x.start()

def call_back(*args):
    if askokcancel('Quit','Are you sure'):
        root.quit()



root.title("Search App")
root.geometry('320x480')
root.configure(bg='white')
root.protocol('WM_DELETE_WINDOW',call_back)


# adding widgets ..
ent = StringVar()
search_entry = Entry(root,width=30,font=('arial',12),bd=2,relief=RIDGE,textvariable=ent)
search_entry.bind('<Return>',call_search)
search_entry.place(x=15,y=20)

search_lbl = Label(root,text="Searching For : ",font=('arial',12,'bold'),bg='white')
search_lbl.place(x=15,y=70)

text = ScrolledText(root,font=('times',12),bd=4,relief=SUNKEN,wrap =WORD)
text.place(x=15,y=100,width=300,height=300)


# Button ...

search_btn = Button(root,text='Search',font=('arial',12,'bold'),width=10,command=search)
search_btn.place(x=10,y=420)

clear_btn = Button(root,text='Clear',font=('arial',12,'bold'),width=10,command=lambda :text.delete(0.0,END))
clear_btn.place(x=105,y=420)

exit_btn = Button(root,text='Exit',font=('arial',12,'bold'),width=10,command=root.quit)
exit_btn.place(x=200,y=420)














root.mainloop()