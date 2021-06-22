import uvicorn as uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel
import selenium_scripts.test1 as test1

from selenium_scripts import test3

app = FastAPI()


class test1Model(BaseModel):
    browser: str
    number: int


@app.get('/')
def home():
    return {"Welcome to Automation Test"}


@app.post('/launchTest1')
def test1api(model: test1Model):
    print(model.dict())
    output = test1.test(model.browser, model.number)
    return {'result': output}


@app.get('/launchTest2')
def test2api():
    data = test3.test()
    return {'result': data}


if __name__ == "__main__":
    uvicorn.run(app, host=str('0.0.0.0'), port=int('7000'))
