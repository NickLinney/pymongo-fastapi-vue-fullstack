from fastapi import FastAPI
from app.views import user as user_view
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

# Connect to MongoDB
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# Include the user router
app.include_router(user_view.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application with MongoDB!"}
