# 🎥 YouTube Downloader (com suporte a Shorts)

Este é um script em Python que permite baixar vídeos do YouTube — incluindo vídeos do tipo *Shorts* — com opções de qualidade e suporte para download de apenas áudio.

---

## 📦 Requisitos

* Python 3.7 ou superior
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* (Opcional, mas recomendado) [FFmpeg](https://ffmpeg.org/) para unir vídeo + áudio em alta qualidade

### 🔧 Instalação

1. **Clone este repositório ou baixe o script**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale a biblioteca necessária**

   ```bash
   pip install yt-dlp
   ```

3. **(Opcional) Instale o FFmpeg**
   Para baixar vídeos em resoluções maiores (como 1080p+), o FFmpeg é necessário.

   * [Guia de instalação para Windows](https://www.gyan.dev/ffmpeg/builds/)
   * No Linux:

     ```bash
     sudo apt install ffmpeg
     ```
   * No Mac (usando Homebrew):

     ```bash
     brew install ffmpeg
     ```

---

## ▶️ Como usar

Execute o script com:

```bash
python youtube_downloader.py
```

Você verá um menu interativo como este:

```
===== YouTube Downloader =====
Informe a URL do vídeo ou short do YouTube: https://youtube.com/watch?v=abc123

Escolha a qualidade do vídeo:
1. Melhor qualidade disponível
2. Qualidade até 720p
3. Somente áudio (M4A)
Digite o número da opção desejada [1-3]:
```

---

## 💡 Exemplos

* Baixar um vídeo na melhor qualidade:

  ```
  https://www.youtube.com/watch?v=abcdefgh
  Opção: 1
  ```

* Baixar um YouTube Short em 720p:

  ```
  https://youtube.com/shorts/xyz123
  Opção: 2
  ```

* Baixar apenas o áudio (formato .m4a):

  ```
  https://youtu.be/abcd
  Opção: 3
  ```

---

## 📁 Saída

Os arquivos baixados serão salvos na mesma pasta onde o script for executado, com o nome do vídeo.

---

## 🛠️ Personalização

Se quiser adaptar o comportamento (como salvar em outra pasta, baixar playlists ou múltiplos links), sinta-se à vontade para modificar o código.

---

## 📄 Licença

Este projeto é de código aberto sob a licença MIT.
