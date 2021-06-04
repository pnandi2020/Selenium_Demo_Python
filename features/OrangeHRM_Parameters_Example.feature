#Author: Abhinay Dixit
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
Feature: To Test Orange HRM Sign On Functionality

  Scenario: Login to OrangeHRM with Valid parameters
 	Given User has Launched Browser
    When User Navigate to Sign On Page
 	And User enters "Admin" and "admin123"
 	And User Click on Login Button
    Then User should logged in and Dashboard page should display