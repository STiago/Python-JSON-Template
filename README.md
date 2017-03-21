# Python - JSON - Template

## Task

﻿Write a python module that can receive a JSON string and if the action is “apply” it adds the contents of the “template” into a priority queue.
The module also processes the queue every second and saves the template to a file.

Example JSON string:

{“action”: “apply”, “when”: “2016-4-19 10:00:00”, “template”: …}


## Solution


Module that can receive a JSON string and if the action is "apply" it adds the contents of the "template" field into a priority queue.

I also included an example program that describes how to use the module.

How to run the example program: ./example_program.py
How to run the tests: ./tests.py

Before running this program and its tests please execute the following commands: 
    - virtualenv env
    - env/bin/pip install -r requirements.txt

#### Requirements

```
pyhamcrest
```

#### Module.py

```
#!env/bin/python
import json
import Queue
from threading import Timer,Thread,Event

queue = Queue.Queue()

def add_template(data = ""):
    try:
        data_as_dict = json.loads(data)
        if data_as_dict.has_key('action') and data_as_dict['action']=='apply':
            if data_as_dict.has_key('template'):
                template = data_as_dict['template']
                template_as_string = str(template)
                queue.put(template_as_string)
            else:
                print "There is no template"
        else:
            print 'Action is different than "apply"'
    except ValueError:
        print "Cannot process the data, it seems to be in a wrong json format"

# Taken from http://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
class perpetualTimer():
   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def write_templates_to_file():

    try:
        f = open('file.txt', 'a')
        while not queue.empty():
            f.write(queue.get())
            f.write('\n')
        f.close()
    except IOError:
        print("Cannot open file.txt")

periodic_task = perpetualTimer(1,write_templates_to_file)

"""Schedules a periodic task that writes the values stored in the queue
every second"""
def init_sync():
    periodic_task.start()

"""Cancels the periodic that is writing to a file every second"""
def stop_sync():
periodic_task.cancel()

```

#### Example_program.py

```
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
```

#### Test.py

```
#!env/bin/python
from hamcrest import *
import unittest
from module import *

# One unit test per function, several cases per unit test
class AddTemplateTest(unittest.TestCase):

    def setUp(self):
        queue = Queue.Queue()

    def tearDown(self):
        queue = None

    def testEmptyJsonDoesNotModifyTheQueue(self):
        add_template('')
        assert_that(queue.empty(), is_(True))

    def testMissingActionInJsonDoesNotModifyTheQueue(self):
        add_template('{"when": "2016-4-19 10:00:00"}')
        assert_that(queue.empty(), is_(True))

    def testActionDifferentThanApplyDoesNotModifyTheQueue(self):
        add_template('{"action": "1", "age": "black", "template": 2}')
        assert_that(queue.empty(), is_(True))

    def testMissingTemplateInJsonDoesNotModifyTheQueue(self):
        add_template('{"action": "apply", "when": "2016-4-19 10:00:00"}')
        assert_that(queue.empty(), is_(True))

    def testValidJsonAddsTemplateToTheQueue(self):
        add_template('{"action": "apply", "when": "2016-4-19 10:00:00", "template":"TEST TEMPLATE"}')
        assert_that(queue.empty(), is_(False))
        assert_that(queue.get(), equal_to("TEST TEMPLATE"))

if __name__ == '__main__':
unittest.main()
```
 
![Image](src)


_Code_ licensed by **GNU GENERAL PUBLIC LICENSE Version 3**.

_Text_ licensed by **Creative Commons Attribution-ShareAlike 4.0 International**.

<p align="center">
<a href="http://www.gnu.org/licenses/gpl-3.0.html">
<img alt="GPL-3.0" src="https://dl.dropboxusercontent.com/s/t0ylvis7f1stcu7/GPL-3.0.png">
</a>
<a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">
<img alt="CC-BY-SA-4.0" src="https://dl.dropboxusercontent.com/s/sb421l5usayaigo/CC-BY-SA-4.0.png">
</a>
</p>

