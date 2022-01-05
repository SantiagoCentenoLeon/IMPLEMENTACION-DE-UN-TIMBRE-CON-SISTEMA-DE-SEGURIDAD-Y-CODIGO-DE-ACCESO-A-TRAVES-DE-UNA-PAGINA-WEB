#!/usr/bin/env python
# -*- coding: cp1252 -*-
while(1):
        import ftplib
        import os
        import time
        # Datos FTP
        ftp_servidor = 'files.000webhost.com'
        ftp_usuario  = 'safedoorbell'
        ftp_clave    = 'n1v3l1nd4'
        ftp_raiz     = '/public_html' # Carpeta del servidor donde queremos subir el fichero
 
        # Datos del fichero a subir
        fichero_origen = 'C:/Users/santiago/Desktop/proyectoembebidos/Imagen1' # Ruta al fichero que vamos a subir
        fichero_destino = 'Imagen1' # Nombre que tendrá el fichero en el servidor
 
        # Conectamos con el servidor
        try:
                s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
                try:
                        f = open(fichero_origen, 'rb')
                        s.cwd(ftp_raiz)
                        s.storbinary('STOR ' + fichero_destino, f)
                        f.close()
                        s.quit()
                except:
                        print "No se ha podido encontrar el fichero " + fichero_origen
        except:
                print "No se ha podido conectar al servidor " + ftp_servidor


        time.sleep(1)
        # Datos del fichero a subir
        fichero_origen = 'C:/Users/santiago/Desktop/proyectoembebidos/sistemasembebidos.html' # Ruta al fichero que vamos a subir
        fichero_destino = 'sistemasembebidos.html' # Nombre que tendrá el fichero en el servidor
 
        # Conectamos con el servidor
        try:
                s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
                try:
                        f = open(fichero_origen, 'rb')
                        s.cwd(ftp_raiz)
                        s.storbinary('STOR ' + fichero_destino, f)
                        f.close()
                        s.quit()
                except:
                        print "No se ha podido encontrar el fichero " + fichero_origen
        except:
                print "No se ha podido conectar al servidor " + ftp_servidor
