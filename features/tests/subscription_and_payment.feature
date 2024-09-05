# Created by royat at 9/4/2024
Feature: Subscription & payments page

  Scenario: User can open Subscription & payments page
    Given Open the main page
    When Click on setting options
    And Click on Subscription & payments option
    Then Verify Payment Page Opens
    And Verify title 'Subscription & payments' is visible
    And Verify 'back' and 'upgrade plan' buttons are available
