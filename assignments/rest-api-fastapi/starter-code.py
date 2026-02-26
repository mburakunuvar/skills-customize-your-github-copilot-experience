"""
Assignment: Building REST APIs with FastAPI
-------------------------------------------
Complete the tasks below to build a simple Task Manager REST API.

Run the app with:
    uvicorn starter-code:app --reload

Then open http://127.0.0.1:8000/docs to explore and test your API.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")

# ---------------------------------------------------------------------------
# Task model - fill in the remaining fields
# ---------------------------------------------------------------------------

class Task(BaseModel):
    id: int
    title: str
    # TODO: Add 'description' (str) and 'completed' (bool, default False) fields


# In-memory storage for tasks
tasks: list[Task] = []


# ---------------------------------------------------------------------------
# Task 1: Basic endpoints
# ---------------------------------------------------------------------------

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    """Return the list of all tasks."""
    # TODO: Return all tasks
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    """Add a new task."""
    # TODO: Append the task to the tasks list and return it
    pass


# ---------------------------------------------------------------------------
# Task 2: Update and delete endpoints
# ---------------------------------------------------------------------------

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Return a single task by ID, or raise 404 if not found."""
    # TODO: Find and return the task with the given task_id
    # Raise HTTPException with status_code=404 if not found
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated: Task):
    """Update an existing task by ID."""
    # TODO: Find the task, update its fields, and return the updated task
    # Raise HTTPException with status_code=404 if not found
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    """Delete a task by ID."""
    # TODO: Find and remove the task from the list
    # Raise HTTPException with status_code=404 if not found
    # Return a confirmation message, e.g. {"message": "Task deleted"}
    pass
