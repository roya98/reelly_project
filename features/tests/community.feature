# Created by royat at 7/30/2024
Feature: Testing features in community page

  Scenario: User can open the community page
    Given Open the main page
    When Log in to the page
    When Click on setting options
    When Click on Community option
    Then Verify the right page opens
    Then Verify 'Contact support' button is available and clickable