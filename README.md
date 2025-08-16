Testing:
1) Manuall testing
2) Automation Testing 
    ==>two Frameworks
        1)Pytest
        2)Robot Framework
        ==> To test UI using selinum library ==> pytest selenium, robotframework selinum
        ==> To test CLI(Command line interfaces) ==>pytest,robotframework

->
1) Regression testing: to test entire application testcases
2) Sanity Testing: To test particular feature testcases
-> 
Quality Check
  - Application we have to analysis and prepare multiple testcases
  - once testcases prepared based on requirement we have to go either manuall testing or automation testing

->
Unit Testing:
- to test the functions or classes working fine or not which is developed by developer
Coverage :
- developer developed code we should cover at least 80% code of unit testcases
- coverage run test.py
- coverage report
- coverage run -m unittest discover
- coverage report
- coverage html
"""

def func_squa(x, y):
    return x * y

testfile
import unittest

from numpy.ma.testutils import assert_equal

from unit_concept import *

class TestConcept(unittest.TestCase):

def test_func_squa(self):
        data = func_squa(10,20)
        assert data==200

def test_func_squa_negitive(self):
        data = func_squa(0,10)
        assert_equal(data,0)
--------------------------------------------------------------------------------------

SDLC ==> Software Development Life Cycle
-----
1) Requirement Phase
2) Analysis Phase
3) Design Phase
4) Development Phase
5) Testing Phase
6) Deployment Phase


STLC ==> Software Testing Life Cycle
-------
1) Requirement Phase
2) Test Analysis Phase
3) Test Design
4) Test Env Setup
5) Test Execution
6) Test Closure

Methodologies:
------------------
1) Waterfall methodology: Any changes in between not possible
2) Agile Methodology: Any changes in between possible


Agile Methodology: Jira tool using manging
---------------------
    Product owner : Application end to end 
    
    Epic:  ==> requirement tool :- confluence 
    -----------------
    - Feature 1 ==> 
    - Feature 2
    - Feature 3
    - Feature 4...
    
    Scrum Master: who manages sprint planning, std meetings,retrospective meeting
    
    Sprint Planning Meeting: Sprint:- 10 days or 2 weeks ==> 210 hours ==> 13 to 26 th month
    -----------------------
    - Feature 1 => Anu      ==> 70 Hours ==> 5hours,5 hours ==> burns ==> Jira tasks ==> Description
    - Feature 2 ==> Bharath ==> 70 hours
    - Feature 3 ==> my      ==> 50 hours
    - Feature 4 ==> my     ==> 20 hours
    
    Product Owner:- Sprint review meeting
    -------------------------
    
    Std up meeting: Every day meetings  15 min
    --------------
        - what you have worked yesterday
        - what you are going to do 
        - any blockers
        
    Retrospective Meeting: 
    ------------------------------
        - What went well in last sprint
        - what not went well in last sprint
    
    DOD: Definition of Done:
    ---------------------
        - feature 1 :developing, testing, reviewing, deployment, product owner review 100%
    
    Product Backlog
    ----------------
    - Feature 4
    - Feature 5
    - Feature 6...
    
______________________________________________________________________________

To install robot framework and library
pip install robotframework
pip install --upgrade robotframework-seleniumlibrary
Ends with .robot file extension


# Execute Test Case with Robot

robot -d Results/   tests/robot_test.robot  ==> To run all *** Test Cases ***
robot -d results   -i tag_name test_dir 


# Usage 1:- Variables,Settings, Test Case with Keywords

The variable type identifier is used to define the type of the variable.

$ is used for scalar variables.
@ is used for list variables.
& is used for dictionary variables.
% is used for environment variables.


robot
*** Settings ***
Library    SeleniumLibrary
Documentation    We are using in this way both variables and keywords in testcase itself

*** Variables ***
${variable_name}    variable_value

*** Test Cases ***
Test Case Name
    [Documentation]    This test case just for testing
    [Tag]   tage_name1  tage_name2
    Keyword name    keyword value

Test Case Name 2
    Keyword name    keyword value ${variable_name}

*** Keywords ***




# Usage 2:- keywords Separate
robot
*** Settings ***
Library    SeleniumLibrary
Documentation    Keyword splitting to separate way instead keeping in Testcases

*** Variables ***
${variable_name}    variable_value

*** Test Cases ***
Test Case Name
    [Documentation]    This test case just for testing
    [Tag]   tage_name1  tage_name2
    Keyword_name1
    
Test Case Name 2
    Keyword_name2

*** Keywords ***
Keyword_name1
    Log     hellow grudeva
Keyword_name2
    Log    ${variable_name}   

-------------------------------------------------------------------------------------
*** Settings ***
Library SSHLibrary
Library Collections
Library String
Library BuiltIn
Library OperatingSystem
Library Process


*** Variables ***
${x}    10
${y}    20
@{villages}    rvp    msm    mpl


*** Test Cases ***
Summing of two variables
    [Documentation]    summing of x and y
    [Tags]    anu    bharath
    Log    ${x}
    Log    ${villages}

Multiplications of two variables
    [Documentation]    summing of x and y
    [Tags]    anu
    Log    ${y}
    Should Contain    reddy vari palli madanapalli avulavari pa;llli    reddy
    # pre defined keywords

Divide of two variables
    [Documentation]    summing of x and y
    [Tags]    anu
    Check the strings

Factor of two variables
    [Documentation]    summing of x and y
    [Tags]    anu
    Check the strings

*** Keywords ***
Check the strings
    [Documentation]    Custom keywords
    Should Not Contain    reddy vari palli madanapalli avulavari pa;llli    bharath
    Should Not Contain    reddy vari palli madanapalli avulavari pa;llli    anu

---------------------------------------------------------------------------------
import argparse

def function(username,password,age):
    print(f"{username} is username")
    print(f"{password} is password")
    age_sq = int(age)*2
    return username, password,age_sq


if _name_ =="_main_":
    parser = argparse.ArgumentParser(description="Taking user details ")
    parser.add_argument('--username', required=True, help='Username fo the Page')
    parser.add_argument('--password', required=True, help='Password for the page ')
    parser.add_argument('--age', required=True, help='age')

    args = parser.parse_args()
    data = function(args.username,args.password,args.age)
    print(data)


====================
Testcases
===============
1) To check the help message using --help command
2) To check the help message using --h command
3) To Check negitive scenioria by only passing few arguments
4) To Check user validation by passing all arguments
5) To Check uservalidations by passing invalid argument values


Mannuall testing
==========================
1) To check the help message using --help command
python uservalidations.py --help
usage: uservalidations.py [-h] --username USERNAME --password PASSWORD --age AGE

Taking user details

options:
  -h, --help           show this help message and exit
  --username USERNAME  Username fo the Page
  --password PASSWORD  Password for the page
  --age AGE            age

2)  To check the help message using --h command
python uservalidations.py --h
usage: uservalidations.py [-h] --username USERNAME --password PASSWORD --age AGE

Taking user details

options:
  -h, --help           show this help message and exit
  --username USERNAME  Username fo the Page
  --password PASSWORD  Password for the page
  --age AGE            age

3) To Check negitive scenioria by only passing few arguments

python uservalidations.py --username reddy
usage: uservalidations.py [-h] --username USERNAME --password PASSWORD --age AGE
uservalidations.py: error: the following arguments are required: --username, --password, --age

4) To Check user validation by passing all arguments

python uservalidations.py --username reddy --password btr --age 20
thirumala is username
reddy is password
('thirumala', 'reddy', 40)

5) To Check uservalidations by passing invalid argument values

python uservalidations.py --username reddy --password btr --age data
ValueError: invalid literal for int() with base 10: 'data'