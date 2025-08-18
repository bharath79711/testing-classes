*** Settings ***

Library    collections
Library    string
Library   OperatingSystem
Library    Process
Library    SSHLibrary


*** Variables ***

${x}    10
${y}    20


*** Test Cases ***

sum of two variables
     [Documentation]    sum of x and y
     [Tags]    anu    bharath
     Log     ${x}+${y}
multiplication of two variables
          [Documentation]    multiplication of x and y
          [Tags]    bharath
          Log    ${x}*${y}
          check the name strn


*** Keywords ***
check the name strn
   [Documentation]    custom keywords
   Should Contain    talari bharath kumar    talari
   Should Not Contain    talari bharath kumar    ashok
   Should Not Contain    talari bharath kumar    anu








