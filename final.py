from umqtt import MQTTClient
from machine import Pin, Timer, ENC, PWM
from board import A21, A7 #for buttons
from board import A6, A9, A18, A17 #for motor
#from board import A5, A20 #to test - for hcsr04 sensor, optional
import time
from micropython import schedule
from machine import Pin, Timer

##################MQTT######################
myMqttClient = "<add here>"
adafruitIoUrl = "io.adafruit.com"
adafruitUsername = "<add here>"
adafruitAioKey = "<add here>"
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)

c.connect()

#############for blue button ################
last_time_b = time.ticks_ms()
count_b = 0
def report_b(pin):
	global count_b
	c.publish("<add your IFTTT feed here>", str(count_b))
 	print("Published {} to Button 1.".format(str(count_b)))

#handler for blue button
def button_blue(button_b):
 	global count_b, last_time_b
 	state_b = button_b()
 	t = time.ticks_ms()
 	delta_t_b = t - last_time_b
 	if delta_t_b > 20 and state_b == 0: 
 		count_b += 1
 		last_time_b = t
 		schedule(report_b, button_b)

#############for red button ################
count_r = 0
last_time_r = time.ticks_ms()
def report_r(pin):
	global count_r
	c.publish("<add your IFTTT feed here>", str(count_r))
 	print("Published {} to Button 2.".format(str(count_r)))

#handler for red button
def button_red(button_r):
 	global count_r, last_time_r 
 	state_r = button_r()
 	t = time.ticks_ms()
 	delta_t_r = t - last_time_r
 	if delta_t_r > 20 and state_r == 0:
 		count_r += 1
 		last_time_r = t
 		schedule(report_r, button_r)

###############for buttons###############
button_b = Pin(A21, mode = Pin.IN, pull = Pin.PULL_UP)
button_b.irq(button_blue, trigger = Pin.IRQ_FALLING)

button_r = Pin(A7, mode = Pin.IN, pull = Pin.PULL_UP)
button_r.irq(button_red, trigger = Pin.IRQ_FALLING)
#Note: You can change your trigger to Pin.IRQ_RISING, or Pin.IRQ_FALLING | Pin.IRQ_RISING. Check what works best for your buttons
print("blue :", button_b())
print("red :", button_r())


##############for motor###################
encL = ENC(0, Pin(A6), Pin(A9))
encL.filter(1023)
count_motor = 0
pwmL1 = PWM(A18, freq = 100000, duty=0, timer= 1)
pwmL2 = PWM(A17, freq=100000, duty=0, timer= 1)

def moveLeft(velocity):
	if velocity > 0:
		pwmL1.duty(100)
		pwmL2.duty(100-velocity)
	else:
		pwmL1.duty(100)
		pwmL2.duty(100+velocity)

############ for mQTT and motor############

def sub_cb(topic, msg):
    print(topic, msg)
    if msg == b'1':
    	moveLeft(20)
    	time.sleep(0.34)
    	moveLeft(0)       

c.set_callback(sub_cb)
c.subscribe("<add your IFTTT feed here>")    

c.disconnect()