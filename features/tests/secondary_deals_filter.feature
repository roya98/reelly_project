# Created by royat at 10/8/2024
Feature: filter in secondary deals page

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open the main page
    When Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the secondary page opens
    When Click on Filters and select 'want to sell' and apply
    Then Verify all cards have 'for sale' tag



  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open the main page
    When Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the secondary page opens
    When Click on Filters and select 'want to buy' and apply
    Then Verify all cards have 'Want to buy' tag


  Scenario: User can filter the Secondary deals by Unit price range
    Given Open the main page
    When Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the secondary page opens
    When Click on Filters Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)

