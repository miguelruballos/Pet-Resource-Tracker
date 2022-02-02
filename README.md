# Pet Resource Tracker

The _Pet Resource Tracker_ is a python program that captures weight data and uploads the data with Google Sheets API. The program runs on a Raspbery Pi that interfaces with HX711 weight scales. 

![](/Build%20and%20Verify%20Device/Image%20Files/system_overview.png)
## Pre-Requisites

*   Complete [How to Build Device](/Build%20and%20Verify%20Device/How_to_Build_Device.md)
*   Complete [How to Verify Device Functionality](/Build%20and%20Verify%20Device/How_to_verify_device_functionality.md)

## Installation

*   Step 1:  Download the current package. 
    *   `gh repo clone miguelruballos/Pet-Resource-Tracker`
*   Step 2: Complete [How to setup Google Sheets API](/API%20Setup/how%20to%20setup%20google%20sheets%20api.md)
*   Step 3: Run the program
    *   `python pet_resource_tracker.py`
*   Step 4: [Use the Pet Tracker!](/How%20to%20Use%20Pet%20Resource%20Tracker/how_to_use_pet_resource_tracker.md)
