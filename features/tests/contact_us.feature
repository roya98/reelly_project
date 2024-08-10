# Created by royat at 8/10/2024
Feature: Verify contact us functionality

  Scenario: User can open the Contact us page
    Given Open the main page
    When Log in to the page
    And Click on setting options
    And Click on Contact us option
    Then Verify the contact us page opens
    Then Verify there are at least 4 social media icons
    Then Verify 'Connect the company' button is available and clickable