*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Create User

*** Test Cases ***
Register With Valid Username And Password
    Set Username  user1
    Set Password  41wyj72r
    Confirm Password  41wyj72r
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  u2
    Set Password  65y8hyrx
    Confirm Password  65y8hyrx
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  user3
    Set Password  ve3l7j
    Confirm Password  ve3l7j
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  user4
    Set Password  fl8jeiol
    Confirm Password  xp9ng892
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Already Taken Username And Valid Password
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Register With Valid Username And Long Enough Password Containing Only Letters
    Set Username  user5
    Set Password  ecjbnerj
    Confirm Password  ecjbnerj
    Submit Credentials
    Register Should Fail With Message  Password must contain at least 1 digit

Login After Successful Registration
    Set Username  user6
    Set Password  heyzw18a
    Confirm Password  heyzw18a
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  user6
    Set Password  heyzw18a
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  user7
    Set Password  z8v3lt
    Confirm Password  z8v3lt
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long
    Go To Login Page
    Set Username  user7
    Set Password  z8v3lt
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Register Page And Create User
    Go To Register Page
    Register Page Should Be Open
    Create User  kalle  kalle123

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
