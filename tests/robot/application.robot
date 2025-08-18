*** Settings ***
Suite Setup    Login to chrome
Suite Teardown    Close All Browsers
Library    BuiltIn
Library  SeleniumLibrary

*** Variables ***

${LOGIN_URL}  https://google.com/
${data}    reddy


*** Test Cases ***

Login to Gmail
        Maximize Browser Window
        Input Text    name=q    gmail
        Press Keys    name=q    ENTER
#        Page Should Not Contain    gmail
#        Close Browser


Example with IF/ELSE IF/ELSE

    ${Number}=    Set Variable    5

    IF    ${Number} > 10
        Log To Console    The number is greater than 10.
    ELSE IF    ${Number} > 0
        Log To Console    The number is greater than 0 but not greater than 10.
    ELSE
        Log To Console    The number is 0 or less.
    END


*** Keywords ***
Login to chrome
    Open Browser  ${LOGIN_URL}  Chrome