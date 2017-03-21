#!env/bin/python
from module import *
import time

print("Hello")

time.sleep(2)

print("2 seconds after")

init_sync()

add_template('{"action": "apply", "when": "2016-4-19 10:00:00", "template":"TEST TEMPLATE"}')
add_template('{"action": "apply", "when": "2016-4-19 10:00:01", "template":"TEST TEMPLATE 2"}')
time.sleep(5)

add_template('{"action": "apply", "when": "2016-4-19 10:00:02", "template":"TEST VICTORIA 1"}')
time.sleep(1)

add_template('{"action": "apply", "when": "2016-4-19 10:00:02", "template":"TEST VICTORIA 2"}')
time.sleep(2)

add_template('{"action": "apply", "when": "2016-4-19 11:00:00", "template":"LAST TEMPLATE"}')
time.sleep(1)

stop_sync()
