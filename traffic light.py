from gpiozero import Button, TrafficLights, Buzzer  
from time import sleep  
  
buzzer = Buzzer(15)  
button = Button(21)  
lights = TrafficLights(25, 8, 7)  
  
while True:  
           button.wait_for_press() 
           buzzer.on() 
           lights.green.on()  
           sleep(2)
            
           button.wait_for_press() 
           buzzer.on() 
           lights.amber.on()  
           sleep(2)
           lights.off()
          
           button.wait_for_press() 
           buzzer.on() 
           lights.red.on()  
           sleep(2)  
          
           lights.off()
           buzzer.off() 
