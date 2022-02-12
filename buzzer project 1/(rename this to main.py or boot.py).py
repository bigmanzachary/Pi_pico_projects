import machine; from time import sleep

"""

Hello Github!

check the files for an image of what your board should
look like.

Thank you for downloading this!

"""

lower_freq_button = machine.Pin(0,machine.Pin.IN,
                                machine.Pin.PULL_DOWN)

higher_freq_button = machine.Pin(1,machine.Pin.IN,
                                machine.Pin.PULL_DOWN)

LED = machine.Pin(25,machine.Pin.OUT)

#PWM Output:
buzzer = machine.PWM(machine.Pin(2))
buzzer.duty_u16(2000) 
freq = 1000 

buzzer.freq(freq)
run = 1

LED.value(1)
sleep(1)
LED.value(0)
sleep(1)
    
while run == 1:
    
    
    def freq_down(pin):
        global freq
        if freq != 50:
            freq -= 50
        
            buzzer.freq(freq)
    
    def freq_up(pin):
        global freq
        global run
        
        freq += 50
        
        buzzer.freq(freq)
        if freq == 1300:
            run = 0

    lower_freq_button.irq(trigger = machine.Pin.IRQ_RISING,
                          handler = freq_down)
    higher_freq_button.irq(trigger = machine.Pin.IRQ_RISING,
                          handler = freq_up)

buzzer.duty_u16(0)