# Patient App Design
from streamsx.topology.topology import Topology
from streamsx.topology.context import *
import time
import json
def Observations():
	while True:
		jsonStr = '{"patientId":"patient-1","device":{"id":"VitalsGenerator","locationId”:"bed1"},"readingSource": {"id":123, "deviceId":"VitalsGenerator", "sourceType":"generated"},"reading": {"ts": 605, "uom":"bpm", "value":82.56785326532197,"readingType": {"code":"8867-4", "system":"streamsx.health/1.0"}}}'
		
		dictObj = json.loads(jsonStr)
		print(dictObj)
		time.sleep(1)
		yield dictObj
	
	
topo = Topology()
patientData = topo.source(Observations)
patientData.print()
submit()