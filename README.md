# pymongo-fastapi--vue-fullstack

This project is a full-stack web application using FastAPI for the backend, MongoDB for the database, and Vue.js for the frontend. The application is containerized using Docker and Docker Compose.

## Project Structure
```bash
project/
 ├── backend/
 │ ├── app/
 │ │ ├── init.py
 │ │ ├── main.py
 │ │ ├── models/
 │ │ │ ├── init.py
 │ │ │ └── user.py
 │ │ ├── views/
 │ │ │ ├── init.py
 │ │ │ └── user.py
 │ │ ├── controllers/
 │ │ │ ├── init.py
 │ │ │ └── user.py
 │ │ ├── schemas/
 │ │ │ ├── init.py
 │ │ │ └── user.py
 │ │ ├── config.py
 │ │ ├── database.py
 │ │ └── requirements.txt
 │ └── Dockerfile
 ├── frontend/
 │ ├── public/
 │ ├── src/
 │ │ ├── assets/
 │ │ ├── components/
 │ │ ├── views/
 │ │ ├── App.vue
 │ │ ├── main.js
 │ ├── package.json
 │ └── Dockerfile
 └── docker-compose.yml
```

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create a .env file in the backend directory with the following content:
```
MONGO_DETAILS=mongodb://mongodb:27017
SECRET_KEY=your_secret_key
```

3. Build and start the containers:
```bash
docker-compose up --build
```

## Backend
The backend is built with FastAPI and uses MongoDB as the database.

* FastAPI:
    * A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

* MongoDB:
    * A NoSQL database for storing user data.

## Frontend
The frontend is built with Vue.js.

* Vue.js:
    * A progressive JavaScript framework for building user interfaces.

## Directory Structure
* backend/app/: Contains the FastAPI application code.
    * main.py: The entry point for the FastAPI application.
    * models/: Contains the Pydantic models.
    * views/: Contains the API route handlers.
    * controllers/: Contains the business logic.
    * schemas/: Contains the Pydantic schemas for request and response models.
    * config.py: Configuration settings for the application.
    * database.py: MongoDB connection setup.
* frontend/: Contains the Vue.js application code.
    * public/: Static assets.
    * src/: Source code for the Vue.js application.
    * assets/: Assets like images and styles.
    * components/: Vue components.
    * views/: Vue views.
    * App.vue: The root Vue component.
    * main.js: The entry point for the Vue application.

## Usage
* Access the FastAPI backend at http://localhost:8000.
* Access the Vue.js frontend at http://localhost:8080.
* Access Mongo Express (MongoDB management tool) at http://localhost:8081.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.