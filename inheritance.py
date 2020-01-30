from datetime import datetime
import os

os.path.join('/Users/amajcher/Desktop','links.txt')
class Astronomer():

    def __init__(self, task_id: str):
        self.task_id = task_id
        print("Astronomer created: %s" % (self.task_id))

    def astro_run(self):

        print("Astronomer run at: %s" % (datetime.now()))

#FirstInstance = Astronomer('DEv123')
#Second = FirstInstance.Astro_run()
class Splunk():
    def __init__(self,session: str):
        self.session = session

    def return_input(self):
        return self.session + " splunk"

class Mode():
    def __init__(self, session: str):
        self.session = session

    def return_input(self):
        return self.session + " Mode"

devConnectionSPL = Splunk('FirstSession')
devConnectionMD = Mode('FirstSession')
print(devConnectionSPL.return_input())
print(devConnectionMD.return_input())

for item in [devConnectionSPL, devConnectionMD]:
    print(type(item))
    print(item.return_input())

