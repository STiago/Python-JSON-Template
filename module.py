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
