from tkinter import *   ## notice capitalized T in Tkinter 


import socket #Importamos la librería socket para poder comunicarnos con nuestro ESP8266



#Variables para el padding(Espaciado entre objetos) en X e Y
padX=10  
padY=20

ESP_IP = '192.168.0.21'  #IP de nuestro modulo
ESP_PORT = 8266 #Puerto que hemos configurado para que abra el ESP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos el objeto socket para conectarnos.

root = Tk() #Creamos la ventana principal de nuestra aplicación
root.title("Controlador ESP8266") #Cambiamos el título a nuestra ventana

frame = Frame (root)  #Creamos el contenedor denuestros objetos

lbl_titulo = Label(frame, text="Controlador ESP8266")  #Creamos texto para el título
imagenESP = PhotoImage(file="esp8266.png") #Cargamos imágen del ESP8266
lbl_imagen = Label(frame, image=imagenESP) #Creamos etiqueta para poner la foto del ESP8266

lbl_titulo.grid(row=0, column=0, pady=padY,padx=padX)  #Añadimos el título a nuestro contenedor
lbl_imagen.grid (row=0, column=1,columnspan=2,pady=padY,padx=padX) #Añadimos nuestra imágen al contenedor




lbl_LEDControl = Label (frame, text="Control LED") #Texto "Control LED"
lbl_LEDControl.grid (row=1, column=0) # Añadimos el texto "Control LED" al contenedor

def enciendeLED():              #Función para encender el LED
    print("Encendiendo LED")
    dato = '1'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 1 al modulo ESP

def apagaLED():                #Función para apagar el LED
    print("Apagando LED")
    dato = '0'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 0 al modulo ESP
    
btn_LEDOn = Button(frame, text="On", fg="green", command=enciendeLED)  #Creamos botón de encendido del LED
btn_LEDOff = Button(frame, text="Off", fg="red",command=apagaLED)      #Creamos botón de apagado del LED  
btn_LEDOn.grid (row=1, column=1,pady=padY)      #Añadimos el botónd "ON" a nuestro contenedor.                                                 
btn_LEDOff.grid (row=1, column=2,pady=padY)     #Añadimos el botónd "OFF" a nuestro contenedor. 
frame.pack()


s.connect((ESP_IP , ESP_PORT)) #Nos conectamos a la IP y el puerto que hemos declarado al inicio.


root.mainloop()


