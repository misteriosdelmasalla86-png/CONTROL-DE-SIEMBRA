#!/bin/bash
# Script para entrenar YOLOv5 con los datos de siembra

cd /workspaces/CONTROL-DE-SIEMBRA/yolov5

echo "🚀 Iniciando entrenamiento de YOLOv5..."
echo "📊 Datos: data.yaml"
echo "🖼️  Modelo: YOLOv5s (pequeño, rápido)"
echo ""

# Entrenamiento
python train.py \
  --img 640 \
  --batch 16 \
  --epochs 10 \
  --data data.yaml \
  --weights yolov5s.pt \
  --device 0 \
  --name siembra-v1 \
  --exist-ok \
  --patience 5

echo ""
echo "✅ Entrenamiento completado"
echo "📁 Resultados en: runs/detect/siembra-v1"
