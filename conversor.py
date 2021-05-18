# Conversor de vídeos de vários formatos para                        |
# audios em MP3                                                      |
# -------------------------------------------                        |
# Esse código faz parte do meu programa E-tube                       |    \ 
# Mas estou trazendo ele aqui porque talvez vocês                           # Autor: lucas-Dk  |  WhatsApp: +5531986802198
# Queiram apenas o conversor. Mas o mesmo código aqui                |    /
# Se encontra dento do E-tube, meu programa!                         |
# ---------------------------------------------------                |
# Facebok: https://www.facebook.com/Walker.Lxrd/                     | 

try:
	import os
	import sys
	import re
	import datetime
	import moviepy.editor as mp
	from time import sleep as suspender
	from time import strftime
except:
	print("\033[1;32m[!] Comando: python3 setup.py\033[m")
else:

	def validar_caminho(caminho):
		valid = re.search(r"^(?=\\([a-zA-Z0-9_\-\\\s]*)(\\)$)",caminho)
		return valid

	while True:
		os.system("clear")
		print("""\033[1;36m                     
 _______  _______  __    _  __   __  _______  ______    _______  _______  ______   
|       ||       ||  |  | ||  | |  ||       ||    _ |  |       ||       ||    _ |  
|       ||   _   ||   |_| ||  |_|  ||    ___||   | ||  |  _____||   _   ||   | ||  
|       ||  | |  ||       ||       ||   |___ |   |_||_ | |_____ |  | |  ||   |_||_ 
|      _||  |_|  ||  _    ||       ||    ___||    __  ||_____  ||  |_|  ||    __  |
|     |_ |       || | |   | |     | |   |___ |   |  | | _____| ||       ||   |  | |
|_______||_______||_|  |__|  |___|  |_______||___|  |_||_______||_______||___|  |_|\033[m\033[1;31m
			                _____ 
			 _ __ ___  _ __|___ / 
			| '_ ` _ \| '_ \ |_ \ 
			| | | | | | |_) |__) |
			|_| |_| |_| .__/____/ 
			          |_|         
			\033[m""")

		caminho_videos = str(input("\033[1;32m[+] Informe o caminho onde está(ão) o(s) vídeo(s):\033[m ")).strip()
		while not validar_caminho(caminho=caminho_videos):
			print("\033[1;31m[!] Coloque uma contra barra -> \\ no final do caminho!\033[m")
			caminho_videos = str(input("\033[1;32m[+] Informe o caminho onde está(ão) o(s) vídeo(s):\033[m ")).strip()
		extensao_file = str(input("\033[1;32m[+] Informe qual é a extensão do arquivo [.mp4/.webm/.wmv ...]:\033[m ")).strip().lower()
		while "." not in extensao_file:
			print("\033[1;31m[+] Coloque um . antes da estensão do arquivo!\033[m")
			extensao_file = str(input("\033[1;32m[+] Informe qual é a extensão do arquivo [.mp4/.webm/.wmv ...]:\033[m ")).strip().lower()
		start = datetime.datetime.now()
		starttime = strftime("%H:%M:%S")
		print("\n\033[1;36m[*] Conversão iniciada as:\033[m {}\n".format(starttime))
		for videos in os.listdir(str(caminho_videos)):
			if videos.endswith(str(extensao_file)):
				seuarquivo = videos
				fdownloads = caminho_videos + seuarquivo
				ldownloads = videos.replace(extensao_file,".mp3")
				wdownloads = mp.VideoFileClip(fdownloads)
				wdownloads.audio.write_audiofile(ldownloads)
		finish = datetime.datetime.now() - start
		finish2 = str(finish)
		print("\n\033[1;32m[*] Conversão finalizada!\033[m")
		print("\033[1;34m[+] Tempo que o programa levou para converter:\033[m {}\n".format(finish2[0:7]))
		print("\033[1;34m[+] Local de armazenamento:\033[m Mesmo local onde o script está!")
		voltar = input("\n\033[1;32m[+] Aperte \033[m\033[1;36mENTER\033[m\033[1;32m para sair ou \033[m\033[1;36mV\033[m\033[1;32m para converter outro(a) vídeo/playlist:\033[m ").upper()
		while voltar not in "V":
			voltar = input("\033[1;32m[+] Aperte \033[m\033[1;36mENTER\033[m\033[1;32m para sair ou \033[m\033[1;36mV\033[m\033[1;32m para converter outro(a) vídeo/playlist:\033[m ").upper()
		if voltar == "V":
			os.system("clear")
		elif voltar == "":
			print("\033[m[*] Programa encerrado as {}".format(starttime))
			sys.exit()
