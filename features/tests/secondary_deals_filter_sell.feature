# Created by royat at 10/8/2024
Feature: want to sell filter in secondary deals page

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open the main page
    When Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the secondary page opens
    When Click on Filters and select 'want to sell' and apply
    Then Verify all cards have 'for sale' tag