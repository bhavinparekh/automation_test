Feature: Showing off behave

  Scenario: test to verify that PLAY, PAUSE and SEEK did work
    Given initialize selenium webdriver
    When I launch browser
    And check video loaded
    And play video for 10s
    And pause video for 10s
    And seek video for 25s
    And play video for 10s
    Then Test successful and close browser