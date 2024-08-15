from SmartHomeHub import *
from Devices import *

# All Device Initializations for the tests 
light = Lightbulb("Kitchen Light")
thermostat = Thermostat("Honeywell Thermostat")
camera = SecurityCamera("Geeni Camera")
system = Television("Samsung TV")
fridge = Refrigerator("LG Fridge")
lock = Lock("Shed Lock")
purifier = AirPurifier("Dyson Air Purifier")
door = GarageDoor("Garage Door ")


# Test device initialization
def test_device_init():
    device = SmartDevice("123456", "Test_Device")
    assert device.device_id == "123456"
    assert device.device_type == "Test_Device"
    assert device.status == "off"


# Test device turn_on
def test_turn_on():
    device = SmartDevice("123456", "Test_Device")
    device.turn_on()
    assert device.status == "on"


# Test device turn_off
def test_turn_off():
    device = SmartDevice("123456", "Test_Device")
    device.turn_on()

    assert device.status == "on"
    device.turn_off()

    assert device.status == "off"


# Test device get_status
def test_get_status():
    device = SmartDevice("123456", "Test_Device")
    # Test status when off
    assert device.get_status() == "off"
    # Test status when on
    device.turn_on()
    assert device.get_status() == "on"


'''Tests for Lightbulb Device Class'''


# Test lightbulb initialization
def test_lightbulb_init():
    assert light.device_id == "Kitchen Light"
    assert light.device_type == "Smart Lightbulb"
    assert light.status == "off"
    assert light.brightness == 0


# Test turn_on method
def test_lightbulb_turn_on():
    light.turn_on()
    assert light.status == "on"
    assert light.brightness == 100


# Test turn_off method
def test_lightbulb_turn_off():
    light.turn_on()
    light.turn_off()
    assert light.status == "off"
    assert light.brightness == 0


# Test adjust_brightness method 1
def test_adjust_brightness1():
    light.turn_on()
    light.change_brightness(50)
    assert light.brightness == 50


# Test adjust_brightness method 2
def test_adjust_brightness2():
    light.change_brightness(-50)
    assert light.brightness == 0


'''Tests for Thermostat Device Class'''


# Test thermostat initialization
def test_thermostat_init():
    assert thermostat.device_id == "Honeywell Thermostat"
    assert thermostat.device_type == "Thermostat"
    assert thermostat.status == "off"
    assert thermostat.temperature == 65.0


# Test turn_on method
def test_thermostat_turn_on():
    thermostat.turn_on()
    assert thermostat.status == "on"
    assert thermostat.temperature == 65.0


# Test turn_off method
def test_thermostat_turn_off():
    thermostat.turn_off()
    assert thermostat.status == "off"
    assert thermostat.temperature == 65


# Test set_temperature method
def test_set_temperature():
    thermostat.set_temperature(72.0)
    assert thermostat.temperature == 72.0


'''Tests for SecurityCamera Device Class '''


# Test security camera initialization
def test_camera_init():
    assert camera.device_id == "Geeni Camera"
    assert camera.device_type == "Security Camera"
    assert camera.status == "off"
    assert camera.motion_detected is False


# Test turn_on method
def test_camera_turn_on():
    camera.turn_on()
    assert camera.status == "active"


# Test turn_off method
def test_camera_turn_off():
    camera.turn_on()
    assert camera.status == "active"
    camera.turn_off()
    assert camera.status == "off"


# Test detect_motion method
def test_detect_motion():
    camera = SecurityCamera("Geeni Camera")
    detected = camera.detect_motion()
    assert isinstance(detected, bool)
    assert camera.motion_detected == detected


'''Tests for Television Device Class'''


# Test television initialization
def test_entertainment_system_init():
    assert system.device_id == "Samsung TV"
    assert system.device_type == "Television"
    assert system.status == "off"
    assert system.volume == 30
    assert system.input_source == "Cable"


# Test turn_on method
def test_entertainment_system_turn_on():
    system.turn_on()
    assert system.status == "on"


# Test turn_off method
def test_entertainment_system_turn_off():
    system.turn_off()
    assert system.status == "off"


# Test set_volume method
def test_set_volume():
    system.set_volume(15)
    assert system.volume == 15

    system.set_volume(20)
    assert system.volume == 20


# Test change_source method
def test_change_source():
    system.change_source("Playstation 5")
    assert system.input_source == "Playstation 5"
    system.change_source("Xbox Series X")
    assert system.input_source == "Xbox Series X"


'''Tests for Refrigerator Device Class'''


# Test refrigerator initialization
def test_refrigerator_init():
    assert fridge.device_id == "LG Fridge"
    assert fridge.device_type == "Refrigerator"
    assert fridge.status == "off"
    assert fridge.refrigerator_temp == 38
    assert fridge.freezer_temp == 26
    assert fridge.door_open is False


# Test turn_on method
def test_refrigerator_turn_on():
    fridge.turn_on()
    assert fridge.status == "on"


# Test turn_off method
def test_refrigerator_turn_off():
    fridge.turn_off()
    assert fridge.status == "off"


# Test set_refrigerator_temp method
def test_set_refrigerator_temp():
    fridge.set_refrigerator_temp(42)
    assert fridge.refrigerator_temp == 42


# Test set_freezer_temp method
def test_set_freezer_temp():
    fridge.set_freezer_temp(30)
    assert fridge.freezer_temp == 30


# Test door_status method
def test_door_status():
    fridge.door_status(True)
    assert fridge.door_open == True
    fridge.door_status(False)
    assert fridge.door_open == False


'''Tests for Lock Device Class'''


# Test lock initialization
def test_lock_init():
    assert lock.device_id == "Shed Lock"
    assert lock.device_type == "Lock"
    assert lock.status == "off"
    assert lock.is_locked is True


# Test for locked method
def test_locked():
    lock.unlocked()
    assert lock.is_locked is False
    lock.locked()
    assert lock.is_locked is True


# Test for unlocked method
def test_unlocked():
    lock.unlocked()
    assert lock.is_locked is False


# Test for get_lock_status method
def test_get_lock_status():
    lock.locked()
    assert lock.get_lock_status() == "locked"
    lock.unlocked()
    assert lock.get_lock_status() == "unlocked"


'''Tests for Air Purifier Device Class'''


# Test air_purifier initialization
def test_air_purifier_init():
    assert purifier.device_id == "Dyson Air Purifier"
    assert purifier.device_type == "Air Purifier"
    assert purifier.status == "off"
    assert purifier.purification_level == 0
    assert purifier.fan_speed == 0


# Test turn_on method
def test_turn_on():
    purifier.turn_on()
    assert purifier.status == "on"
    assert purifier.purification_level == 1
    assert purifier.fan_speed == 1


# Test turn_off method
def test_turn_off():
    purifier.turn_off()
    assert purifier.status == "off"
    assert purifier.purification_level == 0
    assert purifier.fan_speed == 0


# Test set_fan_speed method
def test_set_fan_speed():
    purifier.set_fan_speed(2)
    assert purifier.fan_speed == 2
    purifier.set_fan_speed(3)
    assert purifier.fan_speed == 3


# Test set_purification_level method 
def test_set_purification_level():
    purifier.set_purification_level(2)
    assert purifier.purification_level == 2
    purifier.set_purification_level(3)
    assert purifier.purification_level == 3


# Test get_purification_status method
def test_get_purification_status():
    purifier.set_purification_level(2)
    assert purifier.get_purification_status() == 2


# Test get_fan_speed method
def test_get_fan_speed():
    purifier.set_fan_speed(2)
    assert purifier.get_fan_speed() == 2


'''Tests for Garage Door Device Class '''


# Test garage_door initialization
def test_garage_door_init():
    assert door.device_id == "Garage Door "
    assert door.device_type == "Garage Door"
    assert door.status == "off"
    assert door.is_open is False


# Test open_door method
def test_open_door():
    door.open_door()
    assert door.is_open is True
    assert door.status == "open"


# Test close_door method
def test_close_door():
    door.close_door()
    assert door.is_open is False
    assert door.status == "closed"


'''Tests for SmartHomeHub Class'''


# Class defines a device to be used to test SmartHomeHub methods
class TestDevice:
    # Initialization of device
    def __init__(self, device_id, status="off"):
        self.device_id = device_id
        self.status = status

    # Returns the current status of the device
    def get_status(self):
        return self.status

    # Method to turn on the device
    def turn_on(self):
        self.status = "on"

    # Method to turn off the device
    def turn_off(self):
        self.status = "off"


control_unit = SmartHomeHub()


# Test add_device function
def test_add_device():
    control_unit = SmartHomeHub()
    device = TestDevice("test_device")
    control_unit.add_device(device)
    assert "test_device" in control_unit.devices
    assert control_unit.devices["test_device"] == device


# Test remove_device function
def test_remove_device():
    device = TestDevice("test_device")
    control_unit.add_device(device)
    control_unit.remove_device("test_device")
    assert "test_device" not in control_unit.devices


# Test get_device_status 1
def test_get_device_status():
    device = TestDevice("test_device")
    control_unit.add_device(device)
    status = control_unit.get_device_status("test_device")
    assert status == "off"


# Test get_device_status 2
def test_get_device_status_device():
    status = control_unit.get_device_status("Device Doesn't Exist")
    assert status is None
