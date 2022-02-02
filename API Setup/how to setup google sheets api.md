# How to Setup Google Sheets API
The Pet Resoruce Tracker uses Google Sheets API to upload weight data to a google sheets document. To setup Google API, we need three items:

* Spread Sheet Link ID
* JSON Key
* Google Account

To get these items, complete Google's [Quick Start Tutorial ](https://developers.google.com/sheets/api/quickstart/python).

After completing the tutorial, implement the items into the [Pet Resource Tracker python program](./pet_resource_tracker.py). 

## Spread Sheet Link ID

The _Spread Sheet Link ID_ must be placed on line 139.

![](Build%20and%20Verify%20Device/Image%20Files/spreadsheet_link.png)

## JSON Key

The path to the _JSON Key_ must be placed on line 133.

![](Build%20and%20Verify%20Device/Image%20Files/json_key.png)

## Google Account

The Google Account is used to access the spreadsheet where the weight data is stored. 
