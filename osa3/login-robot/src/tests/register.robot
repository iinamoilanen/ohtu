*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input  kallee
    Input  kalle1234
    Run Application
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input  new
    Input  kalle
    Input  kalle123
    Run Application
    Output Should Contain  Username already exists

egister With Too Short Username And Valid Password
    Input  new
    Input  ka 
    Input  kalle1234
    Run Application
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input  new
    Input  Kalle
    Input  kalle1234
    Run Application
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input    new
    Input    kukka
    Input    k123
    Run Application
    Output Should Contain    Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input    new
    Input    kukka
    Input    kukkanen
    Run Application
    Output Should Contain    Password cannot consist of only letters