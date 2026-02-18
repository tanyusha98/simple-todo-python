from todo.todo import add_task, complete_task, list_tasks

def test_add_and_complete():
    add_task("Test task")
    complete_task(0)
    assert list_tasks()[0]["done"] == True
