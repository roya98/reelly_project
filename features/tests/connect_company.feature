# Created by royat at 8/1/2024
Feature: Connect the company

  Scenario: The user can click on “Connect the company” on
  the left side of the main page
    Given Open the main page
    When Log in to the page
    And Click on 'Connect the company'
    And  Switch the new tab
    Then Verify the connect company page opens