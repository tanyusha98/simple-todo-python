tasks = []
def add_task(task):
    tasks.append({"task": task, "done": False})

def list_tasks():
    return tasks

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

if __name__ == "__main__":
    add_task("Learn GitHub")
    add_task("Write code")
    complete_task(0)
    print(list_tasks())
