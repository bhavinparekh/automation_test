# Automation test

## Getting started

### Test 1: Build a hlsjs player page with SR integrated.

![ScreenShot](screenshots/test1_hlsjs_player.png)
![ScreenShot](screenshots/test1_hls_player2.png)

### Test 2: HTTP traffic inspection using Charles Proxy

![ScreenShot](screenshots/test2_charles_proxy1.png)
![ScreenShot](screenshots/test2_charles-proxy2.png)

#### Streamroot technology is integrated at the player level and more specifically into the player’s media engine. Streamroot replaces the player’s downloader module with its own downloader, which is specifically designed to direct and handle traffic from multiple sources, as well as to cache it and hand it off to the player’s media buffer.

### Test 3: Selenium and python

## Installation

1. Install python3 in your system.Link to python documentation: https://installpython3.com/
2. Install all python packages from requirement.txt or

```bash
git clone https://github.com/bhavinparekh/automation_test.git

cd automation_test

pip install -r requirements.txt
```

3.To lunch application

```bash
python3 app.py
```

3.view web page go to localhost

```bash
http://localhost:9099/
```

## Run Scripts

####1.Setup a script that opens the webpage you generated in Test 1 on multiple chrome and Firefox browsers.

```bash
python3 selenium_scripts/test1.py 
```

####2. Add to the script the ability to PLAY, PAUSE and SEEK the hlsjs video player

```bash
python3 selenium_scripts/test2.py 
```
####3. Add some tests to verify that PLAY, PAUSE and SEEK did work.

Note: For this test I used Python behave framework to write test cases. Link to python behave documentation: https://behave.readthedocs.io/en/stable/
```bash
$ behave
```
output in console 
```
Feature: Showing off behave # features/video_automation.feature:2

  Scenario: test to verify that PLAY, PAUSE and SEEK did work  # features/video_automation.feature:4
    Given initialize selenium webdriver                        # features/steps/video_player_steps.py:12 1.120s
    When I launch browser                                      # features/steps/video_player_steps.py:26 0.170s
    And play video for 10s                                     # features/steps/video_player_steps.py:36 10.037s
    And pause video for 10s                                    # features/steps/video_player_steps.py:47 10.023s
    And seek video for 30s                                     # features/steps/video_player_steps.py:58 0.396s
    And play video for 10s                                     # features/steps/video_player_steps.py:36 10.017s
    Then Test successful and close browser                     # features/steps/video_player_steps.py:70 0.057s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
7 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m31.820s

```
####4. Docker for 3rd test
Install docker-compose in your system using following link : https://docs.docker.com/compose/install/
```bash
docker-compose up --build
```
Note: Becuase we already run app.py on port 9099, so our build gets error like
: 'OSError: [Errno 98] Address already in use' . to avoid this before starting docker kill all running ports 

## view


```ini
http : //localhost:9091/
```
