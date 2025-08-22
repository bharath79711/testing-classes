*** Settings ***

Library    collections
Library    string
Library   OperatingSystem
Library    Process
Library    SSHLibrary


*** Variables ***

${command}    python    C:/PycharmProjects/bharath/testing-classes/word_count.py


*** Test Cases ***

To check by using help command
  [Documentation]    to check by using --help command
  [Tags]    count

  ${result}=    Run    ${command} --help

  should contain    ${result}    usage: word_count.py [-h] [--sentence SENTENCE]

  Should Contain    ${result}    count of words in sentence

To check by using sentence without quatation marks
  [Documentation]    To taking sentence without quatation marks
  [Tags]    count

  ${result}=    Run    ${command} --sentence python is high level programming language

  should contain    ${result}    usage: word_count.py [-h] [--sentence SENTENCE]
  Should Contain    ${result}     word_count.py: error: unrecognized arguments: is high level programming language

To check possitive scenario by passing sentence
  [Documentation]    To check by using sentence
  [Tags]    count

  ${result}=    Run    ${command} --sentence "python is high level programming language"

  Should Contain    ${result}    word: python
  Should Contain    ${result}    total words: 6


To check by without passing any sentence
  [Documentation]    To check by without passing sentence
  [Tags]    count

  ${result}=    Run    ${command} --sentence

  Should Contain    ${result}    usage: word_count.py [-h] [--sentence SENTENCE]
  Should Contain    ${result}    word_count.py: error: argument --sentence: expected one argument


To check by passing numbers in place of sentence
  [Documentation]    to check by passing numbers in place of sentence
  [Tags]    count

  ${result}=    Run    ${command} --sentence "12 122 122 1222 12 122 122 12"

  Should Contain    ${result}    word: 12
  Should Contain    ${result}    total words: 8







