#!/bin/bash

# Create directories
mkdir -p ./backend/app/models
mkdir -p ./backend/app/views
mkdir -p ./backend/app/controllers
mkdir -p ./backend/app/schemas
mkdir -p ./frontend/public
mkdir -p ./frontend/src/assets
mkdir -p ./frontend/src/components
mkdir -p ./frontend/src/views

# Create files in backend/app
touch ./backend/app/__init__.py
touch ./backend/app/main.py
touch ./backend/app/models/__init__.py
touch ./backend/app/models/user.py
touch ./backend/app/views/__init__.py
touch ./backend/app/views/user.py
touch ./backend/app/controllers/__init__.py
touch ./backend/app/controllers/user.py
touch ./backend/app/schemas/__init__.py
touch ./backend/app/schemas/user.py
touch ./backend/app/config.py
touch ./backend/app/database.py
touch ./backend/app/requirements.txt

# Create Dockerfile in backend
touch ./backend/Dockerfile

# Create files in frontend/src
touch ./frontend/src/App.vue
touch ./frontend/src/main.js

# Create package.json and Dockerfile in frontend
touch ./frontend/package.json
touch ./frontend/Dockerfile

# Create docker-compose.yml in project root
touch ./docker-compose.yml

echo "Directory structure and files created successfully!"
