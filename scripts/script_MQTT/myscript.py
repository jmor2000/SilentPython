#.......................... Standard imports ..........................
#.....................................................................
#.....................................................................
import time
import sys
from datetime import datetime
#.......................... Outside imports  .........................
sys.path.append('D:\Python\Monitoring Scripts\SilentPython 2\scripts')  
import lib.mqtt as mqtt_f
import lib.influxDB as influx_f
import lib.core as core
#.....................................................................
#.....................................................................
#.....................................................................



#============================================================Setup
import threading, queue
G_time_sleep = 1
G_time_wait = 1
G_q_msg_P = queue.Queue(100)
G_q_influx_P = queue.Queue(100)
G_mqttClient = mqtt_f.client
G_influxClient = influx_f.client
G_appname = ""
G_count_cycle = 1

#==========================================================================================================Main
#==========================================================================================================Main
#==========================================================================================================Main
def main(sqlclient, appname="", property={}):
    print('Python Code==========================================')

    #___MQTT Client msg Q setup
    global G_q_msg_P, G_mqttClient, G_influxClient
    global G_appname

    G_appname = appname

    #set globals
    mqtt_f.G_q_msg = G_q_msg_P
    mqtt_f.G_sub_items = ['iot2040/tempA0', 'iot2040/tempA2']
    
    #___MQTT Client
    G_mqttClient = mqtt_f.client()
    G_mqttClient.connect("192.168.0.227",11883)
    G_mqttClient.start(True)
    error_latch = True

    #___INFLUX
    G_influxClient = influx_f.client()
    G_influxClient.set_config("Scripts","my-org","nkqiIuAGrBDAACmyx82kD0q4YXhv_MJN-gXKF9PNN-nGimwnlOpT6Zmv4x805XIyFDNUOuzhvNRcoR32jWbTsg==","http://192.168.0.227:8086")
    G_influxClient.connect()

    #__System Checks
    error_influx = G_influxClient.error.get()
    error_mqtt = G_mqttClient.error.get()

    #__Launch Threads
    if error_influx['state'] == False and error_mqtt['state'] == False:
        #__Threading --- loops
        threading.Thread(target=loop_processdata, daemon=True).start()
        threading.Thread(target=loop_influx, daemon=True).start()
        print("loops started")
    else:
        print(f'Influx: {error_influx}, MQTT: {error_mqtt}')
        print("main loop exit")
        exit()

    #==========================================================================================================Loop Main
    #==========================================================================================================Loop Main
    #==========================================================================================================Loop Main
    global G_time_sleep, G_count_cycle
    display_counter = 0
    display_flag = True
    error_influx = False
    error_mqtt = False
    
    while True:                 

        time.sleep(G_time_sleep)       

        #--------------------------------------------Erro Check
        #Check1
        mymqttclientisconnected = G_mqttClient.is_connected()
        if mymqttclientisconnected != error_latch:
            error_latch = mymqttclientisconnected
            print(f'MQTT Connection: {mymqttclientisconnected}')
        temp_error = G_mqttClient.error.get()
        if mymqttclientisconnected == False:
             error_mqtt = True
        else:
             error_mqtt = False

        #Check2
        myinflux_error = G_influxClient.error.signal()
        if myinflux_error == True:
            print(f'Influx Connection: Error')
        temp_error = G_influxClient.error.get()
        if temp_error['state'] == True:
             error_influx = True
        else:
             error_influx = False

        #Update display
        #--------------------------------------------Script Display
        if display_counter == 5:
            display_flag = True
            display_counter = 0
        else:
            display_counter += 1

        if display_flag == True:
            if error_mqtt == True or error_influx == True:
                dstate = "error"
            else:
                dstate = "ok"

            #ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            dtime = datetime.timestamp(datetime.now()) #...........State output
            items = {'state' : dstate, 'ts_updated' : dtime, 'count_cycle' : G_count_cycle}
            sqlclient.sql_update(items)
            #ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

            display_flag = False # reset
            sys.stdout.flush() #outputs the termanl to the logs

        #...........................Send stats
        if error_influx == False:
            stats_queSIZE = G_q_msg_P.qsize()
            stats_avgSPEED = 99
            #G_influxClient.write_multi(G_appname, "Metric_Q", stats_queSIZE, 1)
            #G_influxClient.write(G_appname, "Metric_Speed", stats_avgSPEED, 1)


        #print('........................................................loop 0')
    G_mqttClient.start(False)

#==========================================================================================================Loop MQTT
#==========================================================================================================Loop MQTT
#==========================================================================================================Loop MQTT
def loop_processdata():
        global G_q_msg_P, G_q_influx_P
        global G_time_wait
        global G_mqttClient
        global G_count_cycle

        countme = 0
        while True:
            try:
                item = G_q_msg_P.get(True, G_time_wait)
                payloadconvert = float(item.payload.decode("utf-8"))

                if item.topic == mqtt_f.G_sub_items[0]:
                    #payloadconvert += 10
                    print(f'MSG Payload={payloadconvert}')
                    print(f'MSG Topicx={item.topic}')

                elif item.topic == mqtt_f.G_sub_items[1]:
                    #payloadconvert += 20
                    print(f'MSG Payload={payloadconvert}')
                    print(f'MSG Topic={item.topic}')

                else:
                    print(f'unknown MSG Payload={item.payload}')     

                #---------------------------------Write back the MQTT Broker--------
                #newtopic = str(item.topic + "_New")
                #newtopic = item.topic
                #G_mqttClient.write(newtopic,payloadconvert)
                #-------------------------------------------------------------------

                G_q_msg_P.task_done()
                ok = True
                
            except Exception as e:
                ok = False
                #print('Fail:' + str(e))

            if ok == True:
                G_q_influx_P.put([str(item.topic), payloadconvert, G_count_cycle],1)
                #ccccccccccccccccccccccccccccccccccc
                G_count_cycle += 1 # Count the Cycle
                #ccccccccccccccccccccccccccccccccccc
            
            #print('........................................................loop 1')



#==========================================================================================================Loop INFLUX
#==========================================================================================================Loop INFLUX
#==========================================================================================================Loop INFLUX
def loop_influx():
        global G_q_influx_P, G_influxClient
        global G_time_wait, G_appname

        influx_dataQ = core.dataQ(list)
        influx_dataQ.setQ(G_q_influx_P)

        error_influx = G_influxClient.error.get()

        while True:
                #QQQQQQQQQ
                data_flag, data_point= influx_dataQ.get_data(True)
                        
                #---------Do Task
                if data_flag == True:
                    G_influxClient.write(G_appname, data_point[0], data_point[1], data_point[2])
                    error_influx = G_influxClient.error.get()

                #---------Check For error
                if error_influx['state'] == True:
                    #QQQQQQQQQ
                    influx_dataQ.buffer_data(data_point)
                    print(f'ERROR: Influx Write:{data_point[2]} - Buffer {G_q_influx_P.qsize()} - e:{error_influx}')

                    #.....Timeout & Attempt a Reconnect
                    time.sleep(5)                  
                    G_influxClient.reset()
                    G_influxClient.connect()
            
            #print('........................................................loop 2')




#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
if __name__ == "__main__":
    main(object, appname="App999", property={})
