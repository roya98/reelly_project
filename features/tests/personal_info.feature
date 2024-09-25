# Created by royat at 9/23/2024
Feature: settings and personal information

  Scenario: User can go to settings and edit the personal information
    Given Open the main page
    When Log in to the page
    And Click on setting options
    And Click on Edit profile option
    And Enter some test information in the input fields
    Then Check the right information is present in the input fields
    And Check Close and Save Changes buttons are available and clickable