# Task Management API Documentation

Welcome to the Task Management API! This API allows you to manage tasks, including creating, retrieving, updating, and deleting tasks. It also supports filtering tasks by completion status and pagination for large task lists.

## Base URL

http://<your-domain>/api/tasks/


## Endpoints

### 1. List Tasks


- **URL:** `/`
- **Method:** `GET`
- **Description:** Retrieve a list of tasks. You can filter tasks by completion status using the `completed` query parameter.
- **Query Parameters:**
  - `completed`: Filter tasks by their completion status. Accepts `true` or `false`.
- **Response:**
  - **200 OK**: Returns a list of tasks.
  - **400 Bad Request**: Invalid value for the `completed` parameter.
  - **200 OK**: Message if no tasks are available.

**Example Request:**
GET /api/tasks/?completed=true


**Example Response:**
```json
[
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description for Task 1",
        "completed": false,
        "due_date": "2024-09-30"
    },
    ...
]

### Create a Task
- **URL:** `/`
- **Method:** `POST`
- **Description:** Create a new task.
- **Request Body:**
```json

{
    "title": "Task Title",
    "description": "Task Description",
    "completed": false,
    "due_date": "2024-09-30"
}

Response:
201 Created: Returns the created task.
400 Bad Request: Validation errors.

Example Request:
POST /api/tasks/

Example Response:

{
    "id": 2,
    "title": "New Task",
    "description": "Description for the new task",
    "completed": false,
    "due_date": "2024-10-01"
}


3. Retrieve a Task
URL: /<int:pk>/
Method: GET
Description: Retrieve a specific task by its ID.
Response:
200 OK: Returns the task.
404 Not Found: Task does not exist.

Example Request:
GET /api/tasks/1/

Example Response:

{
    "id": 1,
    "title": "Task 1",
    "description": "Description for Task 1",
    "completed": false,
    "due_date": "2024-09-30"
}


4. Update a Task
URL: /<int:pk>/
Method: PUT
Description: Update a specific task by its ID.

Request Body:
{
    "title": "Updated Task Title",
    "description": "Updated Description",
    "completed": true,
    "due_date": "2024-10-05"
}

Response:
200 OK: Returns the updated task.
400 Bad Request: Validation errors.
404 Not Found: Task does not exist.

Example Request:
PUT /api/tasks/1/


5. Delete a Task
URL: /<int:pk>/
Method: DELETE
Description: Delete a specific task by its ID.
Response:
204 No Content: Task deleted successfully.
404 Not Found: Task does not exist.

Example Request:
DELETE /api/tasks/1/

6. Mark Task as Completed
URL: /mark_task_completed/<int:pk>/
Method: PATCH
Description: Mark a specific task as completed.
Request Body:

{
    "completed": true
}


Example Request:
PATCH /api/tasks/1/mark_task_completed/

Example Response:

{
    "message": "Task updated successfully."
}


Pagination
The API supports pagination for the task list. By default, it returns 10 tasks per page. You can adjust the number of tasks returned by using the page_size query parameter.

Example Pagination Request:
GET /api/tasks/?page_size=5

Example Pagination Response:
{
    "count": 20,
    "next": "http://<your-domain>/api/tasks/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Description for Task 1",
            "completed": false,
            "due_date": "2024-09-30"
        },
        ...
    ]
}







