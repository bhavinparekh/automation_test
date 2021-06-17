import uvicorn as uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel
import selenium_scripts.test1 as test1
import subprocess
import requests

app = FastAPI()


class test1Model(BaseModel):
    browser: str
    number: int


@app.get('/')
def home():
    return {"Welcome to AR Cut & Paste"}


@app.post('/launchTest1')
def test1api(model: test1Model):
    print(model.dict())
    output = test1.test(model.browser, model.number)
    return {'result': output}


@app.get('/launchTest2')
def test2api():
    bashCommand = "behave -f allure_behave.formatter:AllureFormatter -o test_result"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return {'result': output}


if __name__ == "__main__":
    uvicorn.run(app, host=str('0.0.0.0'), port=int('7000'))
