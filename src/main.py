import customtkinter as ctk
from task_manager import TaskManager

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TaskApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()

        self.title("Gestionnaire de tâches")
        self.geometry("500x400")
        self.resizable(False, False)

        self.task_entry = ctk.CTkEntry(self, width=350, placeholder_text="Ajouter une tâche...")
        self.task_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(self, text="Ajouter", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_frame = ctk.CTkFrame(self, width=450, height=250)
        self.task_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.task_listbox = ctk.CTkScrollableFrame(self.task_frame, width=450, height=200)
        self.task_listbox.pack(fill="both", expand=True)

        self.delete_button = ctk.CTkButton(self, text="Supprimer", fg_color="red", command=self.remove_task)
        self.delete_button.pack(pady=5)

        self.complete_button = ctk.CTkButton(self, text="Marquer Terminé", fg_color="green", command=self.toggle_task)
        self.complete_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.task_manager.add_task(task_text)
            self.task_entry.delete(0, "end")
            self.load_tasks()

    def remove_task(self):
        selected_index = self.get_selected_index()
        if selected_index is not None:
            self.task_manager.remove_task(selected_index)
            self.load_tasks()

    def toggle_task(self):
        selected_index = self.get_selected_index()
        if selected_index is not None:
            self.task_manager.toggle_task(selected_index)
            self.load_tasks()

    def load_tasks(self):
        for widget in self.task_listbox.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.task_manager.tasks):
            task_text = task["task"]
            if task["completed"]:
                task_text = f"✔ {task_text}"
            task_label = ctk.CTkLabel(self.task_listbox, text=task_text)
            task_label.pack(anchor="w", padx=5, pady=2)

    def get_selected_index(self):
        children = self.task_listbox.winfo_children()
        if children:
            return len(children) - 1
        return None

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()