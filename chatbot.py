import json
import sys
import os
import subprocess as sp

class Maria():
    def __init__(self, name):
        try:
            memory = open(name+'.json', 'r')
        except FileNotFoundError:
            memory = open(name+'.json', 'w')
            memory.write("""
                            [
                                ["Maria"],
                                {
                                    "oi": "Olá! Qual seu nome?",
                                    "tchau": "Tchau! Tchau!",
                                    "como você está?": "Estou bem!!",
                                    "qual a sua idade?": "Tenho 20 anos"
                                }
                            ]
                        """)
            memory.close()
            memory = open(name+'.json', 'r')
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]
    
    def listen(self, phrase=None):
        return phrase.lower()

    def think(self, phrase):
        if 'abre o link ' in phrase:
            platform = sys.platform
            link = phrase.replace('abre o link ', '')
            if 'win' in platform:
                os.startfile(link)
            if 'linux' in platform:
                try:
                    sp.Popen(link)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', link])
            return "pera pera abrindo ..."
            
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == 'aprende':
            return 'O que você quer que eu aprenda?'
        if phrase == 'python':
            return "https://www.python.org/"
        
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response
        if lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'
        if lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'

    def getName(self, name):
        if 'meu nome é ' in name:
            name = name[12:]
        name = name.title()
        return name

    def answerName(self, name):
        if name in self.known:
            if name != 'Maria':
                phrase = 'Migaaa do céu, '
            else:
                phrase = 'Somos todas Marias....adorei! minha chará, '
        else:
            phrase = 'Muito prazer, eu sou a Maria, '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'

    def saveMemory(self):
        memory = open(self.name+'.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()

    def speak(self, phrase):
        self.historic.append(phrase)