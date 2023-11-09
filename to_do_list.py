import tkinter as tk

class todolist:
    def __init__(self):
        # creating a empty list to store the tasks
        self.tasks = []
        #creating a window 
        self.root = tk.Tk()
        self.root.title("To Do List")
        
        #creating a input field to enter the tasks
        self.task_entry = tk.Entry(self.root)
        #position of the field
        self.task_entry.pack(side = tk.LEFT, padx = 10)
        
        #button to add the tasks
        self.add_button = tk.Button(self.root, text = "ADD TASK", command = self.add_task)
        self.add_button.pack(side = tk.LEFT, padx = 10)
        
        #field to display the tasks
        self.task_list = tk.Listbox(self.root)
        self.task_list.pack(side = tk.LEFT, padx = 10)
        
        #delete button to remove tasks from display field
        self.delete_button = tk.Button(self.root, text = "DELETE TASK", command = self.delete_task)
        self.delete_button.pack(side = tk.LEFT, padx = 10)
        
        #responsible for the movement of mouse, responsiveness of the gui
        #responsible for handling human interaction
        self.root.mainloop()
        
    
    #function to add tasks
    def add_task(self):
        #to get the tasks entered in entry field
        task = self.task_entry.get()
        if task: #checks the presence of text in the entry field
            self.tasks.append(task) #adds the task to empty list created
            self.task_list.insert(tk.END, task)#inserts the task to the display field at the end
            self.task_entry.delete(0, tk.END)#removes the text in the entry field
            
            
    #function to delete the tasks
    def delete_task(self):
        selection = self.task_list.curselection()#it  selects the task in the display field which need to be deleted
        if selection:#check whether any task is selected
            index = selection[0]#selects the first task that is selected to delete when multiple tasks are selected
            del self.tasks[index]#seleects the selected task from the list
            self.task_list.delete(index)#deletes the task from display field
            
if __name__ == '__main__':
    app = todolist()  

