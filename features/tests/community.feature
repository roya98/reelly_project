# Created by royat at 7/30/2024
Feature: Testing features in community page

  Scenario: User can open the community page
    Given Open the main page
    When Log in to the page
    And Click on setting options
    And Click on Community option
    Then Verify the community page opens
    And Verify 'Contact support' button is available and clickable