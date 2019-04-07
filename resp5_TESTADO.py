#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Desenvolver um circuito e programar para que ligue       # 
#  um LED quando escurecer.                                 #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
#Definindo a utilização da biblioteca GPIO
import RPi.GPIO as GPIO
#importação da biblioteca time para utilizar temporizadores
import time
#Aqui definimos que vamos usar o numero de ordem do pino, e
#   não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição 
#   "GPIO.BOARD (12)" para "GPIO.BCM (18)" 
#Definindo a pinagem real
GPIO.setmode(GPIO.BOARD)
#Definindo o pino a ser utilizado
pin_to_circuit = 7
GPIO.setup(12,GPIO.OUT)
def rc_time (pin_to_circuit):
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count
try:
    # Main loop
    while True:
        a=rc_time(pin_to_circuit)
        print a
        if a<100000:
            GPIO.output(12,0)
            #time.sleep(0.1)
        if a>100000:
            GPIO.output(12,1)
            #time.sleep(0.1)
except KeyboardInterrupt:
    print("Fim de programa. \n")
    GPIO.cleanup()
    pass
finally:
    GPIO.cleanup()
