import socket
import webiopi
import sys, codecs
import re

GPIO = webiopi.GPIO

def MotorDrive( iIn1Pin, iIn2Pin, motor ):
    if 5 > motor and -5 < motor:
        GPIO.pwmWrite( iIn1Pin, 0.0 )
        GPIO.pwmWrite( iIn2Pin, 0.0 )
    elif 0 < motor:
        GPIO.pwmWrite( iIn1Pin, motor * 0.01 )
        GPIO.pwmWrite( iIn2Pin, 0.0 )
    else:
        GPIO.pwmWrite( iIn1Pin, 0.0 )
        GPIO.pwmWrite( iIn2Pin, -motor * 0.01 )

IN1PIN = 23
IN2PIN = 24
GPIO.setFunction( IN1PIN, GPIO.PWM )
GPIO.setFunction( IN2PIN, GPIO.PWM )
motor = 0
count_w = 0

pat = re.compile("(((left)|(right))\\s*,\\s*(\\d+))")
patw = re.compile("((w)|(W))")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('PCのIP', 8092))
while 1:
    data = client_socket.recv(512)
    if data:
        for m in pat.findall(data.decode("shift-jis")):
            print m[1] + " | " + m[4]
            if int(m[4]) < 0:
                motor = 0
            elif int(m[4]) > 100:
                motor = 100
            else:
                motor = int(m[4]) 
            if m[1]=="left":
                pass
            if m[1]=="right":
                motor = -1*motor

            MotorDrive( IN1PIN, IN2PIN, motor )

        r = re.compile(r">(.+?)<\/chat")
        returnlist = r.findall(data.decode("shift-jis"))

        if returnlist:
            print returnlist[0].encode('utf-8')
            for m in patw.findall(returnlist[0]):
                count_w+= 1
        if count_w > 100:
            count_w=100
        MotorDrive( IN1PIN, IN2PIN, count_w )
        webiopi.sleep( 1.0 )
        if count_w == 100:
            count_w=0
        print "w_count:", count_w
        MotorDrive( IN1PIN, IN2PIN, 0 )
    client_socket.send(data)
    data = ""