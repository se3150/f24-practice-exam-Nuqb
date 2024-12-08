Feature: calculate the area of a triangle
  As an aspiring mathematician
  I should be able to calculate the area of a triangle
  So that I can chat with my math friends like a pro

Background:
    Given I open the url "https://byjus.com/herons-calculator/"

Scenario: I can calculate the area of a triangle
    When I set "4" to the inputfield "#a"
    When I set "4" to the inputfield "#b"
    When I set "2" to the inputfield "#c"
    When I click on the element ".clcbtn"
    Then I expect that element "#a" contains the text "4"
    Then I expect that element "#b" contains the text "4"
    Then I expect that element "#c" contains the text "2"
    Then I expect that element "#_e" contains the text "5"
    Then I expect that element "#_d" contains the text "3.873"

Scenario: I can use decimals
    When I set "4.5" to the inputfield "#a"
    When I set "4" to the inputfield "#b"
    When I set "2" to the inputfield "#c"
    When I click on the element ".clcbtn"
    Then I expect that element "#a" contains the text "4.5"
    Then I expect that element "#b" contains the text "4"
    Then I expect that element "#c" contains the text "2"
    Then I expect that element "#_e" contains the text "5.25"
    Then I expect that element "#_d" contains the text "4.000"

Scenario: If c is bigger than a + b, the site will alert the user of "Square root of a negative number"
    When I set "4.5" to the inputfield "#a"
    When I set "4" to the inputfield "#b"
    When I set "10" to the inputfield "#c"
    When I click on the element ".clcbtn"
    Then I expect that a alertbox contains the text "Square root of a negative number"