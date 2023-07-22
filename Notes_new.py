import tkinter as tk
from tkinter import messagebox
import os

def save_notes():
    with open("notes.txt", "w") as file:
        file.write("\n".join(notes_list.get(0, tk.END)))

def add_note():
    note = entry_note.get()
    if note:
        notes_list.insert(tk.END, note)
        entry_note.delete(0, tk.END)
        save_notes()
    else:
        messagebox.showwarning("Пустая заметка", "Введите текст заметки!")

def delete_note():
    selected_index = notes_list.curselection()
    if selected_index:
        notes_list.delete(selected_index)
        save_notes()
    else:
        messagebox.showwarning("Нет выбранной заметки", "Выберите заметку для удаления!")

def edit_note():
    selected_index = notes_list.curselection()
    if selected_index:
        selected_note = notes_list.get(selected_index)
        entry_note.delete(0, tk.END)
        entry_note.insert(0, selected_note)
        notes_list.delete(selected_index)
        save_notes()
    else:
        messagebox.showwarning("Нет выбранной заметки", "Выберите заметку для редактирования!")

def clear_entry():
    entry_note.delete(0, tk.END)

def load_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = file.read().splitlines()
        notes_list.delete(0, tk.END)
        for note in notes:
            notes_list.insert(tk.END, note)

root = tk.Tk()
root.title("Заметки")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

notes_list = tk.Listbox(frame, width=50, height=10)
notes_list.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame, command=notes_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
notes_list.config(yscrollcommand=scrollbar.set)

entry_note = tk.Entry(root, width=50)
entry_note.pack(pady=5)

btn_add = tk.Button(root, text="Добавить", command=add_note)
btn_add.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(root, text="Удалить", command=delete_note)
btn_delete.pack(side=tk.LEFT)

btn_edit = tk.Button(root, text="Редактировать", command=edit_note)
btn_edit.pack(side=tk.LEFT)


load_notes()

root.mainloop()
