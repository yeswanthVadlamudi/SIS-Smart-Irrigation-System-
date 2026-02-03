# SIS-Smart-Irrigation-System-
Automated Plant Watering System 🌱💧

![20260203_171039](https://github.com/user-attachments/assets/5be49317-3d2c-4877-8a02-04f248a7855e)

This project is an automated plant watering system using a microcontroller, soil moisture sensor, relay-controlled water pump, and an OLED display. It monitors soil moisture in real-time and waters your plants automatically when the soil is dry.

Features

Automatic watering: Turns on the pump when soil moisture drops below a set threshold.

Soil moisture monitoring: Continuously reads soil moisture values using an analog sensor.

Event logging: Records the date and time of the last watering to a WateringEvents.txt file.

Time display with BST adjustment: Shows current date and time on an SSD1306 OLED display, with optional British Summer Time adjustment.

Customizable threshold: Adjust the moisture threshold and watering duration according to your plant’s needs.

Hardware Required

Microcontroller compatible with MicroPython (e.g., Raspberry Pi Pico W)

Soil moisture sensor

Relay module (for controlling a water pump)

Water pump

SSD1306 OLED display (I2C interface)

Connecting wires

Software / Libraries Used

MicroPython

machine (Pin, ADC)

ssd1306 for OLED display

urtc for RTC (DS3231)

How It Works

The system reads the soil moisture sensor every minute.

If the moisture value is above the threshold (dry soil), the relay is activated to turn on the water pump for a fixed duration.

The watering event is logged to a file with date and time.

The OLED display shows:

Last watering date and time

Current soil moisture

Optional Setup

Setting RTC to GMT: Run the set_rtc_to_gmt_now(rtc) function once to sync the RTC.

BST adjustment: Automatically adds 1 hour for months between March and October when displaying time.

Future Improvements

Push watering logs to a cloud database for remote monitoring.

Add Wi-Fi notifications or alerts when the soil is dry.

Support multiple plants with independent sensors and pumps.
