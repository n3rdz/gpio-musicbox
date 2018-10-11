import pygame
from gpiozero import Button, LEDBoard
from signal import pause

pygame.init()

button_1 = Button(14)
button_2 = Button(18)
button_3 = Button(9)
button_4 = Button(10)

led = LEDBoard(11,22,27,17)


sound1 = pygame.mixer.Sound('samples/drum_tom_mid_hard.wav')
sound2 = pygame.mixer.Sound('samples/drum_splash_hard.wav')
sound3 = pygame.mixer.Sound('samples/drum_cowbell.wav')
sound4 = pygame.mixer.Sound('samples/drum_cymbal_closed.wav')


button_1.when_pressed = sound1.play
button_2.when_pressed = sound2.play
button_3.when_pressed = sound3.play
button_4.when_pressed = sound4.play

def button_1_on() :
    led.value = (1,0,0,0)
     
def button_2_on() :
     led.value = (0,1,0,0)
     
def button_3_on() :
     led.value = (0,0,1,0)
     
def button_4_on() :
     led.value = (0,0,0,1)
     

while True:
    if button_1.is_pressed:
          button_1_on()
          
    if button_2.is_pressed:
      button_2_on() 
          
    if button_3.is_pressed:
      button_3_on()

    if button_4.is_pressed:
      button_4_on()
