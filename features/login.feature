Feature: Basic authentication

  Background:

  Scenario: User with valid credentials can login
    Given I open a browser
    When I login with use=r name 'admin' and password 'admin'
    Then I verify Practical SQA page loaded

