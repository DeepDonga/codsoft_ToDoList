import tkinter as tk

class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List")

        self.window.geometry("400x300") 
         
        self.tasks = {} 
             
        self.task_label = tk.Label(self.window, text="Task:").grid(row=0, column=0)

        self.task_entry = tk.Entry(self.window,width=30)
        self.task_entry.grid(row=0, column=1)

        #Add Button
        self.add_button = tk.Button(self.window, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        # Delete Button
        self.delete_button = tk.Button(self.window, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=0, column=3) 
        
        # Update Button
        self.update_button = tk.Button(self.window, text="Update", command=self.update_task)
        self.update_button.grid(row=1, column=2)
        
        self.task_list = tk.Listbox(self.window,width=30,height=15)
        self.task_list.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            
    def delete_task(self):
        selected_index  = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_list.delete(index)
            
    def update_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_entry.get()
            if new_task:
                self.task_list.delete(index)
                self.task_list.insert(index, new_task)
                self.task_entry.delete(0, tk.END) 
                
if __name__ == "__main__":
    app = ToDoListApp()