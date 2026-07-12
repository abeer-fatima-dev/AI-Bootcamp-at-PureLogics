from fastapi import FastAPI
from app.storage import todos
from app.schemas import TodoCreate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI Application!"}

@app.get("/about")
def about():
    return {"message": "This is my first FastAPI Bootcamp Project"}

@app.get("/todos")
def get_todos():
    return todos
    

@app.post("/todos")
def create_todo(todo: TodoCreate):

    todos.append(
        {
            "id": len(todos) + 1,
            "task": todo.task
        }
    )

    return {
        "message": "Task added successfully"
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):

    for todo in todos:

        if todo["id"] == todo_id:
            return todo

    return {"message": "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoCreate):

    for todo in todos:

        if todo["id"] == todo_id:

            todo["task"] = updated_todo.task

            return {
                "message": "Todo updated successfully",
                "todo": todo
            }

    return {"message": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):

    for todo in todos:

        if todo["id"] == todo_id:

            todos.remove(todo)

            return {
                "message": "Todo deleted successfully"
            }

    return {
        "message": "Todo not found"
    }

