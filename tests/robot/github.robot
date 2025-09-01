*** Settings ***
Library    SeleniumLibrary
Library     BuiltIn
Library    XML
Library     String
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}         Chrome
${github}       https://github.com/
${GITHUB_URL}      https://github.com/login
${GITHUB_USERNAME}      bharathkumartalari70@gmail.com
${GITHUB_PASSWORD}      Bharath@326
${combined}     None
*** Test Cases ***
Login To GitHub
    [Documentation]    Logs into GitHub account
    Open Browser    ${GITHUB_URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    id=login_field    10s
    Input Text    id=login_field    ${GITHUB_USERNAME}

    Wait Until Element Is Visible    id=password    10s
    Input Password    id=password    ${GITHUB_PASSWORD}

    Wait Until Element Is Enabled    name=commit    20s
    Click Button    name=commit
    
    Wait Until Element Is Visible    id=dashboard-repos-filter-left    10s

    Go To    https://github.com/settings/profile
    Wait Until Page Contains Element    xpath=//input[@id='user_profile_name']    10s
    ${text}=    Get Text    id=settings-header
    ${username}=    Split String    ${text}    (
    ${cleaned}=    Strip String    ${username[0]}
    Log    ${cleaned}
    Go To    https://github.com/dashboard
    Input Text    id=dashboard-repos-filter-left    python-classes
    ${combined}=    Set Variable   ${cleaned}/python-classes
    Log    ${combined}
    Wait Until Page Contains    ${combined}   10s
#    ${url} =    Set Variable    ${github}/${cleaned}/python-classes
    ${url} =    Set Variable    /${cleaned}/python-classes
    Log    ${url}
#    Go To      ${url}
    Click Link    xpath=//a[@href='${url}']
    Capture Page Screenshot
    Sleep    5s


