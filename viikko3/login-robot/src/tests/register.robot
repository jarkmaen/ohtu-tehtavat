*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user1  5yunhn4o
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  u2  v9eg1y3l
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  user3  wo5ibk
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user4  zcrleywm
    Output Should Contain  Password must contain at least 1 digit

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
