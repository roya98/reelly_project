# Created by royat at 8/14/2024
Feature: User guide page


  Scenario: User can open User guide page
    Given Open the main page
    When Log in to the page
    And Click on setting options
    And Click on User Guide option
    Then Verify the user guide page opens
    And Verify all lesson videos contain titles