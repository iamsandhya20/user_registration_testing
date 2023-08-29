Feature: User Registration

  Scenario Outline: Successful user registration with different data
    Given the user is on the registration page
    When they enter "<username>" and "<email>"
    And they set the password to "<password>"
    And they confirm the password
    Then the registration should be successful

    Examples:
      | username | email             | password |
      | sandhya   | sandhya@gmail.com | sandhya123  |

