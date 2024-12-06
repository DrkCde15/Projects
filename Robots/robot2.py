import os
import yt_dlp

# Função para baixar o vídeo do YouTube usando yt-dlp
def baixar_video(url):
    # Definir as opções para o yt-dlp
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': r'C:\Users\Júlio César\Videos\Captures\video.mp4'  # Caminho completo para salvar o vídeo
    }
    
    # Baixar o vídeo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Vídeo baixado com sucesso!")

# Função principal para executar o processo de baixar o vídeo
def processar_url(url):
    try:
        baixar_video(url)
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

# Exemplo de uso
url_video = input("Digite a URL do vídeo do YouTube: ")
processar_url(url_video)