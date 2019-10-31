from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Ananda")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")

while True:
  try:
      bot_input = chatbot.get_response(input())
      print(bot_input)
  except:
    print("Algo deu errado... Tchau!")