from gpiozero import LED  # Importa a classe 'LED' da biblioteca gpiozero
from time import sleep    # Importa a função 'sleep' da biblioteca padrão 'time'

led = LED(17) # Cria um objeto 'led' associado ao pino GPIO 17, configurando esse pino como SAÍDA (Output)

while True:       # Inicia um laço de repetição infinito
	led.on()      # Envia nível lógico alto para o pino 17, acendendo o LED
	sleep(1)      # Pausa por 1 segundo enquanto o estado do LED se mantém
	led.off()     # Envia nível lógico baixo para o pino 17, apagando o LED
	sleep(1)      # Pausa novamente por 1 segundo antes de voltar ao início do 'while'
