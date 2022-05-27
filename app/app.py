from unicodedata import name
from app.schemas import API_output
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Body, FastAPI, Query
from typing import Dict, List
from .examples import examples
from sqlalchemy.orm import Session
import yaml
from app.models import Employee
from .library.helpers import *
from app.routers import twoforms, unsplash, accordion
from fastapi import FastAPI, status, Depends,Form
from app.database import Base, EmployeeDb, engine


# Create the database
Base.metadata.create_all(engine)
 

templates = Jinja2Templates(directory="templates")


with open("app/config.yaml") as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)

app = FastAPI(
    title="toxicity detection",
    version=configs["versions"]["api"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/predict", response_model=API_output)
async def read_items(q: str = Query(..., min_length=3), example=examples) -> Dict[List[Dict[str, float]], List[str]]:
    if q:
        score = len(q)
        return {
            "data": {
                "sentence": q,
                "score": score,
            },
            "versions": configs["versions"],
        }
@app.get("/add", response_class=HTMLResponse)
async def addrec(request: Request):
    return templates.TemplateResponse("employee.html", {"request": request})



@app.get("/")
def root():
    return "todooo"

@app.post("/employee", status_code=status.HTTP_201_CREATED)
def create_todo(employee: Employee):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    employeedb = EmployeeDb(name = employee.employee_name)

    # add it to the session and commit it
    session.add(employeedb)
    session.commit()

    # grab the id given to the object from the database
    id = employeedb.employee_id

    # close the session
    session.close()

    # return the id
    
    return f"created employee with id {id}"

@app.post("/add")
def create_employee(request: Request, employee_name: str = Form(...),):
    result = Employee(employee_name=employee_name)
   
 