# Created by royat at 7/24/2024
Feature: Project feature

  Scenario: User can add a project through the settings
    Given Open the main page
    When Log in to the page
    When Click on setting options
    When Click on Add a project
    When Add some test information to the input fields
    Then Verify the right information is present in the input field
    Then Verify 'Send an application' button is available and clickable