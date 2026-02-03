import time
from machine import Pin, ADC, SoftI2C
from ssd1306 import SSD1306_I2C
import urtc

#==== Init Devices ====
i2c0 = SoftI2C(scl=Pin(17), sda=Pin(16), freq=400000)
rtc = urtc.DS3231(i2c0)

i2c1 = SoftI2C(scl=Pin(3), sda=Pin(2), freq=400000)
display = SSD1306_I2C(128, 64, i2c1, addr=0x3c)

relay = Pin(15, Pin.OUT, value=1)   # start pump OFF
sm_sensor = ADC(Pin(28))

# ---- BST check ----
def is_bst(dt):
    month = dt[1]
    return 3 <= month <= 10


# ---- Set RTC to GMT (only run once) ----
def set_rtc_to_gmt_now(rtc):
    # SET THIS TO YOUR CURRENT GMT TIME ONLY ONCE
    # Format: (year, month, day, weekday, hour, minute, second, subsecond)
    rtc.datetime((2026, 1, 18, 7, 16, 59, 0, 0))
    print("RTC set to GMT")

# Uncomment the line below and run once to set RTC
#set_rtc_to_gmt_now(rtc)


while True:
    moisture_value = sm_sensor.read_u16()
    print("Soil Moisture:", moisture_value)
    
    if moisture_value > 24000:
        print("Soil is dry! Turning ON pump")
        relay.value(0)
        time.sleep(3.5)
        relay.value(1)
        
        # Get current date/time from RTC
        t = rtc.datetime()
        date_str = f"{t[2]}/{t[1]}/{t[0]}"

        # BST adjust only for display
        hour = t[4]
        if is_bst(t):
            hour += 1
            if hour == 24:
                hour = 0

        time_str = f"{hour:02d}:{t[5]:02d}"
        
        with open("WateringEvents.txt", "w") as f:
            f.write(date_str + "\n")
            f.write(time_str + "\n")
        
    else:
        print("Enough Moisture, Pump OFF")
        relay.value(1)
        
    try:
        with open("WateringEvents.txt", "r") as fr:
            FirstLine = fr.readline().strip()
            SecondLine = fr.readline().strip()
    except:
        FirstLine, SecondLine = "No record", ""
    
    display.fill(0)
    display.text("Plant was last", 10, 6)
    display.text("watered on:", 10, 16)
    display.text(FirstLine + " at", 10, 26)
    display.text(SecondLine, 10, 36)
    display.text("Moisture:" + str(moisture_value), 10, 46)
    display.show()
    
    time.sleep(60)
