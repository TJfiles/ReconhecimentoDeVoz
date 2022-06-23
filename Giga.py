import speech_recognition as sr
from playsound import playsound
import webbrowser
import subprocess
import os
import pywhatkit
import keyboard
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from worker import Worker
from PyQt5 import QtCore

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 971
        self.altura = 630
        self.titulo = 'Giga Assistente Virtual'
        self.threadpool = QtCore.QThreadPool()

        self.imagem = QLabel(self)
        self.imagem.move(1,1)
        self.imagem.resize(971,630)
        self.imagem.setPixmap(QtGui.QPixmap('Giga.png'))

        self.botao_parar = QPushButton('Encerrar Programa', self)
        self.botao_parar.move(410, 570)
        self.botao_parar.resize(150, 30)
        self.botao_parar.setStyleSheet('QPushButton {font:bold; font-size: 10px; background-color: gray}')
        self.botao_parar.clicked.connect(self.parar)



        self.carregar_janela()


    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def parar(self):
        print('Encerrando programa')
        exit(1)

    def giga(self):
        listener = sr.Recognizer()
        playsound('saudacao.mp3')

        contatos = ('américo', '+5511994975277', 'pai', '+5511973359284', 'amor', '+5511958043341', 'júnior', '+5511951188170')

        def mostrar_contatos():
            print('{:-^45}'.format('LISTA DE CONTATOS'))
            for cont, contato in enumerate(contatos):
                if cont % 2 == 0:
                    print('{:.<30}'.format(contato.capitalize()), end='')
                else:
                    print('{}'.format(contato))
            print('{:-^45}'.format('-'))

        def escutar():
            listener = sr.Recognizer()
            while True:
                try:
                    with sr.Microphone() as source:
                        print('Escutando...')
                        audio = listener.listen(source)
                        texto = listener.recognize_google(audio, language='pt-BR')
                        texto = texto.lower()
                        return texto
                except:
                    pass

        def mandar_mensagem():
            while True:
                try:
                    mostrar_contatos()
                    playsound('contatos.mp3')
                    print('Diga o nome do contato.')
                    contato = escutar()
                    posicao = contatos.index(contato)
                    numero = posicao + 1
                    numero = contatos[numero]
                    print('Agora diga a mensagem.')
                    playsound('mensagem.mp3')
                    mensagem = escutar()
                    print(f'CONTATO:{contato}\nNúmero:{numero}\nTEXTO DA MENSAGEM:{mensagem}')
                    hora = datetime.now().hour
                    minuto = datetime.now().minute
                    playsound('mensagemenviada.mp3')
                    pywhatkit.sendwhatmsg(numero, mensagem, hora, minuto + 1.30)
                    print('Sua mensagem sera enviada em breve...')
                    break
                except: