*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${BROWSER}      chrome
${URL}      https://www.bcci.tv
${URL2}    https://www.bcci.tv/international/men/fixtures-results

*** Test Cases ***
#----Home page----

1.open BCCI Website
     Open Browser   ${URL}  ${BROWSER}
     [Documentation]    Home page verify
     [Tags]     bcci
     Sleep    5s
     Maximize Browser Window
2.Verify main Navigation Menu
     Open Browser   ${URL}  ${BROWSER}
     [Documentation]    verify Home page navigations
     [Tags]     bcci
     Maximize Browser Window
     Page Should Contain    International
     Page Should Contain    Domestic
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[3]
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[1]
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[2]
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[5]
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[6]
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[7]
     Page Should Contain Element    xpath=//*[@id="imw-international-men"]/a[8]


3.Validate Hero Banner And Featured videos
      Open Browser   ${URL}  ${BROWSER}
      Maximize Browser Window
      Wait Until Element Is Visible    xpath=//section[contains(@class,"hero-banner1")]       10s
      Page Should Contain Element    xpath=//section[contains(@class,"hero-banner1")]
      Page Should Contain Element    xpath=//*[contains(@id,"slick-slide")]
      Sleep    5s
      Log To Console    Hero Banner is visible
      Capture Page Screenshot



4.Verify Live Match Or No Match
    Open Browser   ${URL}  ${BROWSER}
    ${status}=    Run Keyword And Return Status    Page Should Contain Element    xpath=//div[contains(@class,"match-score-block")]     10s
    Run Keyword If    '${status}'=='True'    Log To Console    Live match score is visible
    Run Keyword If    '${status}'=='False'    Log To Console    No live matches currently
    Capture Page Screenshot


#=====fixtures and Results======
1.Verify Fixtures Page Loads
    Open Browser    ${URL2}   ${BROWSER}    10s
    Maximize Browser Window
    Title Should Be    xpath=/html/body/section/div/div/div[1]/div[1]/h2
    Capture Page Screenshot
    Log To Console    Fixtures page loaded successfully

2.Check Upcoming Matches List
    Open Browser    ${URL2}   ${BROWSER}    10s
    Wait Until Element Is Visible    xpath=//*[@id="pills-upcoming-tab"]    20s
    Click Element    xpath=//*[@id="pills-upcoming-tab"]
    Wait Until Element Is Visible    xpath=//div[contains(@class,"match-list")]     20s
    Page Should Contain Element      xpath=//div[contains(@class,"match-list")]
    Capture Page Screenshot




