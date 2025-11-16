*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input New Command And Create User
    Input    new
    Input    kalle
    Input    kalle123!
    Run Application

Input New Command
    Input    new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
