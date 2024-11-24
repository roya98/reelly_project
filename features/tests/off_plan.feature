# Created by royat at 11/23/2024
Feature: Off Plan functionalities
  # Enter feature description here

  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open the main page
    When Log in to the page
    And Click on 'off plan' at the left side menu
    Then Verify the off plan page opens
    And Verify each product on this page contains a title and picture visible



