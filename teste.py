#importar as libs
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import keys

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#Instanciar Chatbot

chatbot = ChatBot("Ananda")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")
trainerer = ListTrainer(chatbot)

#armazenar dirretorio principal em variavel
dir_pach = os.getcwd()

#iniciar aplicação
driver = webdriver.Chrome(dir_pach+'chromedrive.exe')
driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(15)

#Funções básicas de comunicação
def pegaConversa():
  try:
    ...
  except:
    ...

def enviaMensagem(mensagem):
  ...

def treinar(mensagem):

  ...