import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)

ena=board.get_pin('d:2:o')
enb=board.get_pin('d:7:o')
motor1=board.get_pin('d:3:o')
led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')

def led(total):
    if total == 0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif total== 1:
        ena.write(0)
        enb.write(0)
        motor1.write(0)
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total== 2:
        ena.write(1)
        enb.write(1)
        motor1.write(1)
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)    
    elif total== 3:
        ena.write(0)
        enb.write(0)
        motor1.write(0)
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif total== 4:
        ena.write(1)
        enb.write(1)
        motor1.write(1)
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif total== 5:
        ena.write(0)
        enb.write(0)
        motor1.write(0)
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)