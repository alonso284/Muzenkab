# Welcome to Muzenkab

Muzenkab is a web application that facilites collectibles exchange between your friends and other communities. Muzenkab achieves this by letting you know what items your friends have available for exchange and which ones they want. For example, imagine you are collecting stamps to complete your FWC Qatar 2022 Album; you have some repeated stamps and are willing to exchange them for stamps that you are missing. Muzenkab allows you and your friends to register which cards you all have available, and recommends exchanges based on that information.

Muzenkab is design for easy use and understanding, and to be fast and dynamic.

# Future Vision

Right now, Muzenkab only allows you to exchange FWC Qatar 2022 stamps. However, we are working to expand it to other collection items, such as Pokemon, Magic and Digimon cards or Rocket League and COD skins and items.

# API

## /login POST

### form entries

| Name     | Type   | Max-Size |
|----------|--------|----------|
| Username | string | 20       |
| Password | string | 20       |

### Return Messages

| Code | Return Message    |
|------|-------------------|
| 400  | Already Logged In |
| 401  | Login Failed      |
| 200  | Login Successful  |

## /logout POST

| Code | Return Message    |
|------|-------------------|
| 200  | Logout Successful |

## /signup POST

### form entries

| Name      | Type   | Max-Size |
|-----------|--------|----------|
| FirstName | string | 20       |
| LastName  | string | 20       |
| Username  | string | 20       |
| Password  | string | 32       |
| CellPhone | string | 15       |
| Email     | string | 50       |

### Return Messages

| Code | Return Messge        |
|------|----------------------|
| 400  | User Already Exists  |
| 401  | Invalid Entry        |
| 200  | Created Successfully |

## /user/\<Username\> GET

## Return Messages

| Code | Return Messge  |
|------|----------------|
| 400  | User Not Found |
| 200  | User Info      |

## JSON Return

```json
{
    "PersonID": 1,
    "FirstName": "John",
    "LastName": "Luke",
    "Username": "JohnLuke94",
    "Password": "password",
    "CellPhone": "012356789",
    "Email": "JohnLuke@muzenkab.click",
    "PartyID1": null,
    "PartyID2": null,
    "PartyID3": null,
    "PartyID4": null,
    "PartyID5": null,
    "QAT_IN": "00000000000000000000",
    "QAT_OUT": "00000000000000000000",
    "ECU_IN": "00000000000000000000",
    "ECU_OUT": "00000000000000000000",
    "SEN_IN": "00000000000000000000",
    "SEN_OUT": "00000000000000000000",
    "NED_IN": "00000000000000000000",
    "NED_OUT": "00000000000000000000",
    "ENG_IN": "00000000000000000000",
    "ENG_OUT": "00000000000000000000",
    "IRN_IN": "00000000000000000000",
    "IRN_OUT": "00000000000000000000",
    "USA_IN": "00000000000000000000",
    "USA_OUT": "00000000000000000000",
    "WAL_IN": "00000000000000000000",
    "WAL_OUT": "00000000000000000000",
    "ARG_IN": "00000000000000000000",
    "ARG_OUT": "00000000000000000000",
    "KSA_IN": "00000000000000000000",
    "KSA_OUT": "00000000000000000000",
    "MEX_IN": "00000000000000000000",
    "MEX_OUT": "00000000000000000000",
    "POL_IN": "00000000000000000000",
    "POL_OUT": "00000000000000000000",
    "FRA_IN": "00000000000000000000",
    "FRA_OUT": "00000000000000000000",
    "AUS_IN": "00000000000000000000",
    "AUS_OUT": "00000000000000000000",
    "DEN_IN": "00000000000000000000",
    "DEN_OUT": "00000000000000000000",
    "TUN_IN": "00000000000000000000",
    "TUN_OUT": "00000000000000000000",
    "ESP_IN": "00000000000000000000",
    "ESP_OUT": "00000000000000000000",
    "CRC_IN": "00000000000000000000",
    "CRC_OUT": "00000000000000000000",
    "GER_IN": "00000000000000000000",
    "GER_OUT": "00000000000000000000",
    "JPN_IN": "00000000000000000000",
    "JPN_OUT": "00000000000000000000",
    "BEL_IN": "00000000000000000000",
    "BEL_OUT": "00000000000000000000",
    "CAN_IN": "00000000000000000000",
    "CAN_OUT": "00000000000000000000",
    "MAR_IN": "00000000000000000000",
    "MAR_OUT": "00000000000000000000",
    "CRO_IN": "00000000000000000000",
    "CRO_OUT": "00000000000000000000",
    "BRA_IN": "00000000000000000000",
    "BRA_OUT": "00000000000000000000",
    "SRB_IN": "00000000000000000000",
    "SRB_OUT": "00000000000000000000",
    "SUI_IN": "00000000000000000000",
    "SUI_OUT": "00000000000000000000",
    "CMR_IN": "00000000000000000000",
    "CMR_OUT": "00000000000000000000",
    "POR_IN": "00000000000000000000",
    "POR_OUT": "00000000000000000000",
    "GHA_IN": "00000000000000000000",
    "GHA_OUT": "00000000000000000000",
    "URU_IN": "00000000000000000000",
    "URU_OUT": "00000000000000000000",
    "KOR_IN": "00000000000000000000",
    "KOR_OUT": "00000000000000000000"
}
```

## /editUser

### form entries

| Name        | Type   | Max-Size |
|-------------|--------|----------|
| FirstName   | string | 20       |
| LastName    | string | 20       |
| Username    | string | 20       |
| OldPassword | string | 32       |
| NewPassword | string | 32       |
| CellPhone   | string | 15       |
| Email       | string | 50       |

### Return Messages

| Code | Return Messge  |
|------|----------------|
| 400  | User Not Found |
| 200  | User Info      |

## /joinParty

## form entries

| Name    | Type | Max-Size |
|---------|------|----------|
| PartyID | int  | 64-bit   |

## Erros Messages

| Code | Return Messge                 |
|------|-------------------------------|
| 400  | No User in Session            |
| 401  | User Already in Party         |
| 402  | No Space Available In Party   |
| 200  | Added {PersonID} to {PartyID} |