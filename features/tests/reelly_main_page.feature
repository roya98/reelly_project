# Created by royat at 7/21/2024
Feature: Test Scenarios for reelly main page

  Scenario: User can change the language from the page
    Given Open the main page
    When Log in to the page
    When Click on the main menu option
    When Change the language of the page to Russian
    Then Verify the language has changed
