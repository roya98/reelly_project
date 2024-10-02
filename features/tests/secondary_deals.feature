# Created by royat at 10/1/2024
Feature: Secondary deals

  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open the main page
    When Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the secondary page opens
    And Go to the final page using the pagination button
    And Go back to the first page using the pagination button