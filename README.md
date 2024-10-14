# Requirement 3

# Todo List API

This project is a simple Todo list API built using Flask, featuring token-based authentication. The API allows users to create, retrieve, update, and delete todo items.

## Project Overview

This API provides endpoints to manage a todo list with token-based authentication. It supports basic CRUD (Create, Read, Update, Delete) operations. All requests must include a Bearer token for authentication, ensuring that only authorized users can access or modify the todo items.

## Features

### **Back-End:**

- **Flask**:
  - Manages GET, POST, PUT, and DELETE requests for todo items.
  - Token-based authentication to secure all endpoints.
  - In-memory data storage for simplicity (resets when the server is restarted).
  - Error handling for invalid requests and 404 not found errors.
  - JSON responses for easy integration with front-end applications or API consumers.

### **API Endpoints Overview**:

1. **GET /todos** - Retrieve all todo items.
2. **POST /todos** - Create a new todo item (requires `title` in the request body).
3. **GET /todos/{id}** - Retrieve a specific todo item by ID.
4. **PUT /todos/{id}** - Update a specific todo item by ID (can update `title` and `completed` fields).
5. **DELETE /todos/{id}** - Delete a specific todo item by ID.
6. **DELETE /todos** - Clear all todo items.

### **Authentication:**

- All endpoints require a Bearer token to be passed in the `Authorization` header.
- Example:
  ```bash
  Authorization: Bearer MySecretToken
  ```

## Installation
1. **Clone the Repository:**
bash
git clone https://github.com/Rahma-memo/Requirment_3
cd your-repo

### **Install Dependencies:**

```bash
pip install flask
```

### **How to Run the Project:**

To start the Flask app locally, use the following command in your terminal:

```bash
python app.py
```

The server will run at [http://127.0.0.1:3000](http://127.0.0.1:3000).

## Postman Collection

You can test the API using the Postman collection available at the following URL:

[Postman Collection URL](<https://elements.getpostman.com/redirect?entityId=38975819-b8f41551-2508-4fbd-ab04-f78f66df6594&entityType=collection>)

## Swagger Documentation

Below is a screenshot of the Swagger documentation for the API:

![image](https://github.com/user-attachments/assets/439dcd31-313d-45ab-a208-3629b73a29e9)

## Usage

### **Authentication Middleware:**

Before each request, the application checks the `Authorization` header for a Bearer token. If the token is missing or invalid, the request will be rejected with a 401 Unauthorized response.

### **API Endpoints Example:**

- **Create a Todo Item**:
  ```bash
  POST /todos
  Authorization: Bearer MySecretToken
  Content-Type: application/json
  {
    "title": "task1"
  }
  ```

- **Get All Todo Items**:
  ```bash
  GET /todos
  Authorization: Bearer MySecretToken
  ```

- **Update a Todo Item**:
  ```bash
  PUT /todos/1
  Authorization: Bearer MySecretToken
  Content-Type: application/json
  {
    "title": "task1",
    "completed": true
  }
  ```

- **Delete a Todo Item**:
  ```bash
  DELETE /todos/1
  Authorization: Bearer MySecretToken
  ```

- **Clear All Todo Items**:
  ```bash
  DELETE /todos
  Authorization: Bearer MySecretToken
  ```

### **Error Handling:**

- If a todo item is not found, a 404 response is returned:
  ```json
  {"error": "Todo not found"}
  ```

- If the request is unauthorized due to a missing or incorrect token, a 401 response is returned:
  ```json
  {"error": "Unauthorized"}
  
