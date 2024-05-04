from datetime import datetime

TODO_LIST = []
HISTORY = []
CURRENT_TASK = None
TODO_FILE = "todo.txt"
DATA_FILE = "todo_history.txt"

def load_todo():
    with open(TODO_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                TODO_LIST.append(line)

def save_todo():
    with open(TODO_FILE, "w") as f:
        for x in TODO_LIST:
            f.write(x+'\n')

def load_history():
    with open(DATA_FILE) as f:
        for line in f:
            line = line.strip()
            line = line.split("\t")
            if line:
                assert len(line) == 3
                HISTORY.append(line)

def save_history():
    with open(DATA_FILE, "w") as f:
        for x in HISTORY:
            f.write('\t'.join(x)+'\n')

def add_todo(todo):
    TODO_LIST.append(todo)
    save_todo()

def list_todo():
    return "\n".join(f"{i}: {todo}" for i, todo in enumerate(TODO_LIST))

def do_todo(i):
    HISTORY.append(["do", str(datetime.now().ctime()), TODO_LIST[i]])
    save_history()

def done_todo(i):
    HISTORY.append(["done", str(datetime.now().ctime()), TODO_LIST[i]])
    del TODO_LIST[i]
    save_history()
    save_todo()

def command(cmd):
    try:
        if cmd[0] == "add":
            add_todo(cmd[1])
        elif cmd[0] == "list":
            print(list_todo())
        elif cmd[0] == "do":
            do_todo(int(cmd[1]))
        elif cmd[0] == "done":
            done_todo(int(cmd[1]))
    except IndexError:
        print("./todo.py <cmd> <param>")
        print("  <cmd>: add, list, do, done")
        print("    add <todo name>")
        print("    list")
        print("    do <todo ID>")
        print("    done <todo ID>")
    
if __name__ == "__main__":
    import sys
    load_todo()
    load_history()
    command(sys.argv[1:])
