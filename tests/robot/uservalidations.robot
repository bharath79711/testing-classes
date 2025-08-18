*** Settings ***
Library    BuiltIn
Library    Process
Library    collections
Library    OperatingSystem

*** Variables ***
${command}    python C:/PycharmProjects/bharath/testing-classes/uservalidation.py


*** Test Cases ***
To check the help message using --help command
    [Documentation]    To check the help related commands in console
    [Tags]    user
    File Should Exist    C:/PycharmProjects/bharath/testing-classes/uservalidation.py

    ${result}=    Run    ${command} --help

    Should Contain    ${result}    usage: uservalidation.py [-h] [-u USERNAME] [-p PASSWORD] [-a AGE]
    Should Contain    ${result}    User validation
    Should Contain    ${result}    -h, --help            show this help message and exit
    Should Contain    ${result}    -a AGE, --age AGE     age

To check the help message using --h command
    [Documentation]    To check the help related commands in console
    [Tags]    user

    ${result}=    Run    ${command} --h

    Should Contain    ${result}    usage: uservalidation.py [-h] [-u USERNAME] [-p PASSWORD] [-a AGE]
    Should Contain    ${result}    User validation
    Should Contain    ${result}    -h, --help            show this help message and exit
    Should Contain    ${result}    -a AGE, --age AGE     age


To Check negitive way by passing few arguments
    [Documentation]    To check negitive way by passing few arguments
    [Tags]    user

    ${result}=    Run    ${command} --username
    Should Contain    ${result}    usage: uservalidation.py [-h] [-u USERNAME] [-p PASSWORD] [-a AGE]
    Should Contain    ${result}    uservalidation.py: error: argument -u/--username: expected one argument

To Check user validation by passing all argument
    [Documentation]    To check passing all arguments
    [Tags]    user

    ${result}=    Run    ${command} --username reddy --password btr --age 20
    Should Contain    ${result}    logged to the server
    Should Contain    ${result}    reddy is usernam
    Should Contain    ${result}    btr is password
    Should Contain    ${result}    20 is age
    Should Contain    ${result}    ('reddy', 'btr', 40)

To Check uservalidations by passing invalid argument values
    [Documentation]    To invalid arguments
    [Tags]    user

    ${result}=    Run    ${command} --username reddy --password btr --age btr
    Should Contain    ${result}    ValueError

To Check uservalidations by passing less age
    [Documentation]    To less age
    [Tags]    user

    ${result}=    Run    ${command} --username reddy --password btr --age 12
    Should Contain    ${result}    check the age above 18

*** Keywords ***
