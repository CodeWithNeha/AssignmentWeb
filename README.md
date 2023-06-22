# Task API

This API allows you to manage tasks. It provides endpoints for creating, updating, retrieving, and deleting tasks.

## Endpoints

### Get all tasks

Get a list of all tasks.

**Endpoint:** `/tasks`

**Method:** GET

**Curl Command:**
```bash
curl --location 'http://127.0.0.1:8000/tasks'
```

**Response:**
[
    {
        "id": 1,
        "title": "Task Title",
        "description": "Task Description"
    },
    {
        "id": 2,
        "title": "Task Title123",
        "description": "Task Description"
    }
]


### Get Single task By Id

Get a single task by id.

**Endpoint:** `/tasks/{task_id}`

**Method:** GET

**Curl Command:**
```bash
curl --location 'http://127.0.0.1:8000/tasks/1'
```

**Response:**
{
    "id": 1,
    "title": "Task Title",
    "description": "Task Description"
}

### Authentication
The API uses HTTP Basic Authentication. To access the endpoints, include the credentials in your curl commands using the -u option

Note: Replace admin with your username and password with your password.

### Create a new task 

Create new task.

**Endpoint:** `/tasks`

**Method:** POST

**Curl Command:**
```bash
curl --location 'http://127.0.0.1:8000/tasks/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46cGFzc3dvcmQ=' \
--data '{
    "title": "Task Title123",
    "description": "Task Description"
}'
```

**BODY :**
{
    "title": "Task Title123",
    "description": "Task Description"
}


**Response:**
{
    "message": "Task created successfully."
}

### Update task by Id 

Update task

**Endpoint:** `/tasks/{task_id}`

**Method:** PUT

**Curl Command:**
```bash
curl --location --request PUT 'http://127.0.0.1:8000/tasks/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46cGFzc3dvcmQ=' \
--data '{
    "title": "Task ",
    "description": "Task Description"
}'
```

**BODY :**
{
    "title": "Task Title123",
    "description": "Task Description"
}


**Response:**
{
    "message": "Task updated successfully."
}


### Delete task by Id 

Delete task

**Endpoint:** `/tasks/{task_id}`

**Method:** DELETE

**Curl Command:**
```bash
curl --location --request DELETE 'http://127.0.0.1:8000/tasks/1/' \
--header 'Authorization: Basic YWRtaW46cGFzc3dvcmQ=' \
--data ''
```

**Response:**
{
    "message": "Task deleted successfully."
}


## Installation and Setup

To set up the project, follow these steps:

1. Clone the repository:

```
git clone https://github.com/CodeWithNeha/AssignmentWeb.git
```

2. Navigate to the project directory:

```
cd your-project
```

3. Create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
```

4. Install the project dependencies:

```
pip install -r requirements.txt
```

5. Start the development server:

```
uvicorn main:app --reload
```