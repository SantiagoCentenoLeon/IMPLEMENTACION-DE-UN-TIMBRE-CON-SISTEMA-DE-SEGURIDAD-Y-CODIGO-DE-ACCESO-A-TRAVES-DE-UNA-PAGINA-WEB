
while(1):
    import serial, time #importar librerias
    pic = serial.Serial("COM10", 9600) #creas el objeto pic, le asignas la comunicacion serial y el puerto COM correspondiente
    fotos = open('fotos.txt','w') #limpia y abre internamente el datos.txt
    time.sleep(1) #delay 1 segundo
    #variables
    a=0
    c=0 
    valor='0'
    numvalor=100
    foto='b'
    numfoto=0
    pic.flush() #limpia el serial antes de enviar algo
    foto=pic.readline() #lee lo que envia el pic , si el pic no envia nada lo espera has5ta que envie algo
    numfoto=long(float(foto)) #convierte a variable tipo long el char foto
    if(numfoto==9):
        pic.write(b'w') #enviamos el char w al pic
        fotos.write("1 \n") #se escribe 1 en fotos.txt ya que aun sigue abierto
        fotos.write("1 \n")
        fotos.close() #se guarda y cierra datos.txt
        c=1
    if(c==1):
        a=int(input("Ingrese aprobacion:")) # nos pide el entero 'a' por el input
        c-=1 #se varia el valor de c
        datos = open('datos.txt','w') #limpiamos ya brimos nuevamente datos.txt
        print("Se permitio el acceso al codigo")
    if(a==1):
        pic.write(b'p')#enviamos el char b al pic que hace posible colocar el codigo en el lcd
        valor = pic.readline() #recibimos el codigo de acceso,esperando que el usuario ingrese su codigo y ponga enter 
        print("El codigo ingresado fue: "+valor)
        datos.write((time.strftime("%Y-%m-%d %H:%M:%S \t")))#se ingresa la fecha y hora cuando se envia el dato
        datos.write("Codigo Ingresado :\t")
        datos.write(valor)
        a-=1#se varia a
        numvalor=long(float(valor))#se convierte a long la cadena valor
        
    if(numvalor==123456 and a==0):
        pic.write(b'y')
        print("yes")
        
    if(numvalor!=123456 and a==0):
        pic.write(b'n')
        print("no")
    pic.close() 
    datos.close()
    fotos = open('fotos.txt','w')
    fotos.write("0 \n")
    fotos.close()
    time.sleep(1)
