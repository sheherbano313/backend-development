from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"welcome to fast api"}


@app.get("/about")
def about():
    return{"message":"this is about page"}

@app.get("/users")
def user():
    return{
        "user":["mohit","Rohit","Rahul"]
    }