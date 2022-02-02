# How to Setup Google Sheets API
The Pet Resoruce Tracker uses Google Sheets API to upload weight data to a google sheets document. 

## Pre-Requisites
* Complete Pre-Requisites and _Step 1_ of [README](../README.md) document. 

To setup Google API, we need three items:

* Spread Sheet Link ID
* JSON Key
* Google Account

To get these items, complete Google's [Quick Start Tutorial ](https://developers.google.com/sheets/api/quickstart/python).

After completing the tutorial, implement the _Spread Sheet Link ID_ and the  _JSON Key_ path into the [Pet Resource Tracker Program Code](../pet_resource_tracker.py) downloaded in _Step 1_ from the [README](../README.md) document. 

## Spread Sheet Link ID

The _Spread Sheet Link ID_ must be placed on line 139.

![](./Image%20Files/spreadsheet_link.png)

## JSON Key

The path to the _JSON Key_ must be placed on line 133.  

![](./Image%20Files/json_key.png)

## Google Account

The Google Account is used to access the spreadsheet where the weight data is stored. This will be covered in the next steps. 

## Next Steps..
Proceed to _Step 3_ in [README](../README.md) document.
