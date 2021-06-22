import json
import os
import subprocess
from pathlib import Path


def test():
    bashCommand = "behave -f allure_behave.formatter:AllureFormatter -o test_result"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    process.communicate()
    path = "test_result"
    paths = sorted(Path(path).iterdir(), key=os.path.getmtime)
    f = open(paths[-1])
    data = json.load(f)
    return data
