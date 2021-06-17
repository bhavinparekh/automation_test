import uvicorn as uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel
import selenium_scripts.test1 as test1
import subprocess
import json
import os
import stat

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
    path = "./test_result"
    files_sorted_by_date = []

    filepaths = [os.path.join(path, file) for file in os.listdir(path)]
    file_statuses = [(os.stat(filepath), filepath) for filepath in filepaths]
    files = ((status[stat.ST_CTIME], filepath) for status, filepath in file_statuses if
             stat.S_ISREG(status[stat.ST_MODE]))
    for creation_time, filepath in sorted(files):
        break
    f = open(filepath)
    data = json.load(f)
    return {'result': data}


if __name__ == "__main__":
    uvicorn.run(app, host=str('0.0.0.0'), port=int('7000'))
