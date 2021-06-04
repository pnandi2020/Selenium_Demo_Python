#Author: Saumya
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
  @Sanity
Feature: To Test Orange HRM Sign On Functionality

  Scenario Outline: Login to OrangeHRM with Valid parameters
    Given User has Launched Browser
    When User Navigate to Sign On Page
    And User enters "<Username>" and "<Password>"
    And User Click on Login Button
    Then User should logged in and Dashboard page should display
    Then Logout from Application
    Examples: With Multiple Data
      | Username | Password |
      | Admin   | admin123  |
      | Admin   | admin123  |
      | Admin   | admin123  |