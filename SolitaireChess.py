#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys
import random

# Autores:
# Angelica Acosta 14-10005
# Yeferson Licet  14-10572
# Proyecto de CI2691

pygame.image.get_extended()
pygame.font.init()

seconds = 0
clock 	= pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

#Constantes de programacion
screen_caption 		= "Solitaire chess"
screen_background 	= (0, 0, 0) #color de la pantalla negro RGBA colores
screen_width 		= 960
screen_height 		= 670
tablero_manual		= ""

files 	= ['partidasnuevas.txt', 'partidasguardadas.txt', 'records.txt']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Definicion de cada pieza/elemento
tablero          		= ['grid500.png', 500, 500] #foto,alto,ancho
name_input       		= ['name.png', 500, 160]
alerta           		= ['alerta.png', 460, 60]
button_exit      		= ['scape.png', 290, 80]

logo_desc        		= ['logo.png', 400, 180]
button_nueva     		= ['bnueva.png', 400, 120]
button_cargar    		= ['bcargar.png', 280, 80]
button_records   		= ['brecords.png', 280, 80]
button_salir     		= ['bsalir.png', 280, 80]
button_facil     		= ['facil.png', 400, 80]
button_dificil   		= ['dificil.png', 280, 80]
button_muydificil 	 	= ['muydificil.png', 280, 80]
button_entrenamiento	= ['entrenamiento.png', 280, 80]
button_aleatorio 		= ['aleatorio.png', 400, 80]
button_crear    		= ['creartablero.png', 280, 80]
ingresar_tablero     	= ['ingresar_tablero.png', 500, 160]
rcrds_title     		= ['records.png', 280, 80]
rcrds_facil     		= ['facilr.png', 280, 80]
rcrds_dificil     		= ['dificilr.png', 280, 80]
rcrds_muydificil     	= ['muydificilr.png', 280, 80]
rcrds_tools     		= ['inrecords.png', 500, 120]

reina 					= ['queen.png', 128, 128]
rey 	 				= ['king.png', 128, 128]
torre  					= ['rook.png', 128, 128]
peon 	 				= ['pawn.png', 128,128]
caballo  				= ['horse.png', 128, 128]
alfil 	 				= ['bishop.png', 128, 128]

button_jugar  			= ['jugar.png', 280, 80]
pausar        			= ['pausar.png', 280, 80]
deshacer      			= ['deshacer.png',280, 80]
terminar      			= ['terminar.png', 280, 80]
button_vacio  			= ['empty.png', 280, 80]
p_inicial     			= ['inicial.png', 246, 120]
p_final       			= ['final.png', 246, 120]

p_perdiste   			= ['perdiste.png', 280,80]
p_ganaste    			= ['ganaste.png', 280, 80]
hint          			= ['hint.png', 136, 141]
solucion      			= ['solucion.png', 320, 120]

button_guardar 			= ['guardarpartida.png', 280, 80]
button_menu    			= ['volvermenu.png', 280, 80]
button_partida 			= ['partidaes.png', 500, 120]
partida_input  			= ['numeropartida.png', 500, 120]
button_pausado 			= ['pausado.png', 500, 120]
_image_library 			= {}

# Carga una imagen desde la carpeta raiz
# @param path: ruta de la foto a carcar
# @return image object
def Logic_getImage(path): #carga la foto de la compu y lo vuelve una variable
	global _image_library
	
	try:
		image = _image_library.get(path)
		if image == None:
				canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
				image = pygame.image.load(canonicalized_path)
				_image_library[path] = image
		return image
	except:
		print("Error al iniciar el juego")

#Draw tablero centered horizontal
logo            = Logic_getImage(logo_desc[0])
salida          = Logic_getImage(button_exit[0])
jugar           = Logic_getImage(tablero[0])
nueva_partida   = Logic_getImage(button_nueva[0])
cargar_partida  = Logic_getImage(button_cargar[0])
records         = Logic_getImage(button_records[0])
salir           = Logic_getImage(button_salir[0])
name            = Logic_getImage(name_input[0])
alerta_drawable = Logic_getImage(alerta[0])
facil           = Logic_getImage(button_facil[0])
dificil         = Logic_getImage(button_dificil[0])
muydificil      = Logic_getImage(button_muydificil[0])
entrenamiento   = Logic_getImage(button_entrenamiento[0])
aleatorio       = Logic_getImage(button_aleatorio[0])
crear_partida   = Logic_getImage(button_crear[0])

ficha_king    	= Logic_getImage(rey[0])
ficha_reina   	= Logic_getImage(reina[0])
ficha_alfil   	= Logic_getImage(alfil[0])
ficha_torre   	= Logic_getImage(torre[0])
ficha_peon    	= Logic_getImage(peon[0])
ficha_caballo 	= Logic_getImage(caballo[0])

ficha_king 		= pygame.transform.scale(ficha_king, (70, 70))
ficha_reina 	= pygame.transform.scale(ficha_reina, (70, 70))
ficha_alfil 	= pygame.transform.scale(ficha_alfil, (70, 70))
ficha_torre 	= pygame.transform.scale(ficha_torre, (70, 70))
ficha_peon 		= pygame.transform.scale(ficha_peon, (70, 70))
ficha_caballo 	= pygame.transform.scale(ficha_caballo, (70, 70))

b_jugar    		= Logic_getImage(button_jugar[0])
b_pausar   		= Logic_getImage(pausar[0])
b_deshacer 		= Logic_getImage(deshacer[0])
b_terminar 		= Logic_getImage(terminar[0])
b_vacio    		= Logic_getImage(button_vacio[0])

b_jugar   		= pygame.transform.scale(b_jugar, (190, 54))
b_pausar   		= pygame.transform.scale(b_pausar, (190, 54))
b_deshacer 		= pygame.transform.scale(b_deshacer, (190, 54))
b_terminar 		= pygame.transform.scale(b_terminar, (190, 54))
b_vacio    		= pygame.transform.scale(b_vacio,(140,54))

b_guardar   	= Logic_getImage(button_guardar[0])
b_menu      	= Logic_getImage(button_menu[0])
tu_partida 		= Logic_getImage(button_partida[0])
partida     	= Logic_getImage(partida_input[0])
pausado    		= Logic_getImage(button_pausado[0])

drawable_inicial= Logic_getImage(p_inicial[0])
drawable_final 	= Logic_getImage(p_final[0])
d_perdiste 	 	= Logic_getImage(p_perdiste[0])
d_ganaste 	 	= Logic_getImage(p_ganaste[0])

drawable_rtitle = Logic_getImage(rcrds_title[0])
drawable_ftitle = Logic_getImage(rcrds_facil[0])
drawable_dtitle = Logic_getImage(rcrds_dificil[0])
drawable_mtitle = Logic_getImage(rcrds_muydificil[0])

drawable_tools_rc	= Logic_getImage(rcrds_tools[0])
drawable_ftitle 	= pygame.transform.scale(drawable_ftitle, (2*rcrds_facil[1]//3,2*rcrds_facil[2]//3))
drawable_dtitle 	= pygame.transform.scale(drawable_dtitle, (2*rcrds_facil[1]//3,2*rcrds_facil[2]//3))
drawable_mtitle 	= pygame.transform.scale(drawable_mtitle, (2*rcrds_facil[1]//3,2*rcrds_facil[2]//3))

salida 				= pygame.transform.scale(salida, (160,50))
i_tablero 			= Logic_getImage(ingresar_tablero[0])
drawable_hint		= Logic_getImage(hint[0])
drawable_hint 		= pygame.transform.scale(drawable_hint, (2*hint[1]//3+8,2*hint[2]//3+8))
drawable_solucion 	= Logic_getImage(solucion[0])
drawable_solucion   = pygame.transform.scale(drawable_solucion, (2*solucion[1]//3,2*solucion[2]//3))

screen 				= pygame.display.set_mode((screen_width, screen_height))
myfont 				= pygame.font.SysFont(None, 18) 

# Pinta de negro el fotograma
# @param screen: screen principal del juego
# @return void
def Render_drawSurface(screen):
	try:
		assert(isinstance(screen, pygame.Surface))
		pygame.display.set_caption(screen_caption)
		screen.fill(screen_background)
	except:
		print("Error al renderizar la pantalla")

#Configuracion inicial de la ventana
screen.blit(logo, (960/2-logo_desc[1]//2, 40))
screen.blit(name, (960/2-name_input[1]/2, logo_desc[2] + 80))
screen.blit(salida, (0,0))
pygame.display.flip()

tablero_original 		= []
piezas_muertas 			= []
piezas_vivas 			= []
movimientos_realizados 	= []
records_facil 			= []
records_dificil 		= []
records_muydificil 		= []
page 					= 0
nombrejugador 			= ""
toplay 					= []

positions_x = [960/2-tablero[1]//2+55,960/2-tablero[1]//2+174,960/2-tablero[1]//2+292,960/2-tablero[1]//2+409]
positions_y = [407,293,175,60]

running 		= True
pantalla		= 'principal'
nivel 			= -1
movimiento 		= ["",""]
numero_partida 	= ''

#Start the screen
Render_drawSurface(screen)

# Renderiza la vista cuando se ingresa el nombre de usuario
# @param none
# @return void
def Render_Input(seccion):
	try:
		assert(seccion == 'principal' or seccion == 'carga')

		if seccion == 'principal':
			Render_drawSurface(screen)
			screen.blit(salida, (0,0))
			screen.blit(logo, (960/2-logo_desc[1]//2, 40))
			screen.blit(name, (960/2-name_input[1]/2, logo_desc[2] + 80))
			textsurface = myfont.render(nombrejugador, True, (255,255,255)) #coloca lo que hayas puesto de nombre
			screen.blit(textsurface,(960/2-name_input[1]/2 + 90, logo_desc[2] + name_input[2]//2 + 72 ))			
			pygame.display.flip()
		
		elif seccion == 'carga':
			Render_drawSurface(screen)
			screen.blit(salida, (0,0))
			screen.blit(logo, (960/2-logo_desc[1]//2, 40))
			screen.blit(partida, (960/2-partida_input[1]/2, logo_desc[2] + 80))
			textsurface = myfont.render(numero_partida, True, (255,255,255)) #coloca lo que hayas puesto de nombre
			screen.blit(textsurface,(960/2-partida_input[1]/2 + 200, logo_desc[2] + partida_input[2]//2 + 87 ))			
			pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista del menu principal
# @param none
# @return void
def Render_Screen():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(salida, (0,0))
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(nueva_partida, (960/2-button_nueva[1]/2, logo_desc[2] + 80))
		screen.blit(cargar_partida, (960/2-button_cargar[1]/2, logo_desc[2] + button_nueva[2] + 80))
		screen.blit(records, (960/2-button_records[1]/2, logo_desc[2] + button_nueva[2]+button_cargar[2] + 80))
		screen.blit(salir, (960/2-button_salir[1]/2, logo_desc[2] + button_nueva[2]+button_cargar[2]+button_records[2] + 80))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista de seleccion de nivel
# @param none
# @return void
def Render_Level():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(salida, (0,0))
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(facil, (960/2-button_facil[1]/2, logo_desc[2] + 80))
		screen.blit(dificil, (960/2-button_dificil[1]/2, logo_desc[2] + button_facil[2] + 120))
		screen.blit(muydificil, (960/2-button_muydificil[1]/2, logo_desc[2] + button_facil[2]+button_dificil[2] + 120))
		screen.blit(entrenamiento, (960/2-button_entrenamiento[1]/2, logo_desc[2] + button_facil[2]+button_dificil[2]+button_muydificil[2] + 120))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista de seleccion de modo de juego
# @param none
# @return void	
def Render_Mode():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(salida, (0,0))
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(aleatorio, (960/2-button_aleatorio[1]/2, logo_desc[2] + 80))
		screen.blit(crear_partida, (960/2-button_crear[1]/2, logo_desc[2] + button_aleatorio[2] + 160))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista cuando hay un error en el input del usuario
# @param type_error: tipo de error a mostrar
# @return void
def Render_ErrorInput(type_error):
	try:
		assert(0 <= type_error <= 4)

		Render_drawSurface(screen)
		if pantalla == 'menu_principal':
			Render_Screen()
		elif pantalla == 'principal':
			Render_Input('principal')
		elif pantalla == 'menu_jugar':
			Render_Level()
		elif pantalla == 'menu_facil' or pantalla == 'menu_dificil' or pantalla == 'menu_entrenamiento':
			Render_Mode()
		elif pantalla == 'menu_cargar':
			Render_Input('carga')
		
		if type_error == 0:
			textsurface = myfont.render('Debes introducir un nombre', True, (255,255,255))
		elif type_error == 1:
			textsurface = myfont.render('Opcion invalida', True, (255,255,255))
		elif type_error == 2:
			textsurface = myfont.render('Debes introducir un numero', True, (255,255,255))
		elif type_error == 3:
			textsurface = myfont.render('Partida inexistente', True, (255,255,255))
		elif type_error == 4:
			textsurface = myfont.render('Error al cargar nivel', True, (255,255,255))

		screen.blit(alerta_drawable, (alerta[1]//2+20, logo_desc[2]+25))
		screen.blit(textsurface,(960/2-name_input[1]/2 + 90, logo_desc[2]+50))			

		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista para guardar o terminar una partida
# @param none
# @return void
def Render_Finish():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(b_guardar, (960/2-button_guardar[1]/2, logo_desc[2] + 140))
		screen.blit(b_menu, (960/2-button_menu[1]/2, logo_desc[2] + button_guardar[2] + 160))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista del numero de la partida guardada
# @param number: numero de la partida
# @return void
def Render_Game(number):
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(tu_partida, (960/2-button_partida[1]/2, logo_desc[2] + 100))
		textsurface = myfont.render(number, True, (255,255,255))
		screen.blit(textsurface,(960/2-button_partida[1]/2 + 200, logo_desc[2]+170))
		levelsurface = myfont.render('Presiona cualquier tecla para volver al menu', True, (255,255,255)) 
		screen.blit(levelsurface,(960/2-button_partida[1]/2 + 120, logo_desc[2] + 250))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista en pausa
# @param none
# @return void
def Render_Stop():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(pausado, (960/2-button_pausado[1]/2, logo_desc[2] + 120))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")
# Renderiza la vista de seleccion de modo de juego cuando hay errores
# @param mensaje: tipo de error a mostrar
# @return void	
def Render_ErrorMode(mensaje):
	try:
		assert(isinstance(screen, pygame.Surface) and mensaje != "")
		if pantalla == 'menu_facil' or pantalla == 'menu_dificil' or pantalla == 'menu_entrenamiento':
			Render_drawSurface(screen)
			screen.blit(salida, (0,0))
			screen.blit(logo, (960/2-logo_desc[1]//2, 40))
			screen.blit(aleatorio, (960/2-button_aleatorio[1]/2, logo_desc[2] + 80))
			screen.blit(crear_partida, (960/2-button_crear[1]/2, logo_desc[2] + button_aleatorio[2] + 160))
			textsurface = myfont.render(mensaje, True, (255,255,255))
			screen.blit(alerta_drawable, (alerta[1]//2+20, logo_desc[2]+25))
			screen.blit(textsurface,(960/2-name_input[1]/2 + 90, logo_desc[2]+50))			
		elif pantalla == 'terminando':
			Render_drawSurface(screen)
			screen.blit(logo, (960/2-logo_desc[1]//2, 40))
			screen.blit(b_guardar, (960/2-button_guardar[1]/2, logo_desc[2] + 140))
			screen.blit(b_menu, (960/2-button_menu[1]/2, logo_desc[2] + button_guardar[2] + 160))
			textsurface = myfont.render(mensaje, True, (255,255,255))
			screen.blit(alerta_drawable, (alerta[1]//2+20, logo_desc[2]+50))
			screen.blit(textsurface,(960/2-name_input[1]/2 + 120, logo_desc[2]+75))
		
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista de la pantalla jugar/tablero
# @param none
# @return void	
def Render_Play():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(jugar, (960/2-tablero[1]//2, 40))
		usuario = pygame.font.SysFont(None, 30).render(nombrejugador, True, (255,255,255))
		screen.blit(usuario,(960/2-len(nombrejugador)*5,15))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Genera un tablero aleatorio en el nivel seleccionado
# @param level: nivel
# @return list	
def Logic_GenerateLevel(level):
	try:
		assert(0 <= level <= 3)
	except:
		return -1
	
	archivo_partidas  = open(files[0], 'r')
	partidas  = archivo_partidas.readlines()
	
	partidas_niveles =[[],[],[],[]]
	
	try:
		assert(len(partidas) > 0)
	except:
		return -1

	for x in range(len(partidas)):
		try:
			columns = partidas[x].split(",")
			partidas_niveles[int(columns[1])].append(columns[0])
		except:
			pass

	if level == 3:
		level = random.randint(0, 1)

	if level == 2:

		try:
			assert(len(partidas_niveles[0]) + len(partidas_niveles[1]) >= 3)
		except:
			return -1

		while len(toplay) < 3:

			level = random.randint(0, 1)
			if len(partidas_niveles[level]) > 0:
				y = random.randint(0, len(partidas_niveles[level])-1)
				if partidas_niveles[level][y] not in toplay:
					toplay.append(partidas_niveles[level][y])
		return toplay[0]
	
	else:
		try:
			assert(len(partidas_niveles[level]) > 0)
		except:
			return -1

		y = random.randint(0, len(partidas_niveles[level])-1)
		archivo_partidas.close()
		return partidas_niveles[level][y]

# Genera un tablero de una partida guardada
# @param none
# @return tiempo_restante: tiempo restante en la partida
# @return nivel_actual: nivel de la partida
# @return vivas: piezas vivas de la partida
# @return movimientos: movimientos realizados en la partida
# @return muertas: piezas eliminadas de la partida
# @return existe: determina si la partida esta guardada
def Logic_LoadLevel():
	try:
		archivo = open(files[1],'r')
		partidas_guardadas = archivo.readlines()

		assert(len(partidas_guardadas) >= 0)

		tiempo_restante = 0
		nivel_actual = -1
		vivas = []
		movimientos = []
		muertas = []
		existe = False

		for i in range(len(partidas_guardadas)):
			partida = partidas_guardadas[i].split("-")
			
			if partida[0] == nombrejugador and partida[1] == numero_partida:
				tiempo_restante = int(partida[2])
				nivel_actual = int(partida[3]) 
				vivas = eval(partida[4])
				movimientos = eval(partida[5])
				muertas =eval(partida[6].rstrip('\r\n'))
				existe = True
		
		return tiempo_restante, nivel_actual, vivas, movimientos, muertas, existe
	except:
		print("Error al cargar tablero")

# Convierte una letra a una posicion en el tablero
# @param cadena: string que define la posicion
# @return int
def Logic_LetterToNumbers(cadena):
	try:
		assert(isinstance(cadena, str))
		
		letras = ["a","b","c","d"]
		for x in range(len(letras)):
			if cadena == letras[x]:
				return x
		return -1
	except:
		print("Error al convertir string")

# Convierte una letra a una nombre de pieza
# @param cadena: string con la inicial de la pieza
# @return string
def Logic_LetterToPieces(cadena):
	try:
		assert(isinstance(cadena, str))
		if cadena.capitalize() == 'A':
			return "alfil"
		elif cadena.capitalize() == 'D':
			return "reina"
		elif cadena.capitalize() == 'R':
			return "rey"
		elif cadena.capitalize() == 'T':
			return "torre"
		elif cadena.capitalize() == 'C':
			return "caballo"
	except:
		print("Error al convertir string")

# Convierte una letra a una nombre de pieza
# @param none
# @return booleano
def Logic_Lost():
	try:
		assert(isinstance(nivel, int))
		if nivel == 0:
			available_time = 180
		elif nivel == 1:
			available_time = 90
		elif nivel == 2:
			available_time = 120
		
		if available_time-seconds == 0:
			status = True
		else:
			status = False
		return status
	except:
		print("Error al calcular el nivel")

# Renderiza el tablero de juego con sus fichas
# @param none
# @return void
def Render_Board():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_Play() 

		for i in range(len(piezas_vivas)):
			if piezas_vivas[i][0] == 'caballo':
				renderiza = ficha_caballo
			elif piezas_vivas[i][0] == 'alfil':
				renderiza = ficha_alfil
			elif piezas_vivas[i][0] == 'reina':
				renderiza = ficha_reina
			elif piezas_vivas[i][0] == 'rey':
				renderiza = ficha_king
			elif piezas_vivas[i][0] == 'torre':
				renderiza = ficha_torre
			elif piezas_vivas[i][0] == 'peon':
				renderiza = ficha_peon

			screen.blit(renderiza, (positions_x[piezas_vivas[i][1]], positions_y[piezas_vivas[i][2]]))
			pygame.display.flip()

		screen.blit(b_jugar, (100, tablero[2] + 70))
		screen.blit(b_pausar, (button_jugar[1]+25, tablero[2] + 70))
		screen.blit(b_deshacer, (button_jugar[1]+228, tablero[2] + 70))
		screen.blit(b_terminar, (button_jugar[1]+432, tablero[2] + 70))

		if Logic_LevelToString() == "ENTRENAMIENTO":
			levelsurface = pygame.font.SysFont(None, 20).render(Logic_LevelToString(), True, (255,255,255))
		else:
			levelsurface = pygame.font.SysFont(None, 30).render(Logic_LevelToString(), True, (255,255,255))

		screen.blit(levelsurface,(90,222))	
		
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza el tiempo
# @param none
# @return void
def Render_Time():
	try:
		assert(isinstance(screen, pygame.Surface))
		pygame.draw.rect(screen, (0,0,0), (85,320,100,50))
		
		if nivel <= 2:	
			timesurface = pygame.font.SysFont(None, 30).render(Logic_Time(), True, (255,255,255))
			screen.blit(timesurface,(90,322))
		
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Calcula el tiempo transcurrido y devuelve el tiempo restante
# @param none
# @return string
def Logic_Time():
	try:
		assert(isinstance(nivel, int))

		if nivel == 0:
			available_time = 180
		elif nivel == 1:
			available_time = 90
		elif nivel == 2:
			available_time = 120
		else:
			available_time = 10**10 #tiempo infinito en entrenamiento

		return str((available_time-seconds)//60) + ":"+str((available_time-seconds)%60)
	except:
		print("Error al calcular el nivel")

# Convierte el nivel actual de entero a palabra
# @param none
# @return string
def Logic_LevelToString():
	try:
		assert(isinstance(nivel, int))
		if nivel == 0:
			return "FACIL"
		elif nivel == 1:
			return "DIFICIL"
		elif nivel == 2:
			return "MUY DIFICIL"
		elif nivel == 3:
			return "ENTRENAMIENTO"
	except:
		print("Error al calcular el nivel")

# Muestra una alerta al introducir movimiento incorrecto
# @param mov: define si es el movimiento inicial o el de destino
# @return void
def Render_ErrorPlaying(mov):
	try:
		assert(isinstance(mov, int))
		assert(isinstance(screen, pygame.Surface))

		Render_Play() 

		for i in range(len(piezas_vivas)):
			if piezas_vivas[i][0] == 'caballo':
				renderiza = ficha_caballo
			elif piezas_vivas[i][0] == 'alfil':
				renderiza = ficha_alfil
			elif piezas_vivas[i][0] == 'reina':
				renderiza = ficha_reina
			elif piezas_vivas[i][0] == 'rey':
				renderiza = ficha_king
			elif piezas_vivas[i][0] == 'torre':
				renderiza = ficha_torre
			elif piezas_vivas[i][0] == 'peon':
				renderiza = ficha_peon

			screen.blit(renderiza, (positions_x[piezas_vivas[i][1]], positions_y[piezas_vivas[i][2]]))
			pygame.display.flip()
			
		if mov == 0:
			screen.blit(drawable_inicial, (960//2 - p_final[1]//2, tablero[2] + 50))
		elif mov == 1:
			screen.blit(drawable_final, (960//2 - p_final[1]//2, tablero[2] + 50))

		
		if mov == 0 or mov == 1:
			if Logic_LevelToString() == "ENTRENAMIENTO":
				levelsurface = pygame.font.SysFont(None, 20).render(Logic_LevelToString(), True, (255,255,255))
			else:
				levelsurface = pygame.font.SysFont(None, 30).render(Logic_LevelToString(), True, (255,255,255))
	
			screen.blit(levelsurface,(90,222))
			textsurface = myfont.render('Movimiento incorrecto', True, (255,255,255))
			screen.blit(pygame.transform.scale(alerta_drawable, (alerta[1]//2, alerta[2]//2)), (960//2 - alerta[1]//4, tablero[2] + 30))
			screen.blit(textsurface,(960//2 - alerta[1]//4 + 50, tablero[2] + 40))

			if mov == 0:
				textsurface = pygame.font.SysFont(None, 36).render(movimiento[0], True, (255,255,255))
			else:
				textsurface = pygame.font.SysFont(None, 36).render(movimiento[1], True, (255,255,255))
			screen.blit(textsurface,(960//2 - p_final[1]//2+100, tablero[2] + 112))	

			pygame.display.flip()
		
		elif mov == 2:

			screen.blit(b_jugar, (100, tablero[2] + 70))
			screen.blit(b_pausar, (button_jugar[1]+25, tablero[2] + 70))
			screen.blit(b_deshacer, (button_jugar[1]+228, tablero[2] + 70))
			screen.blit(b_terminar, (button_jugar[1]+432, tablero[2] + 70))
			
			if Logic_LevelToString() == "ENTRENAMIENTO":
				levelsurface = pygame.font.SysFont(None, 20).render(Logic_LevelToString(), True, (255,255,255))
			else:
				levelsurface = pygame.font.SysFont(None, 30).render(Logic_LevelToString(), True, (255,255,255))

			screen.blit(levelsurface,(90,222))	
			textsurface = myfont.render('No puede deshacer', True, (255,255,255))
			screen.blit(pygame.transform.scale(alerta_drawable, (alerta[1]//2, alerta[2]//2)), (960//2 - alerta[1]//4, tablero[2] + 30))
			screen.blit(textsurface,(960//2 - alerta[1]//4 + 50, tablero[2] + 40))	
			pygame.display.flip()
		
		elif mov == 3:
			screen.blit(b_jugar, (100, tablero[2] + 70))
			screen.blit(b_pausar, (button_jugar[1]+25, tablero[2] + 70))
			screen.blit(b_deshacer, (button_jugar[1]+228, tablero[2] + 70))
			screen.blit(b_terminar, (button_jugar[1]+432, tablero[2] + 70))
			
			if Logic_LevelToString() == "ENTRENAMIENTO":
				levelsurface = pygame.font.SysFont(None, 20).render(Logic_LevelToString(), True, (255,255,255))
			else:
				levelsurface = pygame.font.SysFont(None, 30).render(Logic_LevelToString(), True, (255,255,255))

			screen.blit(levelsurface,(90,222))	
			textsurface = myfont.render('No puede pausar', True, (255,255,255))
			screen.blit(pygame.transform.scale(alerta_drawable, (alerta[1]//2, alerta[2]//2)), (960//2 - alerta[1]//4, tablero[2] + 30))
			screen.blit(textsurface,(960//2 - alerta[1]//4 + 50, tablero[2] + 40))	
			pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")


# Renderiza el input para colocar un nuevo movimiento
# @param mov: define si es el movimiento inicial o el de destino
# @return void
def Render_Move(mov):
	try:
		assert(isinstance(mov, int))
		assert(isinstance(screen, pygame.Surface))
		
		Render_Play() 

		for i in range(len(piezas_vivas)):
			if piezas_vivas[i][0] == 'caballo':
				renderiza = ficha_caballo
			elif piezas_vivas[i][0] == 'alfil':
				renderiza = ficha_alfil
			elif piezas_vivas[i][0] == 'reina':
				renderiza = ficha_reina
			elif piezas_vivas[i][0] == 'rey':
				renderiza = ficha_king
			elif piezas_vivas[i][0] == 'torre':
				renderiza = ficha_torre
			elif piezas_vivas[i][0] == 'peon':
				renderiza = ficha_peon

			screen.blit(renderiza, (positions_x[piezas_vivas[i][1]], positions_y[piezas_vivas[i][2]]))
		
		if mov == 0:
			screen.blit(drawable_inicial, (960//2 - p_final[1]//2, tablero[2] + 50))
			textsurface = pygame.font.SysFont(None, 36).render(movimiento[0], True, (255,255,255))
			screen.blit(textsurface,(960//2 - p_final[1]//2+100, tablero[2] + 112))	
		elif mov == 2:
			screen.blit(drawable_inicial, (960//2 - p_final[1]//2, tablero[2] + 50))
			textsurface = pygame.font.SysFont(None, 36).render(movimiento[0], True, (255,255,255))
			screen.blit(textsurface,(960//2 - p_final[1]//2+100, tablero[2] + 112))	
			textsurface = myfont.render('Ficha sin solucion', True, (255,255,255))
			screen.blit(pygame.transform.scale(alerta_drawable, (alerta[1]//2, alerta[2]//2)), (960//2 - alerta[1]//4, tablero[2] + 30))
			screen.blit(textsurface,(960//2 - alerta[1]//4 + 50, tablero[2] + 40))	
		else:
			screen.blit(drawable_final, (960//2 - p_final[1]//2, tablero[2] + 50))
			textsurface =  pygame.font.SysFont(None, 36).render(movimiento[1], True, (255,255,255))
			screen.blit(textsurface,(960//2 - p_final[1]//2+100, tablero[2] + 112))

		if Logic_LevelToString() == "ENTRENAMIENTO":
			levelsurface = pygame.font.SysFont(None, 20).render(Logic_LevelToString(), True, (255,255,255))
		else:
			levelsurface = pygame.font.SysFont(None, 30).render(Logic_LevelToString(), True, (255,255,255))
	
		screen.blit(levelsurface,(90,222))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza los posibles movimientos validos para una pieza seleccionada
# @param solutions: posibles posiciones validas
# @return void
def Render_Solutions(solutions):
	try:
		assert(isinstance(solutions, list))
		assert(isinstance(screen, pygame.Surface))

		Render_Play() 

		for i in range(len(solutions)):
			posx,posy = int(positions_x[solutions[i][1]]-13),int(positions_y[solutions[i][2]]-13)
			screen.blit(drawable_hint,(posx, posy))	
		
		screen.blit(drawable_solucion,(900 - solucion[1]//2, 40))	
		
		mov = 1

		for i in range(len(piezas_vivas)):
			if piezas_vivas[i][0] == 'caballo':
				renderiza = ficha_caballo
			elif piezas_vivas[i][0] == 'alfil':
				renderiza = ficha_alfil
			elif piezas_vivas[i][0] == 'reina':
				renderiza = ficha_reina
			elif piezas_vivas[i][0] == 'rey':
				renderiza = ficha_king
			elif piezas_vivas[i][0] == 'torre':
				renderiza = ficha_torre
			elif piezas_vivas[i][0] == 'peon':
				renderiza = ficha_peon

			screen.blit(renderiza, (positions_x[piezas_vivas[i][1]], positions_y[piezas_vivas[i][2]]))
		
		screen.blit(drawable_final, (960//2 - p_final[1]//2, tablero[2] + 50))
		textsurface =  pygame.font.SysFont(None, 36).render(movimiento[1], True, (255,255,255))
		screen.blit(textsurface,(960//2 - p_final[1]//2+100, tablero[2] + 112))
		
		if Logic_LevelToString() == "ENTRENAMIENTO":
			levelsurface = pygame.font.SysFont(None, 20).render(Logic_LevelToString(), True, (255,255,255))
		else:
			levelsurface = pygame.font.SysFont(None, 30).render(Logic_LevelToString(), True, (255,255,255))
		
		screen.blit(levelsurface,(90,222))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Genera un tablero en forma de lista a partir de un string
# @param partida: string en formato de ajedrez
# @return list
def Logic_Board(partida):
	
	try:
		assert(isinstance(partida,str))
		piecitas = partida.split("-")
		tablero_original = []
		assert(2 <= len(piecitas) <= 10)
	except:
		return -1

	for i in range(len(piecitas)):

		if len(piecitas[i]) == 2:
			letra_x = Logic_LetterToNumbers(piecitas[i][0])
			
			if letra_x == -1:
				return -1

			try:	
				for x in range(len(tablero_original)):
					assert(tablero_original[x][1] != letra_x or tablero_original[x][2] != int(piecitas[i][1])-1)

				tablero_original.append(['peon', letra_x, int(piecitas[i][1])-1])
			except:
				return -1
				
		elif len(piecitas[i]) == 3:
			letra_x = Logic_LetterToNumbers(piecitas[i][1])
			
			if letra_x == -1:
				return -1
			try:
				for x in range(len(tablero_original)):
					assert(tablero_original[x][1] != letra_x or tablero_original[x][2] != int(piecitas[i][2])-1)
					
				tablero_original.append([Logic_LetterToPieces(piecitas[i][0]), letra_x, int(piecitas[i][2])-1])
			except:
				return -1

		else:
			return -1
	
	try:
		assert(2 <= len(tablero_original) <= 10)
	except:
		return -1

	for i in range(len(tablero_original)):
		if tablero_original[i][0] ==  'reina' or tablero_original[i][0] == 'rey':
			for j in range(len(tablero_original)):
				if i != j and tablero_original[i][0] == tablero_original[j][0]:
					return -1
		if tablero_original[i][0] == 'torre' or tablero_original[i][0] == 'alfil' or tablero_original[i][0] == 'caballo' or tablero_original[i][0] == 'peon':
			for j in range(len(tablero_original)):
				if i != j and tablero_original[i][0] == tablero_original[j][0]:
					for k in range(len(tablero_original)):
						if i != j and i != k and j != k and tablero_original[i][0] == tablero_original[k][0]:
							return -1
	return tablero_original

# Renderiza la finalizacion de la partida
# @param type_end: int define si el jugador pierde o gana
# @return void
def Render_EndGame(type_end):
	try:
		assert(type_end == 1 or type_end == 2)

		Render_drawSurface(screen)
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))

		if type_end == 1:
			screen.blit(d_ganaste, (960/2-p_ganaste[1]/2, logo_desc[2] + 80))
		else:
			screen.blit(d_perdiste, (960/2-p_perdiste[1]/2, logo_desc[2] + 80))

		levelsurface = myfont.render('Presiona cualquier tecla para volver al menu', True, (255,255,255)) 
		screen.blit(levelsurface,(960/2-p_perdiste[1]/2 + 10, logo_desc[2] + 200))	

		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Valida si la partida ha sido ganada, perdida o continua siendo valida
# 1 gana, 2 pierde
# @param none
# @return int
def Logic_Validate():
	try:
		assert(isinstance(piezas_vivas,list))

		if len(piezas_vivas) == 1:
			existe_rey = False
			for x in range(len(piezas_muertas)):
				if piezas_muertas[x][0] == 'rey':
					existe_rey = True
					break
			
			if piezas_vivas[0][1] != 'rey' and existe_rey:
				return 2
			else:
				return 1
		else:
			canMove = False

			for i in range(len(piezas_vivas)):
				move_from = [int(piezas_vivas[i][1]), int(piezas_vivas[i][2])]
				pieza_moviendo = piezas_vivas[i][0]

				for k in range(len(piezas_vivas)):
					move_to = [int(piezas_vivas[k][1]), int(piezas_vivas[k][2])]
					canMove = Logic_Position(pieza_moviendo, move_from[0], move_from[1], move_to[0], move_to[1])
					if canMove:
						return -1

			return 2
	except:
		print("Error al renderizar")

# Define si una pieza puede ser movida
# @param pieza:str, x,y posiciones iniciales, x1,y1 posiciones finales
# @return booleano
def Logic_Position(pieza,x,y,x1,y1):
    PosicionValida=False
    try:
        assert(0<=x<=3 and 0<=y<=3 and 0<=x1<=3 and 0<=y1<=3
               and int(x)==x and int(y)==y and int(x1)==x1 and int(y1)==y1)
        
        if pieza=='peon':
            if (x1==x+1 or x1==x-1) and (y1==y+1):
                for i in range(len(piezas_vivas)):
                    if piezas_vivas[i][1]==x1 and piezas_vivas[i][2]==y1:
                        PosicionValida=True
                        break
                    else:
                        pass
            else:
                pass
            
        elif pieza=='caballo':
            if (((x1==x+2 or x1==x-2) and (y1==y+1 or y1==y-1))
                or ((x1==x+1 or x1==x-1) and (y1==y+2 or y1==y-2))):
                for i in range(len(piezas_vivas)):
                    if piezas_vivas[i][1]==x1 and piezas_vivas[i][2]==y1:
                        PosicionValida=True
                        break
                    else:
                        pass
            else:
                pass

        elif pieza=='torre':
            if (((x1==x+1 or x1==x+2 or x1==x+3 or x1==x-1
                or x1==x-2 or x1==x-3) and y1==y)
                or ((y1==y+1 or y1==y+2 or y1==y+3 or y1==y-1
                or y1==y-2 or y1==y-3) and x1==x)):
                for i in range(len(piezas_vivas)):
                    if piezas_vivas[i][1]==x1 and piezas_vivas[i][2]==y1:
                        PosicionValida=True
                        break
                    else:
                        pass
            else:
                pass

        elif pieza=='rey':
            if (((x1==x+1 or x1==x-1) and (y1==y+1 or y1==y-1 or y1==y))
                or ((y1==y+1 or y1==y-1) and (x1==x+1 or x1==x-1 or x1==x))):
                for i in range(len(piezas_vivas)):
                    if piezas_vivas[i][1]==x1 and piezas_vivas[i][2]==y1:
                        PosicionValida=True
                        break
                    else:
                        pass
            else:
                pass

        elif pieza=='alfil':
            if (((x1==x+1 or x1==x-1) and (y1==y+1 or y1==y-1))
                or ((x1==x+2 or x1==x-2) and (y1==y+2 or y1==y-2))
                or ((x1==x+3 or x1==x-3) and (y1==y+3 or y1==y-3))):
                for i in range(len(piezas_vivas)):
                    if piezas_vivas[i][1]==x1 and piezas_vivas[i][2]==y1:
                        PosicionValida=True
                        break
                    else:
                        pass
            else:
                pass

        elif pieza=='reina':
            if (((x1==x+1 or x1==x-1) and (y1==y+1 or y1==y-1))
                or ((x1==x+2 or x1==x-2) and (y1==y+2 or y1==y-2))
                or ((x1==x+3 or x1==x-3) and (y1==y+3 or y1==y-3))
                or ((x1==x+1 or x1==x+2 or x1==x+3 or x1==x-1 or x1==x-2 or x1==x-3)
                and y1==y)
                or ((y1==y+1 or y1==y+2 or y1==y+3 or y1==y-1 or y1==y-2 or y1==y-3)
                and x1==x)):
                for i in range(len(piezas_vivas)):
                    if piezas_vivas[i][1]==x1 and piezas_vivas[i][2]==y1:
                        PosicionValida=True
                        break
                    else:
                        pass
            else:
                pass
            
    except:
        pass
    return PosicionValida

# Actualiza el tablero a nivel logico al realizar una jugada
# @param none
# @return booleano
def Logic_Move():
	#Busquemos la pieza viva en esa posicion 
	try:
		assert(len(movimiento) == 2)
		move_from = [Logic_LetterToNumbers(movimiento[0][0]), int(movimiento[0][1])-1]
		move_to   = [Logic_LetterToNumbers(movimiento[1][0]), int(movimiento[1][1])-1]
		
		movimientos_realizados.append([move_from[0],move_from[1],move_to[0],move_to[1]])

		if Logic_LetterToNumbers(movimiento[0][0]) == -1 or Logic_LetterToNumbers(movimiento[1][0]) == -1:
			return False

		pieza_moviendo = ""
		pieza_comida = ""

		for i in range(len(piezas_vivas)):
			if piezas_vivas[i][1] == move_from[0] and piezas_vivas[i][2] == move_from[1]:
				pieza_moviendo = piezas_vivas[i][0]
				indice_moviendo = i
			
			if piezas_vivas[i][1] == move_to[0] and piezas_vivas[i][2] == move_to[1]:
				pieza_comida = piezas_vivas[i][0]
				indice_comida = i

		canMove = Logic_Position(pieza_moviendo, move_from[0], move_from[1], move_to[0], move_to[1])
		
		if canMove:
			piezas_muertas.append(piezas_vivas[indice_comida])
			piezas_vivas[indice_moviendo][1] = move_to[0]
			piezas_vivas[indice_moviendo][2] = move_to[1]
			piezas_vivas.pop(indice_comida)

			return True
		
		movimiento[1] = "" 
		return False
	except:
		return False
		
# Deshace una jugada de ser posible
# @param none
# @return void
def Logic_Undo():
	try:
		assert(len(piezas_muertas) > 0)
		if len(piezas_muertas) > 0 and nivel != 1 and nivel != 2:
		
			last_move = movimientos_realizados[len(movimientos_realizados)-1]
		
			movimientos_realizados.pop(len(movimientos_realizados)-1) 

			move_from = [last_move[0],last_move[1]]
			move_to   = [last_move[2],last_move[3]]

			for i in range(len(piezas_vivas)):
				if piezas_vivas[i][1] == move_to[0] and piezas_vivas[i][2] == move_to[1]:
					piezas_vivas[i][1] = move_from[0]
					piezas_vivas[i][2] = move_from[1]
					break

			piezas_vivas.append(piezas_muertas[len(piezas_muertas)-1])
			piezas_muertas.pop(len(piezas_muertas)-1)
	except:
		pass

# Renderiza la vista de carga manual de tablero
# @param none
# @return void
def Render_LoadManual():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(salida, (0,0))
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(i_tablero, (960/2-name_input[1]/2, logo_desc[2] + 80))
		pygame.display.flip()
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista de carga manual de tablero al ingresar datos
# @param none
# @return void
def Render_Manual():
	try:
		assert(isinstance(screen, pygame.Surface))
		Render_drawSurface(screen)
		screen.blit(salida, (0,0))
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(i_tablero, (960/2-name_input[1]/2, logo_desc[2] + 80))
		textsurface = myfont.render(tablero_manual, True, (255,255,255)) #coloca lo que hayas puesto de nombre
		screen.blit(textsurface,(960/2-name_input[1]/2 + 90, logo_desc[2] + name_input[2]//2 + 72 ))			
		pygame.display.flip() #dibuja lo que dice blit
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista de carga manual de tablero al generarse errores
# @param none
# @return void
def Render_ErrorManual(number):

	try:
		assert(number == int(number))
		Render_drawSurface(screen)
		screen.blit(salida, (0,0))
		screen.blit(logo, (960/2-logo_desc[1]//2, 40))
		screen.blit(i_tablero, (960/2-name_input[1]/2, logo_desc[2] + 80))
		textsurface = myfont.render(tablero_manual, True, (255,255,255)) #coloca lo que hayas puesto de nombre
		screen.blit(textsurface,(960/2-name_input[1]/2 + 90, logo_desc[2] + name_input[2]//2 + 72 ))			
	
		if number == 1:
			textsurface = myfont.render('Hay fichas incorrectas', True, (255,255,255))
		else:
			textsurface = myfont.render('Tablero no valido', True, (255,255,255))

		screen.blit(pygame.transform.scale(alerta_drawable, (alerta[1]//2, alerta[2]//2)), (960//2 - alerta[1]//4, tablero[2] + 30))
		screen.blit(textsurface,(960//2 - alerta[1]//4 + 50, tablero[2] + 40))	
		pygame.display.flip() #dibuja lo que dice blit
	except:
		print("Error al renderizar la pantalla")

# Renderiza la vista de los records
# @param none
# @return void
def Render_Records(records_facil, records_dificil, records_muydificil):
	try:
		assert(isinstance(records_facil,list) and isinstance(records_dificil,list) and isinstance(records_muydificil,list))
		Render_drawSurface(screen)
		screen.blit(logo, (960/2-logo_desc[1]//2, 10))
		screen.blit(drawable_rtitle, (960/2-logo_desc[1]//2+60,logo_desc[2]-20))
		#Draw titles
		screen.blit(drawable_ftitle, (20,logo_desc[2] +60))
		screen.blit(drawable_dtitle, (960/2-rcrds_facil[1]//2+40,logo_desc[2] +60))
		screen.blit(drawable_mtitle, (960 -rcrds_facil[1]//2-70,logo_desc[2] +60))
		show = 5

		normalx = 20
		normaly = logo_desc[2] + 180

		screen.blit(drawable_tools_rc , (960/2-rcrds_tools[1]//2, 670-rcrds_tools[2]//2-100))
	
		if len(records_facil) > 0 :
			nombresurface 	= myfont.render('NOMBRE', True, (255,255,255)) 
			partidassurface = myfont.render('PARTIDAS', True, (255,255,255)) 
			screen.blit(nombresurface , (normalx, normaly-30))
			screen.blit(partidassurface,(normalx + 200, normaly-30))
		else:
			partidassurface = myfont.render('VACIO', True, (255,255,255)) 
			screen.blit(partidassurface , (normalx+70, normaly-30))
		#Faciles
		for x in range (page*show, show*(1+page)):
			if x < len(records_facil):	
				nombresurface 	= myfont.render(records_facil[x][0], True, (255,255,255)) 
				partidassurface = myfont.render(str(records_facil[x][1]), True, (255,255,255)) 
				screen.blit(nombresurface , (normalx, normaly+ ((x-page*show)*20)))
				screen.blit(partidassurface,(normalx + 200, normaly+ ((x-page*show)*20)))
		
		normalx =960/2-rcrds_facil[1]//2

		if len(records_dificil) > 0:
			nombresurface 	= myfont.render('NOMBRE', True, (255,255,255)) 
			partidassurface = myfont.render('PARTIDAS', True, (255,255,255)) 
			screen.blit(nombresurface , (normalx, normaly-30))
			screen.blit(partidassurface,(normalx + 200, normaly-30))
		else:
			partidassurface = myfont.render('VACIO', True, (255,255,255)) 
			screen.blit(partidassurface , (normalx+110, normaly-30))
	
		#Dificiles
		for x in range (page*show, show*(1+page)):
			if x < len(records_dificil):	
				nombresurface 	= myfont.render(records_dificil[x][0], True, (255,255,255)) 
				partidassurface = myfont.render(str(records_dificil[x][1]), True, (255,255,255)) 
				screen.blit(nombresurface , (normalx, normaly+ ((x-page*show)*20)))
				screen.blit(partidassurface,(normalx + 200, normaly+ ((x-page*show)*20)))

		normalx = 960 -rcrds_facil[1]//2-160

		if len(records_muydificil) > 0:
			nombresurface 	= myfont.render('NOMBRE', True, (255,255,255)) 
			partidassurface = myfont.render('PARTIDAS', True, (255,255,255)) 
			screen.blit(nombresurface , (normalx, normaly-30))
			screen.blit(partidassurface,(normalx + 200, normaly-30))
		else:
			partidassurface = myfont.render('VACIO', True, (255,255,255)) 
			screen.blit(partidassurface , (normalx+160, normaly-30))

		#Muy Dificiles
		for x in range (page*show, show*(1+page)):
			if x < len(records_muydificil):	
				nombresurface 	= myfont.render(records_muydificil[x][0], True, (255,255,255)) 
				partidassurface = myfont.render(str(records_muydificil[x][1]), True, (255,255,255)) 
				screen.blit(nombresurface , (normalx, normaly+ ((x-page*show)*20)))
				screen.blit(partidassurface,(normalx + 200, normaly+ ((x-page*show)*20)))
	
		pygame.display.flip()
	
	except:
		print("Error al renderizar la pantalla")

# Clasifica y ordena los records por nivel
# @param records_facil: lista de records del nivel facil
# @param records_dificil: lista de records del nivel dificil
# @param records_muydificil: lista de records del nivel muy dificl
# return void
def Logic_Records(records_facil, records_dificil, records_muydificil):
	try:
		assert(isinstance(records_facil,list) and isinstance(records_dificil,list) and isinstance(records_muydificil,list))
		archivo_records = open(files[2],'r')
		records_nivel = archivo_records.readlines()
		archivo_records.close()
	
		del records_facil[:]
		del records_dificil[:]
		del records_muydificil[:]

		for i in range(len(records_nivel)):
			secciones = records_nivel[i].split(",")
			if len(secciones) == 3:
				if secciones[2].rstrip('\r\n') == 'FACIL':
					records_facil.append([secciones[0],int(secciones[1])])
				elif secciones[2].rstrip('\r\n') == 'DIFICIL':
					records_dificil.append([secciones[0],int(secciones[1])])
				elif secciones[2].rstrip('\r\n') == 'MUY DIFICIL':
					records_muydificil.append([secciones[0],int(secciones[1])])
		
		records_facil = sorted(records_facil, key=lambda records_facil: records_facil[1], reverse = True)
		records_dificil = sorted(records_dificil, key=lambda records_dificil: records_dificil[1], reverse = True)
		records_muydificil = sorted(records_muydificil, key=lambda records_muydificil: records_muydificil[1], reverse = True)

		for i in range(len(records_facil)):
			for j in range(len(records_facil)):
				if i < j and records_facil[i][1] == records_facil[j][1] and (j == len(records_facil)-1 or records_facil[j][1] != records_facil[j+1][1]):
					records_facil[i:j+1] = sorted(records_facil[i:j+1])

		for i in range(len(records_dificil)):
			for j in range(len(records_dificil)):
				if i < j and records_dificil[i][1] == records_dificil[j][1] and (j == len(records_dificil)-1 or records_dificil[j][1] != records_dificil[j+1][1]):
					records_dificil[i:j+1] = sorted(records_dificil[i:j+1])

		for i in range(len(records_muydificil)):
			for j in range(len(records_muydificil)):
				if i < j and records_muydificil[i][1] == records_muydificil[j][1] and (j == len(records_muydificil)-1 or records_muydificil[j][1] != records_muydificil[j+1][1]):
					records_muydificil[i:j+1] = sorted(records_muydificil[i:j+1])
	
		Render_Records(records_facil, records_dificil, records_muydificil)

	except:
		print("Error al renderizar la pantalla")

# Calcula los posibles movimientos de una pieza
# @param none
# @return void
def Logic_Solutions():
	canmove=[]
	try:
		assert(len(movimiento) == 2)
		move_from = [Logic_LetterToNumbers(movimiento[0][0]), int(movimiento[0][1])-1]

		if Logic_LetterToNumbers(movimiento[0][0]) == -1:
			return -1


		#Lets find the piece in this place
		for k in range(len(piezas_vivas)):
			if piezas_vivas[k][1] == move_from[0] and piezas_vivas[k][2] == move_from[1]:
				move_from.append(piezas_vivas[k][0])
				break
		
		for p in range(len(piezas_vivas)):
			if piezas_vivas[p][1] != move_from[0] or piezas_vivas[p][2] != move_from[1]:
				move_to = [int(piezas_vivas[p][1]), int(piezas_vivas[p][2])]
				if Logic_Position(move_from[2], move_from[0], move_from[1], move_to[0], move_to[1]):
					created = [move_from[2],int(piezas_vivas[p][1]), int(piezas_vivas[p][2])]
					canmove.append(created)

		return canmove
	except:
		return -1

# Loop principal del juego
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN: #keydown, es la accion de apretar una tecla
			if pantalla == 'principal': 
				if str(pygame.key.name(event.key)) in (letters + numbers):
					nombrejugador += str(pygame.key.name(event.key))
					Render_Input('principal')
				elif event.key == pygame.K_BACKSPACE: #k_backspace, es la accion de borrar
					if len(nombrejugador) > 0:
						nombrejugador = nombrejugador[:-1]
						Render_Input('principal')
				elif event.key == pygame.K_RETURN: #k_return, es enter
					if len(nombrejugador) == 0:
						Render_ErrorInput(0)
					else:
						pantalla = 'menu_principal'
						Render_Screen()
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
			elif pantalla == 'menu_principal':
				if str(pygame.key.name(event.key)) in ['1','2','3','4']:
					if event.key == pygame.K_1:
						pantalla = 'menu_jugar'
						Render_Level()
					elif event.key == pygame.K_2:
						pantalla = 'menu_cargar'
						Render_Input('carga')
					elif event.key == pygame.K_3:
						pantalla = 'records'
						Logic_Records(records_facil, records_dificil, records_muydificil)
					elif event.key == pygame.K_4:
						sys.exit()
				elif event.key == pygame.K_ESCAPE:
					pantalla = 'principal'
					Render_Input('principal')
				else:
					Render_ErrorInput(1)
			elif pantalla == 'records':
				if event.key == pygame.K_ESCAPE:
					pantalla = 'menu_principal'
					Render_Screen()
				elif event.key == pygame.K_UP:
					if page > 0:
						page -= 1
					Logic_Records(records_facil, records_dificil, records_muydificil)
				elif event.key == pygame.K_DOWN:
					page += 1
					Logic_Records(records_facil, records_dificil, records_muydificil)

			elif pantalla == 'menu_jugar':
				if str(pygame.key.name(event.key)) in ['1','2','3','4']:
					if event.key == pygame.K_1:
						pantalla = 'menu_facil'
						nivel = 0
						Render_Mode()
					elif event.key == pygame.K_2:
						pantalla = 'menu_dificil'
						nivel = 1
						Render_Mode()
					elif event.key == pygame.K_3:
						pantalla = 'muydificil'
						nivel = 2
						partidastring = Logic_GenerateLevel(nivel)
						toplay.pop(0)
						if partidastring != -1:
							seconds = 0
							if Logic_Board(partidastring) != -1:
								pantalla = 'jugar'
								piezas_vivas = Logic_Board(partidastring)
								Render_Board()
							else:
								pantalla = 'menu_principal'
								Render_ErrorInput(4)
						else:
							pantalla = 'menu_principal'
							Render_ErrorInput(4)
					elif event.key == pygame.K_4:
						pantalla = 'menu_entrenamiento'
						nivel = 3
						Render_Mode()
				elif event.key == pygame.K_ESCAPE:
					pantalla = 'menu_principal'
					Render_Screen()
				else:
					Render_ErrorInput(1)
			
			elif pantalla == 'menu_cargar':
				if str(pygame.key.name(event.key)) in numbers:
					numero_partida += str(pygame.key.name(event.key))
					Render_Input('carga')
				elif event.key == pygame.K_BACKSPACE: #k_backspace, es la accion de borrar
					if len(numero_partida) > 0:
						numero_partida = numero_partida[:-1]
						Render_Input('carga')
				elif event.key == pygame.K_RETURN: #k_return, es enter
					if len(numero_partida) == 0:
						Render_ErrorInput(2)
					else:
						seconds, nivel, piezas_vivas, movimientos_realizados, piezas_muertas, exists = Logic_LoadLevel()
						if exists:
							pantalla = 'jugar'
							Render_Board()
						else:
							Render_ErrorInput(3)

				elif event.key == pygame.K_ESCAPE:
						pantalla = 'menu_principal'
						Render_Screen()

			elif pantalla == 'menu_facil' or pantalla == 'menu_dificil' or pantalla == 'menu_entrenamiento':
				if str(pygame.key.name(event.key)) in ['1','2']:
					if event.key == pygame.K_1: #juego al azar
						partidastring = Logic_GenerateLevel(nivel)
						if partidastring != -1:
							seconds = 0
							if Logic_Board(partidastring) != -1:
								pantalla = 'jugar'
								piezas_vivas = Logic_Board(partidastring)
								Render_Board()
							else:
								Render_ErrorMode("Hubo un error al generar el tablero")
						else:
							Render_ErrorMode("No se encontraron partidas para este nivel")
					elif event.key == pygame.K_2: #Cargar por teclado
						pantalla = 'load_manual'
						Render_LoadManual()

				elif event.key == pygame.K_ESCAPE:
					pantalla = 'menu_jugar'
					Render_Level()
				else:
					Render_ErrorInput(1)
			elif pantalla == 'jugar':
				if event.key == pygame.K_1:
					pantalla = 'jugando_inicial'
					Render_Move(0)
				elif event.key == pygame.K_2:
					if nivel != 2:
						pantalla = 'pausado'
						Render_Stop()
					elif nivel == 2:
						Render_ErrorPlaying(3)
				elif event.key == pygame.K_3:
					if nivel == 0 or nivel == 3:
						if len(piezas_muertas)==0:
							Render_ErrorPlaying(2)
						else:	
							Logic_Undo()
							Render_Board()
					elif nivel == 2 or nivel == 1:
						Render_ErrorPlaying(2)
				elif event.key == pygame.K_4:
					if nivel != 3:
						pantalla = 'terminando'
						Render_Finish()
					else:
						pantalla = 'menu_principal'
						Render_Screen()

			elif pantalla == 'jugando_inicial':
				if str(pygame.key.name(event.key)) in (['1','2','3','4'] + ["a", "b", "c", "d"]):
					if len(movimiento[0]) < 2:
						movimiento[0] += str(pygame.key.name(event.key))
						Render_Move(0)
				
				elif event.key == pygame.K_BACKSPACE: #k_backspace, es la accion de borrar
					if len(movimiento[0]) > 0:
						movimiento[0] = movimiento[0][:-1]
						Render_Move(0)

				elif event.key == pygame.K_RETURN: #k_return, es enter
					if len(movimiento[0]) < 2 :
						Render_ErrorPlaying(0)
					else:
						if nivel == 3:
							solutions = Logic_Solutions()
							if solutions == -1:
								Render_ErrorPlaying(0)
							elif len(solutions) == 0:
								Render_Move(2)
							else:
								pantalla = 'jugando_final'
								Render_Solutions(solutions)
						else:
							pantalla = 'jugando_final'
							Render_Move(1)
							
				elif event.key == pygame.K_ESCAPE:
					pantalla = 'jugar'
					movimiento[0] = ""
					movimiento[1] = ""
					Render_Board()
			
			elif pantalla == 'jugando_final':
				if str(pygame.key.name(event.key)) in (['1','2','3','4'] + ["a", "b", "c", "d"]):
					if len(movimiento[1]) < 2:
						movimiento[1] += str(pygame.key.name(event.key))
						Render_Move(1)
				
				elif event.key == pygame.K_BACKSPACE: #k_backspace, es la accion de borrar
					if len(movimiento[1]) > 0:
						movimiento[1] = movimiento[1][:-1]
						Render_Move(1)
					else:
						Render_Move(0)
						pantalla = 'jugando_inicial'

				elif event.key == pygame.K_RETURN: #k_return, es enter
					if len(movimiento[1]) < 2 :
						Render_ErrorPlaying(1)
					else:
						pantalla = 'haciendo_jugada'
						if Logic_Move():
							pantalla = 'jugar'
							movimiento[0] = ""
							movimiento[1] = ""
							status = Logic_Validate()
							
							if status == 1:

								if nivel == 2 and len(toplay) > 0:
									partidastring = toplay[0]
									toplay.pop(0)
									if partidastring != -1:
										if Logic_Board(partidastring) != -1:
											pantalla = 'jugar'
											piezas_vivas = Logic_Board(partidastring)
											Render_Board()
										else:
											pantalla = 'menu_principal'
											Render_ErrorInput(4)
									else:
										pantalla = 'menu_principal'
										Render_ErrorInput(4)
								else:			
									pantalla = "finalizado"
									Render_EndGame(1)
									r = open(files[2],'r')
									archivo_ganadores = r.readlines()
									r.close()
									R = open(files[2],'w')
									agregado = False
									for i in range(len(archivo_ganadores)):
											secciones = archivo_ganadores[i].split(",")
											
											if len(secciones) != 3:
												pass

											if secciones[0] == nombrejugador and secciones[2].rstrip('\r\n') == Logic_LevelToString():
												agregado = True
												secciones[1] = str(int(secciones[1])+1)

											R.write(secciones[0]+','+secciones[1]+','+secciones[2])
									
									if not agregado:
										if len(archivo_ganadores) == 0:
											R.write(nombrejugador+','+'1'+','+Logic_LevelToString())
										else:
											R.write('\r\n'+nombrejugador+','+'1'+','+Logic_LevelToString())

									R.close()
								
							elif status == 2:
								pantalla = "finalizado"
								Render_EndGame(2)	
							else:
								Render_Board()
						else:
							pantalla = 'jugando_final'
							Render_ErrorPlaying(1)

				elif event.key == pygame.K_ESCAPE:
					pantalla = 'jugar'
					movimiento[0] = ""
					movimiento[1] = ""
					Render_Board()

			elif pantalla == 'terminando':
				if event.key == pygame.K_1:
					G = open(files[1],'r')
					archivo_guardado = G.readlines()
					num_partida = str(len(archivo_guardado)+1)
					G.close()

					partidas_guardadas = open(files[1],'w')
					for i in range(len(archivo_guardado)):
						partidas_guardadas.write(archivo_guardado[i])

					partidas_guardadas.write('\r\n'+nombrejugador+'-'+num_partida+'-'+str(seconds)+'-'+str(nivel)+'-'+str(piezas_vivas)+'-'+str(movimientos_realizados)+'-'+str(piezas_muertas))
					partidas_guardadas.close()
					
					pantalla = 'partida_guardada'
					Render_Game(num_partida)

				elif event.key == pygame.K_2:
					pantalla = 'menu_principal'
					Render_Screen()
				
				else:
					Render_ErrorMode('Opcion invalida')
			
			elif pantalla == 'finalizado' or pantalla == 'partida_guardada':
				tablero_original 		= []
				piezas_muertas 			= []
				piezas_vivas 			= []
				movimientos_realizados 	= []
				tablero_manual          = ''
				numero_partida          = ''
				pantalla = 'menu_principal'
				Render_Screen()
			
			elif pantalla == 'pausado':
				pantalla = 'jugar'
				Render_Board()

			elif pantalla == 'load_manual':
				if str(event.unicode) in (['1','2','3','4'] + ["a", "b", "c", "d", "-", "r", "t"]):
					tablero_manual += str(event.unicode)
					Render_Manual()
				
				elif event.key == pygame.K_BACKSPACE: #k_backspace, es la accion de borrar
					if len(tablero_manual) > 0:
						tablero_manual = tablero_manual[:-1]
						Render_Manual()
					
				elif event.key == pygame.K_ESCAPE:
					pantalla = 'menu_jugar'
					Render_Level()
				
				elif event.key == pygame.K_RETURN: #k_return, es enter
					if len(tablero_manual) > 0:
						
						if Logic_Board(tablero_manual) != -1:
							piezas_vivas = Logic_Board(tablero_manual)
							status = Logic_Validate()
							if status == 2:
								Render_ErrorManual(2)
							else:
								seconds = 0
								pantalla = 'jugar'
								Render_Board()
						else:
							Render_ErrorManual(1)

				
		elif event.type == pygame.USEREVENT + 1:
			if pantalla == 'terminando' or pantalla == 'pausado' or nivel == 3:
				pass
			elif pantalla == 'jugando_inicial' or pantalla == 'jugando_final' or pantalla == 'jugar':
				seconds+=1
				Render_Time()
				if Logic_Lost():
					pantalla = "finalizado"
					Render_EndGame(2)