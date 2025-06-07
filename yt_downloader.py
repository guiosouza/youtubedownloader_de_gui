#!/usr/bin/env python3
"""
youtube_downloader.py

Script para baixar vídeos do YouTube (incluindo shorts) usando a biblioteca yt-dlp.

Dependências:
    pip install yt-dlp

Exemplo de uso:
    python youtube_downloader.py
"""
import sys
from yt_dlp import YoutubeDL

def download_videos(urls, output_path, format_str, audio_only=False):
    """
    Faz o download dos vídeos ou shorts fornecidos.

    Args:
        urls (list of str): URLs dos vídeos a serem baixados.
        output_path (str): Diretório de saída para os downloads.
        format_str (str): String de formato para qualidade/formato do vídeo.
        audio_only (bool): Se True, baixa apenas o áudio em M4A.
    """
    ydl_opts = {
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",
        'format': format_str,
        'noplaylist': True,
        'quiet': False,
        'no_warnings': True,
    }
    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        })

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def main():
    print("===== YouTube Downloader =====")
    url = input("Informe a URL do vídeo ou short do YouTube: ").strip()
    if not url:
        print("Erro: Nenhuma URL fornecida.")
        sys.exit(1)

    print("\nEscolha a qualidade do vídeo:")
    print("1. Melhor qualidade disponível")
    print("2. Qualidade até 720p")
    print("3. Somente áudio (M4A)")

    choice = input("Digite o número da opção desejada [1-3]: ").strip()

    if choice == '1':
        format_str = 'best'
        audio_only = False
    elif choice == '2':
        format_str = '[height<=720]'
        audio_only = False
    elif choice == '3':
        format_str = 'bestaudio'
        audio_only = True
    else:
        print("Opção inválida.")
        sys.exit(1)

    try:
        download_videos([url], '.', format_str, audio_only)
    except Exception as e:
        print(f'Falha no download: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
