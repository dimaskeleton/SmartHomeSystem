import threading
import random

'''
Purpose: Represents a device in a smart home system
Contract: 
    - turn_on() turns on the device
    - turn_off() turns off the device
    - get_status() returns the status of the device
'''


class SmartDevice:
    # Initializes an instance of SmartDevice
    def __init__(self, device_id, device_type):
        self.device_id = device_id  # Initializes device_id for each device
        self.device_type = device_type  # Initializes the device type
        self.status = "off"  # Initial status of device is set to 'off'
        self.lock = threading.Lock()  # Thread lock for safe modifications to device state

    # Turns on the device
    def turn_on(self):
        with self.lock:  # Lock before changing status
            self.status = "on"  # Set device status to 'on'

    # Turns off the device
    def turn_off(self):
        with self.lock:  # Lock before changing status
            self.status = "off"  # Set device status to 'off'

    # Gets and returns the status of the device
    def get_status(self):
        with self.lock:  # Lock before reading status
            return self.status  # Returns the status of the event


'''
Purpose: Represent a smart lightbulb with an adjustable brightness
Contract: 
    - turn_on() turns on the lightbulb
    - turn_off() turns off the lightbulb
    - change_brightness() changes the brightness of the lightbulb
'''


class Lightbulb(SmartDevice):
    # Initializes an instance of Lightbulb
    def __init__(self, device_id):
        super().__init__(device_id, "Smart Lightbulb")  # Initializes device type as "Smart Lightbulb"
        self.brightness = 0  # Initializes brightness to 0 as it's off

    # Turns on the lightbulb and prints the status
    def turn_on(self):
        super().turn_on()  # Turns device on through SmartDevice method
        self.brightness = 100  # Sets the brightness to 100
        # Prints status after turning on lightbulb
        print(f"{self.device_type} {self.device_id} turned on with brightness {self.brightness}%")

    # Turns off the lightbulb and prints the status
    def turn_off(self):
        super().turn_off()  # Turns device off through SmartDevice method
        self.brightness = 0  # Sets the brightness to 0
        print(f"{self.device_type} {self.device_id} turned off")  # Prints status after turning off the lightbulb

    # Changes the brightness of the lightbulb if it's on and prints the update
    def change_brightness(self, level):
        with self.lock:  # Lock before changing brightness
            if self.status == "on":  # Checks if the lightbulb is on, only changes brightness if on
                self.brightness = max(0, min(level, 100))  # Ensures brightness stays between 0 and 100
                # Prints the updated brightness of the bulb
                print(f"{self.device_type} {self.device_id} brightness adjusted to {self.brightness}%")
            else:
                # Prints message stating to turn on light to adjust the brightness
                print(f"{self.device_type} {self.device_id} is off. Please turn it on to change the brightness.")


'''
Purpose: Represent a thermostat with adjustable temperature settings
Contract:
    - turn_on() turns on the thermostat 
    - turn_off() turns off the thermostat
    - set_temperature() sets the temperature of the thermostat
'''


class Thermostat(SmartDevice):
    # Initializes an instance of thermostat
    def __init__(self, device_id):
        super().__init__(device_id, "Thermostat")  # Initializes device type as 'Thermostat'
        self.temperature = 65  # Sets default temperature to 65 degrees

    # Turns on the thermostat and prints the status
    def turn_on(self):
        super().turn_on()  # Turns thermostat on through SmartDevice method
        # Prints status after turning thermostat on
        print(f"{self.device_type} {self.device_id} turned on, temperature set to {self.temperature}°F")

    # Turns off the thermostat and prints the status
    def turn_off(self):
        super().turn_off()  # Turns thermostat off through SmartDevice method
        # Prints status after turning thermostat on
        print(f"{self.device_type} {self.device_id} turned off")

    # Sets the thermostat temperature and prints the update
    def set_temperature(self, temp):
        with self.lock:  # Lock before changing temperature
            self.temperature = temp  # Sets the new temperature
            # Prints the updated temperature of the thermostat
            print(f"{self.device_type} {self.device_id} temperature set to {self.temperature}°F")


'''
Purpose: Represent a security camera that can detect motion
Contract:
    - turn_on() turns on the security camera
    - turn_off() turns off the security camera 
    - detect_motion() detects motion in the security camera 
'''


class SecurityCamera(SmartDevice):
    # Initializes an instance of SecurityCamera
    def __init__(self, device_id):
        super().__init__(device_id, "Security Camera")  # Initializes device type as 'Security Camera'
        self.motion_detected = False  # Initializes boolean to detect motion, false at first

    # Turns on the security camera and prints the status
    def turn_on(self):
        with self.lock:  # Lock before changing status
            self.status = "active"  # Sets camera status to 'active'
            print(
                f"{self.device_type} {self.device_id} activated")  # Prints the status after turning on the security camera

    # Turns off the security camera and prints the status
    def turn_off(self):
        super().turn_off()  # Turns Security Camera off through SmartDevice method
        print(
            f"{self.device_type} {self.device_id} deactivated")  # Prints the status after turning off the security camera

    # Detects motion and prints the result
    def detect_motion(self):
        with self.lock:  # Lock before detecting motion
            self.motion_detected = bool(
                random.randint(0, 1))  # Randomly sets motion to True or False for accurate results
            # If motion is detected...
            if self.motion_detected:
                print(f"{self.device_type} {self.device_id} detected motion")  # Print message that motion was detected
            else:
                # If motion isn't detected, print message that motion was not detected
                print(f"{self.device_type} {self.device_id} no motion detected")
            return self.motion_detected  # Returns the result if motion was detected or not


'''
Purpose: Represent a TV with volume and input sources
Contract: 
    - turn_on() turns on the TV 
    - turn_off() turns off the TV
    - set_volume() changes the volume of the TV
    - change_source() changes the input source of the TV
'''


class Television(SmartDevice):
    # Initializes an instance of Television
    def __init__(self, device_id):
        super().__init__(device_id, "Television")  # Initializes device type as 'Television'
        self.volume = 30  # Initializes volume to 30
        self.input_source = "Cable"  # Initializes input source as 'Cable'

    # Turns the TV on and prints the status
    def turn_on(self):
        super().turn_on()  # Turns TV on through SmartDevice method
        # Prints the status of the TV after turning it on
        print(f"{self.device_type} {self.device_id} turned on. Volume: {self.volume}, Source: {self.input_source}")

    # Turns off the TV and prints the status
    def turn_off(self):
        super().turn_off()  # Turns TV off through SmartDevice method
        print(f"{self.device_type} {self.device_id} turned off")  # Prints the status of the TV after turning it off

    # Sets the volume of the TV and prints the updated volume
    def set_volume(self, volume):
        with self.lock:  # Lock before changing volume
            self.volume = max(0, min(volume, 100))  # Ensures volume stays between 0 and 100
            # Prints the volume status to the new value
            print(f"{self.device_type} {self.device_id} volume set to {self.volume}")

    # Changes the TV input source and prints the updated source
    def change_source(self, source):
        with self.lock:  # Lock before changing source
            self.input_source = source  # Sets the new input source
            # Prints the updated input source for the TV
            print(f"{self.device_type} {self.device_id} input source changed to {self.input_source}")


'''
Purpose: Represent a Refrigerator with temperature and door settings 
Contract: 
    - turn_on() turns on the refrigerator
    - turn_off() turns off the refrigerator
    - set_refrigerator_temp() updates the refrigerator temp.
    - set_freezer_temp() updates the freezer temp. 
    - door_status() updates the door status if it's open or closed 
'''


class Refrigerator(SmartDevice):
    # Initializes instance of Refrigerator
    def __init__(self, device_id):
        super().__init__(device_id, "Refrigerator")  # Initializes device type as 'Refrigerator'
        self.refrigerator_temp = 38  # Sets the refrigerator temperature to 38 degrees
        self.freezer_temp = 26  # Sets the freezer temperature to 26 degrees
        self.door_open = False  # Sets the door status to False indicating closed door

    # Turns on the refrigerator and prints the status of it
    def turn_on(self):
        super().turn_on()  # Turns on refrigerator through SmartDevice method
        # Prints the status of the refrigerator
        print(
            f"{self.device_type} {self.device_id} turned on. Refrigerator temp: {self.refrigerator_temp}°F, Freezer temp: {self.freezer_temp}°F")

    # Turns off the refrigerator and prints the status of it
    def turn_off(self):
        super().turn_off()  # Turns off refrigerator through SmartDevice method
        # Prints the status of turning it off
        print(f"{self.device_type} {self.device_id} turned off")

    # Sets the temperature of the refrigerator and prints the updated temperature
    def set_refrigerator_temp(self, temp):
        with self.lock:  # Lock before changing temp
            self.refrigerator_temp = temp  # Updates refrigerator temperature
            # Prints the updated temperature that refrigerator was set to
            print(f"{self.device_type} {self.device_id} refrigerator temperature set to {self.refrigerator_temp}°F")

    # Sets the temperature of the freezer and prints the updated temperature
    def set_freezer_temp(self, temp):
        with self.lock:  # Lock before changing temp
            self.freezer_temp = temp  # Updates freezer temp
            # Prints the updated temperature that the freezer was set to
            print(f"{self.device_type} {self.device_id} freezer temperature set to {self.freezer_temp}°F")

    # Change the status of the door and prints the status
    def door_status(self, is_open):
        with self.lock:  # Lock before changing status
            self.door_open = is_open  # Updates the door status
            status = "open" if self.door_open else "closed"  # Checks if the door is open or not
            # Prints the status of the door
            print(f"{self.device_type} {self.device_id} door is {status}")


'''
Purpose: Represent a lock that and be either locked or unlocked 
Contract:
    - locked() locks the current 'lock'
    - unlocked() unlocks the current 'lock'
    - get_locked_status() returns the status of the lock 
'''


class Lock(SmartDevice):
    # Initializes instance of Lock
    def __init__(self, device_id):
        super().__init__(device_id, "Lock")  # Initializes device type as 'Lock'
        self.is_locked = True  # Default lock status is closed

    # Locks the lock and prints the status
    def locked(self):
        with self.lock:  # Lock before changing is_locked
            self.is_locked = True  # Sets the lock to be 'Locked'
            # Prints the status of the lock
            print(f"{self.device_type} {self.device_id} is now locked.")

    # Unlocks the lock and prints the status
    def unlocked(self):
        with self.lock:  # Lock before changing is_locked
            self.is_locked = False  # Sets the lock to be 'Unlocked'
            # Prints the status of the lock
            print(f"{self.device_type} {self.device_id} is now unlocked.")

    # Returns the current lock status
    def get_lock_status(self):
        with self.lock:  # Lock before operation
            return "locked" if self.is_locked else "unlocked"  # Returns the lock status


'''
Purpose: Represent an air purifier with adjustable purification levels and fan speed
Contract:
    - turn_on() turns on the air purifier
    - turn_off() turns off the air purifier 
    - set_purification_level() sets the purification level setting
    - set_fan_speed() sets the fan speed to one of the options 
    - get_fan_speed() returns the status of the air purifier fan speed
'''


class AirPurifier(SmartDevice):
    # Initializes an instance of AirPurifier
    def __init__(self, device_id):
        super().__init__(device_id, "Air Purifier")  # Initializes device type as 'Air Purifier'
        self.purification_level = 0  # Initializes purification_level to 0
        self.fan_speed = 0  # Initializes fan_speed to 0

    # Turns on the AirPurifier and prints the status of it
    def turn_on(self):
        self.purification_level = 1  # Sets purification_level to 1 after turning on
        self.fan_speed = 1  # Sets fan_speed to 1 after turning on
        super().turn_on()  # Turns on the Air Purifier through SmartDevice method
        # Prints the status of the air purifier
        print(f"{self.device_id} turned on at purification level {self.purification_level} with fan speed {self.fan_speed}")

    # Turns off the AirPurifier and prints the status of it
    def turn_off(self):
        self.purification_level = 0  # Sets purification_level to 0
        self.fan_speed = 0  # Sets the fan_speed to 0
        super().turn_off()  # Turns off the Air Purifier through SmartDevice method

        # Prints the status of the air purifier
        print(f"{self.device_id} turned off")

    # Sets the purification level and prints the result of it
    def set_purification_level(self, level):
        with self.lock:  # Lock before changing air_purification_level
            self.purification_level = max(0, min(level, 3))  # Limited to 3 options for the air purifier
            # If the purification_level is greater than 0...
            if self.purification_level > 0:
                self.status = "on"  # The status of it is on

            # Prints the status of the updated purification level
            print(f"{self.device_type} purification level set to {self.purification_level}")

    # Sets the fan speed and prints the result of it
    def set_fan_speed(self, speed):
        with self.lock:  # Lock before changing fan speed
            self.fan_speed = max(0, min(speed, 3))  # Limited to 3 options for the fan speed
            # Prints the status of the updated fan speed
            print(f"{self.device_id} fan speed set to {self.fan_speed}")

    # Returns the purification status
    def get_purification_status(self):
        with self.lock:  # Lock before operation
            return self.purification_level  # Returns current purification level

    # Returns the fan_speed status
    def get_fan_speed(self):
        with self.lock:  # Lock before operation
            return self.fan_speed  # Returns fan speed status


'''
Purpose: Represent a Garage Door that can either be opened or closed 
Contract: 
    - open_door() opens the garage door
    - close_door() closes the garage door 
'''


class GarageDoor(SmartDevice):
    # Initializes instance of GarageDoor
    def __init__(self, device_id):
        super().__init__(device_id, "Garage Door")  # Initializes device type as 'Garage Door'
        self.is_open = False  # Initializes garage door status as closed/false

    # Opens the garage door and prints the status of it
    def open_door(self):
        with self.lock:  # Lock before changing garage door status
            self.is_open = True  # Sets garage door status to true
            self.status = "open"  # Sets the garage door status to 'open'
            print(f"{self.device_type} {self.device_id} is now open.")  # Prints the status of the garage door

    # Closes the garage door and prints the status of it
    def close_door(self):
        with self.lock:  # Lock before changing garage door status
            self.is_open = False  # Sets the garage door status to false
            self.status = "closed"  # Sets the garage door status to 'closed'
            print(f"{self.device_type} {self.device_id} is now closed.")  # Prints the status of the garage door
