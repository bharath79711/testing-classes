*** Settings ***

Library    collections
Library    string
Library   OperatingSystem
Library    Process
Library    SSHLibrary

*** Variables ***
${command}    python    C:/PycharmProjects/bharath/testing-classes/sentence_dict_count.py




*** Test Cases ***
To check the help message using --helpp command
  [Documentation]    To check the out put by using help command
  [Tags]    char_count

  ${result}=    Run    ${command} --help
  should contain    ${result}    usage: sentence_dict_count.py [-h] [--sentence SENTENCE]
  should contain    ${result}    count the characters in a sentence

To check possitive scenario by passing --sentence
   [Documentation]    To check buy passing sentence
   [Tags]    char_count

   ${result}=    Run    ${command} --sentence "python is good skill"

   Should Contain    ${result}    char p : 1
   Should Contain    ${result}    char l : 2


To check passing by numbers
   [Documentation]    To check by passing numbers in  strng format
   [Tags]    char_count

   ${result}=    Run    ${command} --sentence "123 123 4567"

   should contain    ${result}    char 1 : 2
   should contain    ${result}    char 7 : 1

To check without passing any sentence
   [Documentation]    without taking any sentence
   [Tags]    char_count

   ${result}=    Run    ${command} --sentence

   should contain    ${result}    usage: sentence_dict_count.py [-h] [--sentence SENTENCE]
   should contain    ${result}    sentence_dict_count.py: error: argument --sentence: expected one argument


To check without mention sentence in quation

   [Documentation]    to take sentence without qutation marks
   [Tags]    char_count

   ${result}=    Run    ${command} --sentence python is good
   Should Contain    ${result}    usage: sentence_dict_count.py [-h] [--sentence SENTENCE]
   Should Contain    ${result}    sentence_dict_count.py: error: unrecognized arguments: is good


