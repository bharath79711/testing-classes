*** Settings ***
Library     collections
Library    string
Library     OperatingSystem
Library    Process
Library   SeleniumLibrary



*** Variables ***
${URL}      https://accounts.google.com
${EMAIL}        anudeepm39@gmail.com
${PASSWORD}     Amma143@#
${BROWSER}      chrome


*** Test Cases ***
Gmail login test

    open browser    ${URL}  ${BROWSER}
    Input Text    id=identifierId    ${Email}
    Click Button    xpath=//*[@id="identifierNext"]/div/button
    Sleep    10s
    Input Text  id=password   ${PASSWORD}
#    Click Button    locator

    Click Button    xpath=//*[@id="passwordNext"]//div/button
    #Sleep    3s
   # Capture Page Screenshot
   # [Teardown]  close Browser
