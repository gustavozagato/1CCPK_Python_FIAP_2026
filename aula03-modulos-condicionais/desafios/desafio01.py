from playsound import playsound

# Substitua 'caminho/do/seu/arquivo.mp3' pelo local real do seu arquivo
try:
    print("Reproduzindo áudio...")
    playsound('e-o-pix-nada-ainda.mp3')
    print("Reprodução finalizada.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
