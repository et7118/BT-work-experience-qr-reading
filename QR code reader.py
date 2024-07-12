from CHECKqrcodevalue import check_qr
from check_in_checker import check_check_in
from Leds import Flash, On, Off
import time
import serial
import sqlite3

# url = "https://httpbin.org/post" 


connection_obj = sqlite3.connect('Database1.db') 

Piserial = serial.Serial(      #connects us to serial port 
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
print("Connected to: " + Piserial.portstr) 

def check_if_a_dict(string): #checks if the value in the qr code can act as a dictionary
    try:
        x = eval(string)
        return True
    except Exception:
        return False

def success(name): 
    Flash('green',1)
    print(name)

def failure():
    print('incorrect qr code')
    Flash('red', 2.5)
    

On('blue') #turns on blue LED to show you can start scanning qr codes
try:
    while True:
            if Piserial.in_waiting > 0:
                line = Piserial.readline().decode('utf-8').rstrip() #reads qr code
                if check_if_a_dict(line):  
                    qrcodevalue = eval(line) #turns string into dict
                
                    
                    if qrcodevalue['uuid']: #if the dict has a field uuid
                            if check_qr(qrcodevalue)[0]:  #checks its in GUEST table
                                if check_check_in(qrcodevalue['uuid']): # registers it as checked in unless it has already done so
                                    success(check_qr(qrcodevalue)[1])    
                                else:
                                    failure()
                            else:
                                failure()
                     
                               
                    else:
                        failure()
                else: 
                    failure()
except KeyboardInterrupt:
    pass
finally:
    Off('blue')
    Piserial.close()


            #q = requests.post(url, json = qrcodevalue)
            #print(q.json())



