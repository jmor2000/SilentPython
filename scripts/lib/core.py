

#.... Main Class for modules
class parent:
    def __init__(self, details):
        self.details = details
        self.error = self.error()
    
    class error:
        def __init__(self):
            self.value = {'state' : False, 'value' : 0, 'msg' : ''}
            self.latch = False

        def set(self, state=False, msg='', value=0):
            latch_prev = self.value['state']

            if latch_prev == False and state == True:
                self.latch = True
            elif state == False:
                self.latch = False

            self.value['state'] = state
            self.value['value'] = value
            self.value['msg'] = msg

        def signal(self):
            returnvalue = self.latch
            self.latch = False
            return returnvalue

        def get(self):
            return self.value

        def clear(self):
            self.value = {'state' : False, 'value' : 0, 'msg' : ''}

#.... Data Q's with a buffer
import queue

class dataQ:
    def __init__(self, dataPoint):
        self.bufferFlag = False
        self.timewait = 1
        self.que = queue.Queue
        self.dataFlag = False
        self.dataPoint = dataPoint
        self.dataPointBUFF = dataPoint
        self.dataPointREF = dataPoint
        
    def setQ(self, que=queue.Queue):
        self.que = que

    def get_data(self, setbuffer=False):
        
        if setbuffer == True:
        #-------------------------------------------------------B-TRUE
            if self.bufferFlag == False:
                #-------------------Read from buffer
                try:
                    self.dataPoint =  self.que.get(True, self.timewait)
                    self.dataFlag = True

                except:
                    self.dataPoint = self.dataPointREF
                    self.dataFlag = False
            else:
                #------------------FIFO Buffer ()
                    self.dataPoint = self.dataPointBUFF
                    self.dataFlag = True
                    self.bufferFlag = False
        #-------------------------------------------------------B-FALSE
        else:
                self.bufferFlag == False
                try:
                    self.dataPoint =  self.que.get(True, self.timewait)
                    self.dataFlag = True

                except:
                    self.dataPoint = self.dataPointREF
                    self.dataFlag = False

        return self.dataFlag,  self.dataPoint


    def buffer_data(self, dataPoint):
        self.dataPointBUFF = dataPoint
        self.bufferFlag = True

    def get_que_size(self):
        return self.que.qsize

    def clear(self):
        try:
            with self.que.mutex:
                self.que.queue.clear()
            self.bufferFlag = False
            self.dataFlag = False
            self.dataPoint = self.dataPointREF
            self.dataPointBUFF = self.dataPointREF
        except:
            next

#.... Test
if __name__ == "__main__":
    print('Python Script==========================================')
    mycore = parent("Here they are")
    print(mycore.details)
    mycore.error.set(True,'error axsdf',1999)
    print(mycore.error.get())
    print(mycore.error.signal())
    print(mycore.error.signal())    