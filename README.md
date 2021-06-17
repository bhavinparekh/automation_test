# Automation test

## Getting started

### Test 1: Build a hlsjs player page with sr integrated.

I created a webpage using the repo and link you provided in the document. And for the server part, I am using python

![ScreenShot](screenshots/test1_hlsjs_player.png)
![ScreenShot](screenshots/test1_hls_player2.png)

### Test 2: HTTP traffic inspection using Charles Proxy

![ScreenShot](screenshots/test2_charles_proxy3.png)
![ScreenShot](screenshots/test2_charles-proxy2.png)
![ScreenShot](screenshots/test2_charles_proxy4.png)

#### CDN mesh Delivery replaces the player’s downloader module with its downloader, which handles traffic from multiple sources, as well as cache it and hands it off to the player’s media buffer.

### Test 3: Selenium and python

## Installation

1. Install python3 in your system. Link to python documentation: https://installpython3.com/
2. Install all python packages from requirement.txt

```bash
git clone https://github.com/bhavinparekh/automation_test.git

cd automation_test

pip install -r requirements.txt
```

3.To lunch the application

```bash
python3 app.py
```

3.To view web page go to localhost 9099

```bash
http://localhost:9099/
```

4.To run test cases

```bash
python3 api.py runserver 0.0.0.0:7000
```

### Run Test in Docker environment

1. Navigate to the working folder and run the following command

```bash
cd automation_test
docker-compose up --build
```
##### Test 1
Go to http://0.0.0.0:7000/launchTest1

select "post" in Postman

put following json in body part

```
{
    "browser": "chrome",
    "number": 3
}
```
Click 'send'
##### Test 2
Go to http://0.0.0.0:7000/launchTest2

select "Get" in Postman

Click 'send'

Note: Because we already run app.py on port 9099, so our build gets error like
: 'OSError: [Errno 98] Address already in use' to avoid this before starting docker kill all running ports

## Summary

After doing this test I learn more About CDN mesh devilry and How the peer-to-peer network work.

I face one issue while doing this excise that first my demo works perfectly without Charles proxy but after some time
it's stopped working until I started Charles proxy. So Didn't able to figure out what's the issue I am facing with
proxies.

The 3rd test used selenium python. And for the test framework, I used Python behave which similar to cucumber.

Set up the docker for the project is a little tricky because of port and localhost API calls.