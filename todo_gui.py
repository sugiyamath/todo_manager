import tkinter as tk
import todo


def refresh_listbox():
    listbox.delete(0, tk.END)
    for item in todo.TODO_LIST:
        listbox.insert(tk.END, item)


def refresh_history():
    history.delete(0, tk.END)
    for item in todo.HISTORY[::-1]:
        history.insert(tk.END, item)


def add_item():
    item = entry.get()
    if item:
        todo.add_todo(item)
        entry.delete(0, tk.END)
        refresh_listbox()


def do_item():
    try:
        index = listbox.curselection()[0]
        todo.do_todo(index)
        refresh_listbox()
        refresh_history()
    except:
        pass


def done_item():
    try:
        index = listbox.curselection()[0]
        todo.done_todo(index)
        refresh_listbox()
        refresh_history()
    except:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("TODO List")

    entry = tk.Entry(root, width=50)
    entry.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    add_button = tk.Button(button_frame, text="Add", command=add_item)
    add_button.pack(side=tk.LEFT)

    do_button = tk.Button(button_frame, text="Do", command=do_item)
    do_button.pack(side=tk.LEFT)

    done_button = tk.Button(button_frame, text="Done", command=done_item)
    done_button.pack(side=tk.LEFT)

    listbox = tk.Listbox(root, width=50)
    listbox.pack()

    history_label = tk.Label(root, text="history")
    history_label.pack()

    history = tk.Listbox(root, width=50)
    history.pack()

    todo.load_todo()
    todo.load_history()
    refresh_listbox()
    refresh_history()

    root.mainloop()
