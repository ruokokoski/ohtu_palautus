*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  teemu
    Set Password  teemu1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

*** Keywords ***
Reset Application Create User And Go To Login Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page
