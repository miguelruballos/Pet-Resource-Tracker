# How to Setup Google Sheets API
The Pet Resource Tracker uses Google Sheets API to upload weight data to a Google Sheets spreadsheet. This document will guide you with: 
* Completing Google Sheets API Tutorial
* Importing the Dashboard Spreadsheet
* Implementing Google API information to the Pet Resource Tracker source code. 

## Pre-Requisite
* Complete _Pre-Requisites_ and _Step 1_ from the [README](../README.md) document. 


### Google Sheets API Tutorial
* Step 1: Complete Google's [Quick Start Tutorial ](https://developers.google.com/sheets/api/quickstart/python).
  * After completing the tutorial, you will receive the following items:
    * Google Account
    * Spread Sheet Link ID
    * JSON Key

### Import the Dashboard Spreadsheet
* Step 2: Log into Google Sheets with _Google Account_.
* Step 3: Using the _Spread Sheet Link ID_, open the spreadsheet.
* Step 4: Import the [Dashboard Spreadsheet Template](../API%20Setup/dashboard_spreadsheet.xlsx).
  * `File>Import` 
### Implement _Spread Sheet Link ID_ and the  _JSON Key_ into the Pet Resource Tracker Program
The package downloaded in _Step 1_ from the [README](../README.md) document includes the program's source code file called [pet_resource_tracker.py](../pet_resource_tracker.py).

* Step 5: Place the _Spread Sheet Link ID_ on line 139.
  * ![](Image%20Files/spreadsheet_link.png)

* Step 6: Place the path to the _JSON Key_ on line 133.  
  * ![](Image%20Files/json_key.png)

## Next Steps..
Proceed to _Step 3_ in [README](../README.md) document.
