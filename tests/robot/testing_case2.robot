*** Settings ***
Library    BuiltIn

*** Variables ***

${Name}    Bharath
${age}    29
${village}    chintakunta
${Number}    9010297520
${Pin_code}    516172
@{fruits}    apple banana orange mango dragonfruit kiwi
&{user}    Name=Bharath    age=29    city=Bangalore    course=python


*** Test Cases ***
welcome
  [Tags]    bharath
   inviting
   Log    test case one done
print fruits
  [Tags]    Bharath    anu
  Log To Console  \nmy favourite fruits
  FOR    ${fruit}    IN    @{fruits}
        Log To Console   ${fruit}
  END

user details
  [Tags]    Bharath
  Log    Name:${user.Name}
  Log    Age:${user.age}
  Log    city:${user.city}
  Log    course:${user.course}

add numbers test
  [Tags]    anu
  ${result}=    add two numbers    10    20
  Log To Console    Results is:${result}
  Should Be Equal As Numbers    ${result}    30

substraction test
  [Tags]    Bharath
  ${result}=    substraction of two numbers    30    10
  Log To Console    result is:${result}
  Should Be Equal As Numbers    ${result}    20

Division test
  [Tags]    Bharath    anu
  ${result}=    Division    20    10
  Log To Console    result is:${result}
  Should Be Equal As Numbers    ${result}    2

multiplication test
  [Tags]    Bharath
  ${result}=    product    10    20
  Log To Console    result is:${result}
  should be equal as numbers    ${result}    200


*** Keywords ***
inviting
  log    Hello!${Name}
  Log    age :${age}
  log    village:${village}
  Log    mob_no:${Number}
  log    pin code:${Pin_code}

add two numbers
   [Arguments]    ${x}    ${y}
   ${sum}=    Evaluate    ${x} + ${y}
   RETURN   ${sum}


substraction of two numbers
   [Arguments]    ${x}    ${y}
   ${sub}=    Evaluate    ${x} - ${y}
   RETURN    ${sub}


Division
  [Arguments]    ${x}    ${y}
  ${div}=    Evaluate    ${x} / ${y}
  RETURN    ${div}

product
  [Arguments]    ${x}    ${y}
  ${mul}=    Evaluate    ${x} * ${y}
  RETURN    ${mul}
