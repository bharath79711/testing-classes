*** Settings ***
Library    BuiltIn
Library    Process
Library    collections
Library    OperatingSystem
*** Variables ***
${command}    python     C:/PycharmProjects/bharath/testing-classes/calculator.py

*** Test Cases ***
To check the help message using --help command
    [Documentation]    To check the help related commands in console
    [Tags]    calculations
    File Should Exist    C:/PycharmProjects/bharath/testing-classes/calculator.py

     ${result}=    Run    ${command} --help

     Should Contain    ${result}    usage: calculator.py [-h] [--operation {add,subtract,multiply,divide}]
     Should Contain    ${result}    Simple command-line calculator
     Should Contain    ${result}    num1                  First number
     Should Contain    ${result}    num2                  Second number
     Should Contain    ${result}    -h, --help            show this help message and exit
     Should Contain    ${result}    --operation {add,subtract,multiply,divide}
     Should Contain    ${result}    Operation to perform (default: add)


To check the help message using --h command
    [Documentation]    To check the help related commands in console
    [Tags]    calculations

     ${result}=    Run    ${command} --h

     Should Contain    ${result}    usage: calculator.py [-h] [--operation {add,subtract,multiply,divide}]
     Should Contain    ${result}    Simple command-line calculator
     Should Contain    ${result}    num1                  First number
     Should Contain    ${result}    num2                  Second number
     Should Contain    ${result}    -h, --help            show this help message and exit
     Should Contain    ${result}    --operation {add,subtract,multiply,divide}
     Should Contain    ${result}    Operation to perform (default: add)

To check addition calucation by passing possitive numbers
    [Documentation]    To check by taking two possitive numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation add 25 25

     Should Contain    ${result}     Result: 50.0

To check addition calucation by passing Negative numbers
    [Documentation]    To check by taking two Negative numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation add -10 -12

     Should Contain    ${result}     Result: -22.0

To check subtraction calucation by passing possitive numbers
    [Documentation]    To check by taking two possitive numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation subtract 24 12

     Should Contain    ${result}     Result: 12.0

To check subtraction calucation by passing Negative numbers
    [Documentation]    To check by taking two Negative numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation subtract -24 -12

     Should Contain    ${result}     Result: -12.0

To check multiply calucation by passing possitive numbers
    [Documentation]    To check by taking two possitive numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation multiply 19 2

     Should Contain    ${result}     Result: 38.0


To check multiply calucation by passing Negative numbers
    [Documentation]    To check by taking two Negative numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation multiply -11 -2

     Should Contain    ${result}     Result: 22.0

To check Multiply calucation by passing one possitivi and one negative number
      [Documentation]    two check product by taking one possitive and negative number
      [Tags]    calculations

      ${result}=    Run    ${command} --operation multiply -11 2

     Should Contain    ${result}     Result: -22.0



To check division calucation by passing possitive numbers
    [Documentation]    To check by taking two possitive numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation divide 24 4

     Should Contain    ${result}     Result: 6.0




To check division calucation by passing Negative numbers
    [Documentation]    To check by taking two Negative numbers
    [Tags]    calculations

     ${result}=    Run    ${command} --operation divide -12 -6

     Should Contain    ${result}     Result: 2.0


To check division calucation by passing ZERO
    [Documentation]    To check by taking divisable by zero
    [Tags]    calculations

     ${result}=    Run    ${command} --operation divide 10 0

     Should Contain    ${result}     Error: Division by zero


To check more than one oprations at a time
     [Documentation]    two check by taking more than one operation
     [Tags]    calculations

     ${result}=    Run    ${command} --operation add 10 12 --operation subtract 15 5

     Should Contain    ${result}    usage: calculator.py [-h] [--operation {add,subtract,multiply,divide}]
     Should Contain    ${result}    calculator.py: error: unrecognized arguments: 15 5

