# Created by royat at 8/29/2024
Feature: Testing Password Functionality

  Scenario: User can open change password page
    Given Open the main page
    When Log in to the page
    And Click on setting options
    And Click on Change password option
    Then Verify the change password page opens
    When Add some test password to the input fields
    Then Verify the 'Change password' button is available