*** Settings ***
Library    SeleniumLibrary
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}        Chrome
${FB_URL}         https://www.facebook.com
${FB_EMAIL}       7893782282
${FB_PASSWORD}    7893782282Anu

*** Test Cases ***
Login To Facebook
    [Documentation]    Logs into Facebook account
    Open Browser    ${FB_URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    id=email    10s
    Input Text    id=email    ${FB_EMAIL}

    Wait Until Element Is Visible    id=pass    10s
    Input Password    id=pass    ${FB_PASSWORD}

    Wait Until Element Is Enabled    name=login    10s
    Click Button    name=login
    Sleep    10s
    Capture Page Screenshot
#
#    # Optional: Wait for "Are you human?" message and handle it
#    Wait Until Page Contains    Verifying you are human    timeout=10s
#    Capture Page Screenshot
#    Log    Facebook may be verifying bot activity. Manual intervention may be required.
