#!/usr/bin/env bash
# Incrusta subtítulos estilo Reels en un video de HeyGen.
# Uso: ./subtitular.sh entrada.mp4 subtitulos.srt salida.mp4
set -euo pipefail
ffmpeg -y -hide_banner -loglevel error -i "$1" \
  -vf "subtitles=$2:force_style='FontName=Noto Sans,Bold=1,FontSize=13,PrimaryColour=&H00FFFFFF,OutlineColour=&H00281610,BorderStyle=1,Outline=2.2,Shadow=0,Alignment=2,MarginV=105,MarginL=22,MarginR=22'" \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$3"
