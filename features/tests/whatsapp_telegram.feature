# Created by royat at 9/10/2024
Feature: Whatsapp and Telegram

  Scenario: User can access Whatsapp and Telegram communities
    Given open the main page
    When Log in to the page
    And Click on setting options
    And Click on support option
    And Switch to support window
    Then Verify the support page opens
    When Switch to settings window
    And Click on news option
    Then Verify the news page opens


