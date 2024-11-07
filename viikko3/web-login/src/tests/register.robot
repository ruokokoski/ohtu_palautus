*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation    kalle1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle1234
    Set Password Confirmation    kalle1234
    Submit Credentials
    Register Should Fail With Message    Too short username

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation    kalle12
    Submit Credentials
    Register Should Fail With Message    Too short password

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallepalle
    Set Password Confirmation    kallepalle
    Submit Credentials
    Register Should Fail With Message    Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation    kalle123
    Submit Credentials
    Register Should Fail With Message    Passwords do not match

Register With Username That Is Already In Use
    Set Username  teemu
    Set Password  teemu1234
    Set Password Confirmation    teemu1234
    Submit Credentials
    Register Should Fail With Message    Username in use

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation    kalle1234
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kalle
    Set Password  kalle1234
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation    kalle123
    Submit Credentials
    Click Link  Login
    Set Username  kalle
    Set Password  kalle1234
    Submit Login
    Login Should Fail With Message    Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  teemu  teemu1234
    Go To Register Page

Go To Register Page
    Go To    ${REGISTER_URL}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Register Should Succeed
    Title Should Be    Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
