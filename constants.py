WAKE_UP_PIN = 'P4'
DOOR_PIN_1 = 'P9'
DOOR_PIN_2 = 'P10'
TEMP_DATA_PIN = 'P16'
MOTOR_PIN_LIST = ['P19', 'P20', 'P21', 'P22']

DOOR_NUMBER_OF_CHECKS = 50 # doorCheckTime = this.number * 0.1

MIN_INT = -9999
MAX_INT = 9999

TEMP_DIFF = 1.5 # Maximum acceptable discrepancy

ITERATOR_NUM = 100
TEMP_DATA_GATHERING_DELAY = 0.2
# TEMP_DATA_GATHERING_DELAY * ITERATOR_NUM = total time gathering data

# Temperature boundaries
UPPER_TEMP = 30
LOWER_TEMP = 28
# Time boundaries
EARLY_HOUR = 10
LATE_HOUR = 21

# Speed ​​(ms) The larger the value, the slower the speed, the minimum value is 1800us
MOTOR_SPEED = 1800
REQ_DEGREE_TO_OPEN = 1900

DEEP_SLEEP_TIME = 1000*60*20 # 20 min (Format = Millisec)
