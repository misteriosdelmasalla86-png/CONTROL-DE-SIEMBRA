#!/usr/bin/env python3
"""
Script simplificado para entrenar YOLOv5 con datos locales
"""

import os
import sys
from pathlib import Path

# Cambiar al directorio de yolov5
os.chdir('/workspaces/CONTROL-DE-SIEMBRA/yolov5')

print("=" * 80)
print("🌱 ENTRENAMIENTO YOLOV5 - CONTROL DE SIEMBRA")
print("=" * 80)
print()

# Verificar que existan los datos
data_yaml = Path('data.yaml')
train_imgs = Path('../datasets-yolo/images/train')
val_imgs = Path('../datasets-yolo/images/val')

print("📋 Verificando datos...")
print(f"  ✓ data.yaml existe: {data_yaml.exists()}")
print(f"  ✓ Imágenes train: {len(list(train_imgs.glob('*')))} archivos")
print(f"  ✓ Imágenes val: {len(list(val_imgs.glob('*')))} archivos")
print()

# Importar train desde YOLOv5
print("🔧 Importando YOLOv5...")
try:
    from train import main
    print("✓ YOLOv5 importado correctamente")
except ImportError as e:
    print(f"✗ Error al importar: {e}")
    print("\nIntentando ejecutar train.py directamente...")
    os.system('python train.py --img 640 --batch 8 --epochs 2 --data data.yaml --weights yolov5s.pt --name semillas-argentinas --device cpu --exist-ok')
    sys.exit(0)

print()
print("🚀 Iniciando entrenamiento...")
print("-" * 80)

# Ejecutar entrenamiento
sys.argv = [
    'train.py',
    '--img', '640',
    '--batch', '8',
    '--epochs', '2',
    '--data', 'data.yaml',
    '--weights', 'yolov5s.pt',
    '--name', 'semillas-argentinas',
    '--device', 'cpu',
    '--exist-ok'
]

try:
    main()
except Exception as e:
    print(f"\n❌ Error durante entrenamiento: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("-" * 80)
print("✅ Entrenamiento completado!")
print()
print("📁 Resultados en: /workspaces/CONTROL-DE-SIEMBRA/yolov5/runs/detect/semillas-argentinas/")
print()
