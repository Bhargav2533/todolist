import tkinter as tk
from tkinter import *
import tkinter.messagebox




#creating the initial window
window=Tk()
#giving a title
window.title("To-Do List APP by Bhargav")


#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="white",fg="black",height=20,width=50,font = "arial")  
listbox_task.pack(side=tkinter.LEFT)

#Scrolldown in case the total list exceeds the size of the given window 
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)









def task_adding():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0,"end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command= add)
    button_temp.pack()
    root1.mainloop()
    

#function to facilitate the delete task from the Listbox
def task_remove():
    #selects the selected item and then deletes it 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])
#Executes this to mark completed 

def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    #update it 
    temp_marked=temp_marked+" ✔"
    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)



#Button widget 
entry_button=Button(window,text="Add task",width=50,fg="white", bg="black",command= task_adding)
entry_button.pack()

delete_button=Button(window,text="Delete selected task",width=50,fg="white",bg="black",command= task_remove )
delete_button.pack()

mark_button=Button(window,text="Mark as completed ",width=50,fg="white",bg="black",command= markcompleted)
mark_button.pack(pady=3)


window.mainloop()
