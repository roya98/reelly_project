# Created by royat at 9/28/2024
Feature: Setting UI elements

  Scenario: User can go to settings and see the right number of UI elements
    Given Open the main page
    When Log in to the page
    And Click on setting options
    Then Verify the settings page opens
    And Verify there are 12 options for the settings
    And Verify 'connect the company' button is available