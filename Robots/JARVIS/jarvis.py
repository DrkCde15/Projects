import pyttsx3

engine = pyttsx3.init()

# Lista todas as vozes disponíveis
voices = engine.getProperty('voices')

# Tenta encontrar uma voz masculina em português
selected_voice = None
for voice in voices:
    if "pt" in voice.id.lower() and ("male" in voice.name.lower() or "masculina" in voice.name.lower()):
        selected_voice = voice
        break

# Se não encontrar uma masculina, usa a primeira voz pt disponível
if not selected_voice:
    for voice in voices:
        if "pt" in voice.id.lower():
            selected_voice = voice
            break

# Se ainda não encontrou, usa a voz padrão
if selected_voice:
    engine.setProperty('voice', selected_voice.id)

# Fala a saudação
engine.say("Olá Sr., meu nome é JARVIS, bem-vindo ao seu sistema.")
engine.runAndWait()
