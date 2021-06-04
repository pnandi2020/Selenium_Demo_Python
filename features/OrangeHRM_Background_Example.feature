#Author: Abhinay Dixit
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
@E2E
Feature: To Test Orange HRM Sign On and Sign Out Functionality

  Background: Common Steps
    Given User has Launched Browser
    When User Navigate to Sign On Page
 	And User enters "Admin" and "admin123"
 	And User Click on Login Button
  @Sanity
  Scenario: Successful to Dashboard Page
    Then User should logged in and Dashboard page should display

  Scenario: Successful LogOut from OrangeHRM
    And User Click on Welcome Link
    And User Click on Logout Link
    Then User user travel back to OrangeHRM Login Page