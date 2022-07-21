#.......................... Standard imports ..........................
#.....................................................................
#.....................................................................
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import sys

#.......................... Outside imports  .........................
sys.path.append('D:\Python\Monitoring Scripts\SilentPython 2\scripts')  
from lib.core import parent
#.....................................................................
#.....................................................................
#.....................................................................

class client(parent):
    def __init__(self):
        #-------inherit the methods and properties from its parent.
        super().__init__("These are the real details")
        #-------Set child properties
        self.items = {'bucket': "", 'org': "", 'token': "", 'url': ""}
        self.connection = influxdb_client.InfluxDBClient.write_api

    #=================================================================[Set database config]
    def set_config(self, bucket, org, token, url):
        self.items['bucket'] = bucket
        self.items['org'] = org
        self.items['token'] = token
        self.items['url'] = url

    #=================================================================[Connect to the database]
    def connect(self):
        try:  
            #...................................................
            #...................................................
            #...................................................              
            bucket = self.items['bucket'] #"Scripts"
            org = self.items['org']       #"my-org"
            token = self.items['token']   #"nkqiIuAGrBDAACmyx82kD0q4YXhv_MJN-gXKF9PNN-nGimwnlOpT6Zmv4x805XIyFDNUOuzhvNRcoR32jWbTsg=="
            url = self.items['url']       #"http://localhost:8086"
            client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)

            self.connection = client.write_api(write_options=SYNCHRONOUS)
            self.connection.flush()
            print(f"Influx client connected: {bucket}")
            #...................................................
            #...................................................
            #...................................................

        except Exception as e: 
            self.error.set(True, "influx_connect: " + str(e), 0)

        #=================================================================[Write to the database]
    def write(self,groupname='',valuename='',value=0.000, count=0):
        try:
            #...................................................
            #...................................................
            #...................................................

            bucket = self.items['bucket'] #"Scripts"
            org1 = self.items['org']       #"my-org"

            point = influxdb_client.Point(groupname).field(valuename, value)
            self.connection.write(bucket=bucket, org=org1,  record=point)
            print(f"Influx value writen: {groupname}, {valuename}, {value}, {count}")
            #...................................................
            #...................................................
            #...................................................
        except Exception as e: 
            self.error.set(True, "influx_write: " + str(e), 0)

                #=================================================================[Write to the database multi]
    def write_multi(self,groupname='',valuename='',value=0.000, count=0):
        try:
            #...................................................
            #...................................................
            #...................................................

            bucket = self.items['bucket'] #"Scripts"
            org1 = self.items['org']       #"my-org"

            point = influxdb_client.Point(groupname).field(valuename, value)
            point2 = influxdb_client.Point(groupname).field('testx', 10)
            points = [point, point2]            
            self.connection.write(bucket=bucket, org=org1,  record=points)
            #...................................................
            #...................................................
            #...................................................
        except Exception as e: 
            self.error.set(True, "influx_write: " + str(e), 0)

        #=================================================================[Write to the database]
    def reset(self):
        try:
            #...................................................
            #...................................................
            #...................................................
            self.connection.close()
            self.error.clear()
            #...................................................
            #...................................................
            #................................................... 
        except Exception as e: 
            next

