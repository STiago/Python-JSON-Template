# Python-JSON-Template

﻿Write a python module that can receive a JSON string and if the action is “apply” it adds the contents of the “template” into a priority queue.
The module also processes the queue every second and saves the template to a file.

Example JSON string:

{“action”: “apply”, “when”: “2016-4-19 10:00:00”, “template”: …}


## Solution

Documentation [here](https://stiago.github.io/Python-JSON-Template/)

```
Module that can receive a JSON string and if the action is "apply" it adds the contents of the "template" field into a priority queue.

I also included an example program that describes how to use the module.

How to run the example program: ./example_program.py
How to run the tests: ./tests.py

Before running this program and its tests please execute the following commands: 
    - virtualenv env
    - env/bin/pip install -r requirements.txt

```
