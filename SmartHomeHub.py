from Devices import *
import threading

'''
Purpose: Act as a central hub and management system for all the devices in the smart home
Contract:
    - add_device() adds a new device to the smart home system
    - remove_device() removes a device from the smart home system
    - get_device_status() returns the status of a given device 
    - send_command() sends a command to be executed by the given device class
    - execute_device_command() executes the given command if the device can receive it 
'''


class SmartHomeHub:
    # Initializes instance of SmartHomeHub
    def __init__(self):
        self.devices = {}  # Dictionary to store all the devices with device_id as a key and device as value
        self.lock = threading.Lock()  # Lock to keep dictionary modifications safe
        self.threads = []  # List to keep track of the threads

    # Adds a new device to the smart home system
    def add_device(self, device):
        with self.lock:  # Lock before adding the device
            # If the device doesn't exist in the system...
            if device.device_id not in self.devices:
                self.devices[device.device_id] = device  # Add it to the devices dictionary
                print(f"Device {device.device_id} added.")  # Print updated status that device was added
            else:
                print(
                    f"Device {device.device_id} already exists in the system.")  # Message if the device already exists

    # Removes an existing device from the smart home system
    def remove_device(self, device_id):
        with self.lock:  # lock before removing device
            # If the device is found in the devices dictionary...
            if device_id in self.devices:
                del self.devices[device_id]  # Remove that device from it
                print(f"Device {device_id} removed.")  # Prints updated status that device was removed
            else:
                print(f"Device {device_id} not found in the system.")  # Message if the device isn't found in the system

    # Gets and returns the status of a given device
    def get_device_status(self, device_id):
        with self.lock:  # Lock before getting status
            # If the device is in the devices dictionary...
            if device_id in self.devices:
                return self.devices[device_id].get_status()  # Returns the status of it
            else:
                print(f"Device {device_id} not found in the system.")  # Message if the device isn't found in the system
                return None  # Returns None since device doesn't exist

    # Send a command to the given device to be executed
    def send_command(self, device_id, command, *args):
        with self.lock:  # Lock before sending command
            # If the device is found in the devices dictionary...
            if device_id in self.devices:
                device = self.devices[device_id]  # Sets device to a device_id
                # Creates a new thread to execute the command
                thread = threading.Thread(target=self.execute_device_command, args=(device, command) + args)
                self.threads.append(thread)  # Add the thread to the list of threads
                thread.start()  # Start the thread
            else:
                print(f"Device {device_id} not found in the system.")  # Message if the device isn't found in the system

    # Executes the given command on the specific device, if command isn't applicable prints an error
    def execute_device_command(self, device, command, *args):
        # if-elif statements to link the command to the specific device passing the arguments through it
        if command == "turn_on":
            device.turn_on()
        elif command == "turn_off":
            device.turn_off()
        elif command == "set_temperature" and isinstance(device, Thermostat):
            device.set_temperature(*args)
        elif command == "change_brightness" and isinstance(device, Lightbulb):
            device.change_brightness(*args)
        elif command == "detect_motion" and isinstance(device, SecurityCamera):
            device.detect_motion()
        elif command == "set_volume" and isinstance(device, Television):
            device.set_volume(*args)
        elif command == "change_source" and isinstance(device, Television):
            device.change_source(*args)
        elif command == "set_refrigerator_temp" and isinstance(device, Refrigerator):
            device.set_refrigerator_temp(*args)
        elif command == "set_freezer_temp" and isinstance(device, Refrigerator):
            device.set_freezer_temp(*args)
        elif command == "door_status" and isinstance(device, Refrigerator):
            device.door_status(*args)
        elif command == "lock" and isinstance(device, Lock):
            device.locked()
        elif command == "unlock" and isinstance(device, Lock):
            device.unlocked()
        elif command == "get_lock_status" and isinstance(device, Lock):
            device.get_lock_status()
        elif command == "set_purification_level" and isinstance(device, AirPurifier):
            device.set_purification_level(*args)
        elif command == "set_fan_speed" and isinstance(device, AirPurifier):
            device.set_fan_speed(*args)
        elif command == "get_fan_speed" and isinstance(device, AirPurifier):
            device.get_fan_speed()
        elif command == "get_purification_status" and isinstance(device, AirPurifier):
            device.get_purification_status()
        elif command == "open_door" and isinstance(device, GarageDoor):
            device.open_door()
        elif command == "close_door" and isinstance(device, GarageDoor):
            device.close_door()

        # If the command isn't supported for a specific device, prints an error
        else:
            print(f"Command '{command}' not supported for device {device.device_id}")


if __name__ == "__main__":
    home_controller = SmartHomeHub()

    # Initialize all the devices 
    light = Lightbulb("Living Room Light")
    thermostat = Thermostat("Nest Thermostat")
    camera = SecurityCamera("Driveway Camera")
    entertainment_system = Television("Samsung TV")
    refrigerator = Refrigerator("LG Refrigerator")
    lock = Lock("Masterlock")
    air_purifier = AirPurifier("Dyson Air Purifier")
    garage_door = GarageDoor("Garage Door")

    # Add devices to the main control unit
    home_controller.add_device(light)
    home_controller.add_device(thermostat)
    home_controller.add_device(camera)
    home_controller.add_device(entertainment_system)
    home_controller.add_device(refrigerator)
    home_controller.add_device(lock)
    home_controller.add_device(air_purifier)
    home_controller.add_device(garage_door)

    # SmartLight Class methods example
    home_controller.send_command("Living Room Light", "turn_on")
    home_controller.send_command("Living Room Light", "change_brightness", 75)
    home_controller.send_command("Living Room Light", "change_brightness", 40)
    home_controller.send_command("Living Room Light", "turn_off")
    home_controller.send_command("Living Room Light", "turn_off")

    # Thermostat Class methods example
    home_controller.send_command("Nest Thermostat", "turn_on")
    home_controller.send_command("Nest Thermostat", "set_temperature", 72.5)
    home_controller.send_command("Nest Thermostat", "set_temperature", 70.2)
    home_controller.send_command("Nest Thermostat", "turn_off")

    # SecurityCamera Class methods example
    home_controller.send_command("Driveway Camera", "turn_on")
    home_controller.send_command("Driveway Camera", "detect_motion")
    home_controller.send_command("Driveway Camera", "detect_motion")
    home_controller.send_command("Driveway Camera", "turn_off")

    # Television Class methods example
    home_controller.send_command("Samsung TV", "turn_on")
    home_controller.send_command("Samsung TV", "set_volume", 30)
    home_controller.send_command("Samsung TV", "change_source", "Youtube TV")
    home_controller.send_command("Samsung TV", "change_source", "Playstation 5")
    home_controller.send_command("Samsung TV", "set_volume", 45)
    home_controller.send_command("Samsung TV", "change_source", "Xbox Series X")
    home_controller.send_command("Samsung TV", "turn_off")

    # Refrigerator Class methods example
    home_controller.send_command("LG Refrigerator", "turn_on")
    home_controller.send_command("LG Refrigerator", "set_refrigerator_temp", 40)
    home_controller.send_command("LG Refrigerator", "set_freezer_temp", 30)
    home_controller.send_command("LG Refrigerator", "door_status", True)
    home_controller.send_command("LG Refrigerator", "set_refrigerator_temp", 38)
    home_controller.send_command("LG Refrigerator", "set_freezer_temp", 26)
    home_controller.send_command("LG Refrigerator", "door_status", False)
    home_controller.send_command("LG Refrigerator", "turn_off")

    # Lock Class methods example
    home_controller.send_command("Masterlock", "lock")
    home_controller.send_command("Masterlock", "get_lock_status")
    home_controller.send_command("Masterlock", "unlock")
    home_controller.send_command("Masterlock", "get_lock_status")
    home_controller.send_command("Masterlock", "lock")

    # AirPurifier Class methods example
    home_controller.send_command("Dyson Air Purifier", "turn_on")
    home_controller.send_command("Dyson Air Purifier", "set_purification_level", 2)
    home_controller.send_command("Dyson Air Purifier", "get_purification_status")
    home_controller.send_command("Dyson Air Purifier", "set_fan_speed", 3)
    home_controller.send_command("Dyson Air Purifier", "get_fan_speed")
    home_controller.send_command("Dyson Air Purifier", "set_purification_level", 3)
    home_controller.send_command("Dyson Air Purifier", "get_purification_status")
    home_controller.send_command("Dyson Air Purifier", "set_fan_speed", 1)
    home_controller.send_command("Dyson Air Purifier", "turn_off")

    # GarageDoor Class methods example
    home_controller.send_command("Garage Door", "open_door")
    home_controller.send_command("Garage Door", "close_door")
    home_controller.send_command("Garage Door", "open_door")
    home_controller.send_command("Garage Door", "close_door")

    # Example of command not found
    home_controller.send_command("Garage Door", "open_garage")
