*** Settings ***

Library    collections
Library    string
Library   OperatingSystem
Library    Process
Library    SSHLibrary

*** Variables ***

${command}    python C:/PycharmProjects/bharath/testing-classes/mul_arg_diff_typ.py


*** Test Cases ***

To check the help message using --help command
  [Documentation]    to check by using help command
  [Tags]    BK

  ${result}=    Run    ${command} --help

  should contain    ${result}    usage: mul_arg_diff_typ.py [-h] [--name NAME] [--village VILLAGE]

   should contain    ${result}    different types of arguments


To check possitive scenario by passing all arguments
  [Documentation]    to check by passing all argumennts
  [Tags]    BK

  ${result}=    Run    ${command} --name Bharath --village chintakunta --city Bangalore --age 18 --marks 90

  Should Contain    ${result}    name: Bharath
  Should Contain    ${result}    first class

To check by using few arguments
  [Documentation]    to check by passing two arguments
  [Tags]    BK

  ${result}=    Run    ${command} --name Bharath --village chintakunta

  Should Contain    ${result}    Traceback (most recent call last):
  should contain    ${result}    TypeError: '>=' not supported between instances of 'NoneType' and 'int'


To check by using age is less than 18
  [Documentation]    to check by taking age is less than 18
  [Tags]    BK

  ${result}=    Run    ${command} --name Bharath --village chintakunta --city Bangalore --age 15 --marks 90

  should contain    ${result}    age can't be less than 18

To check age in form of string
  [Documentation]    to check in place of age is string
  [Tags]    BK
  ${result}=    Run    ${command} --name Bharath --village chintakunta --city Bangalore --age bk --marks 90

  Should Contain    ${result}    mul_arg_diff_typ.py: error: argument --age: invalid int value: 'bk'
  should contain    ${result}    usage: mul_arg_diff_typ.py [-h] [--name NAME] [--village VILLAGE]