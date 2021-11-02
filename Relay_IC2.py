#I2C Relay PCB Test Code
#Graeme Peek
#11_2_2021
#Revision: 1.0.0
# Import various required libraries
import board
import time
import digitalio
import busio
 
from time import sleep  # Import sleep from time
from adafruit_mcp230xx.mcp23017 import MCP23017 # Import Adafruit MCP23017 Library
i2c = busio.I2C(board.SCL, board.SDA) # create istance of I2C object
#lock I2C bus
while not i2c.try_lock():
    pass
# Print addresses found
for i in i2c.scan():
    HighestAddress = i
    print("I2C Address Found:", hex(i))
# Unlock I2C Bus
i2c.unlock()
#print Highest I2C address found, this is the one we will use for the relay board.
print(HighestAddress)
# Create istanc of MCP23017 object
mcp = MCP23017(i2c, address= HighestAddress) # Instantiate mcp object with the correct bus address.
#mcp = MCP23017(i2c, address= 0x23) # Instantiate mcp object with the correct bus address. Use ths line for a fixed address (in this case fixed at 0x23)
time.sleep(3) # small delay to display addresses found, not required for function
Relay = [1,2,3,4,5,6,7,8,9] # Create array of relays
#loop through all 8 relays and setup IO for output
for i in range(1,9):
    Relay[i] = mcp.get_pin(i-1) #assign pin number of MCP23017 to each relay instance
    print("Relay ",i, " Configured")
    Relay[i].direction = digitalio.Direction.OUTPUT # set that pin as an output
time.sleep(3) # small delay before cycling hrough relays, not required for function
#loop forever
while True:
    #loop through all 8 relays
    for i in range(1,9):
        Relay[i].value = True #Turn relay on
        print("Relay ",i, " On") #display message relay turned on
        time.sleep(1) # wait 1 second
        Relay[i].value = False #Turn realy off
        print("Relay ",i, " Off") #Display message relay turned off
        time.sleep(1) # wait 1 second