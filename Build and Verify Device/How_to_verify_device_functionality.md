# How to Verify Device Functionality 

Verify device functionality by running a program that perfroms a series of checks. Verify the the appropriate messages appear on the LCD screen. 

## Pre-Requisite
* Complete [How to Build Device](How_to_Build_Device.md) 
* Download [Build Verification Program](verify_device_functionality_program.py)

## Steps

* Step 1: Run the verification program on  Raspberry Pi
	* `python verify_device_functionality_program.py`
* Step 2: Verify the following messages appear:
	* Setting up Device
	*   Set Zero: Sucess  
		Set Ratio: Sucess
+  Step 3: Verify the following weight measurements appear:
	*  Scale 1: 0 g  
	   Scale 2: 0 g
* Step 4: Place object of known weight on both weight scales and verify accuracy of weight measurement.
* Step 5: Press Button 1
	* Verify the following message appears:
		* Button 1 Pressed 
- Step 6: Press Button 2
	* Verify the following messages appear:
		* Button 2 Pressed
		* Set Zero: Sucess  
		Set Ratio: Sucess
* Step 7: Press Button 3
	*  Verify the following message appears:
		-  Button 3 Pressed
+  Step 8: Press Button 4
  	* Verify green LED turns on.
	+  Verify the following message appears:
		*  Green Light On
		*  Button 4 Pressed
		
## Troubleshooting
*  If you experience errors, please refer to [How to Build Device](How_to_Build_Device.md) to verify proper connections. 
## Next Steps..
Complete steps in [README](../blob/main/README.md)
