# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework in Python. Students will learn how to define routes, handle HTTP methods, work with request/response models using Pydantic, and test endpoints interactively through FastAPI's built-in documentation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI project and define a set of RESTful endpoints for a simple "Task Manager" API. The API should allow clients to create, read, update, and delete tasks.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app instance
- Define a `Task` model using Pydantic with fields: `id` (int), `title` (str), `description` (str), and `completed` (bool, default `False`)
- Implement a `GET /tasks` endpoint that returns a list of all tasks
- Implement a `POST /tasks` endpoint that accepts a task body and adds it to the list
- Store tasks in an in-memory list (no database required)


### 🛠️ Add Update and Delete Endpoints

#### Description
Extend the API with endpoints to update an existing task's details and to delete a task by its ID.

#### Requirements
Completed program should:

- Implement a `GET /tasks/{task_id}` endpoint that returns a single task by ID, or returns a 404 error if not found
- Implement a `PUT /tasks/{task_id}` endpoint that updates the title, description, or completed status of an existing task
- Implement a `DELETE /tasks/{task_id}` endpoint that removes a task by ID
- Return appropriate HTTP status codes (e.g., `200`, `201`, `404`) for each endpoint

Example response for `GET /tasks/1`:
```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Go through the FastAPI documentation",
  "completed": false
}
```
