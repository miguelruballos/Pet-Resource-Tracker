# How to Build Pet Resource Tracker Device

The Pet Resource Tracker device is made up of multiple components. This guide will specify the components and their connections. 

 
| Pet Resource Tracker Device Diagram Overview      | Raspberry PI GPIO |
| ----------- | ----------- |
| <img src="./Image%20Files/pet_resource_tracker_device_diagram.png" width="800" />      | <img src="./Image%20Files/raspberry_pi_GPIO.png" width="200" />       |

## Pre-Requisites

*   1x Raspberry Pi with GPIO
*   2x HX711 weight scales with Load Cells pre-connected
*   1x LCD screen
*   4x Buttons
*   1x LEDs
*   1x Breadboard
*   12x Female to Female Jumper Wires
*   6x Male to Male Jumper Wires
*   5x Male to Female Jumper Wires
*   12x Female to Female Jumper Wires
*   1x Resistor


## How to Build Device
*   Step 1: Disconnect Raspberry PI from power.
*   Step 2: Connect first HX711 weight scale to GPIO with 4x Female to Female jumper wires.

	* **_HX711 to GPIO_**
	* GRD - GRD(6)
	* DT  - GPIO5
	* SCK - GPIO6
	* VCC - 3V3(1)
*   Step 3: Connect second HX711 weight scale to GPIO with 4x Female to Female jumper wires.
	* **_HX711 to GPIO_**
	* GRD - GRD(14)
	* DT  - GPIO(23)
	* SCK - GPIO(24)
	* VCC - 3v3(17)
*   Step 4: Connect LCD screen to GPIO with 4x Female to Female jumper wires.
	* **_LCD to GPIO_**
	* GRD - GRD(6)
	* VCC - 5V(4)
	* SDA - GPIO(3)
	* SCL - GPIO(2)
*   Step 5: Attach 4x Buttons to Breadboard.
	*  **_Button Pins to Breadboard_**  
	* Left Pins - Column E
	* Right pins - Column F
	* <img src="./Image%20Files/button_pins_to_breadboard.png" width="500" />
*   Step 6: Connect 4x Male to Male jumper cables from the button's bottom left row to the breadboard's negative rail. 
	* A7  - Adjacent Negative Rail
	* A11 - Adjacent Negative Rail
	* A15 - Adjacent Negative Rail
	* A19 - Adjacent Negative Rail
	* <img src="./Image%20Files/bottom_button_pins_to_negative_rail.png" width="500"  />
*   Step 7: Connect 4x Male to female jumper cables from the button's top left row to the GPIO.
	* A5  - GPIO16
	* A9  - GPIO20 
	* A13 - GPIO21
	* A17 - GPIO13
	* <img src="./Image%20Files/top_button_pins_to_gpio.png" width="500" />
*   Step 8: Attach 1x LED to breadboard.
	* **_LED to Breadboard_**  
	* Short pin - E22
	* Long pin - E23
*   Step 9: Connect 1x Male to Male jumper cable from the LEDs Short pin row to breadboard's negative rail.
	* A22 - Adjacent Negative Rail
	* <img src="./Image%20Files/top_row_led_to_negative_rail.png" width="500"  />
*   Step 10: Connect 1x Resistor from the LEDs Long pin row to lower column on breadboard.
	* B23 - B31
	* <img src="./Image%20Files/resistor_to_lower_row.png" width="500" />
	
* Step 11: Connect LEDs resistor row to GPIO.
	* A31 - GPIO(26)
	* <img src="./Image%20Files/resistor_to_gpio%20-%20Copy.png" width="500"  />
*   Step 8: Connect breadboard negative rail to GPIO.
	* **_Breadboard to GPIO_**   
	* Top Negative Rail Pinhole - Ground(34)
	* <img src="./Image%20Files//breadboard_negative_rail_to_gpio%20-%20Copy.png" width="500"  />

### Next Steps...

Complete [How to verify device functionality](How_to_verify_device_functionality.md)
