# 🌱 Control de Siembra - Guía de Entrenamiento YOLOv5

## ✅ Completado

1. **Conversión de datasets a formato YOLO**
   - Script: `convertir-a-yolo.py`
   - Convierte datasets de maíz y soja al formato YOLO
   - Crea carpetas: `datasets-yolo/images/train` y `datasets-yolo/images/val`

2. **Instalación de YOLOv5**
   - Repositorio clonado: `/workspaces/CONTROL-DE-SIEMBRA/yolov5`
   - Archivo de configuración: `yolov5/data.yaml`

3. **Estructura de datos lista**
   ```
   datasets-yolo/
   ├── images/
   │   ├── train/  (10 imágenes)
   │   └── val/    (15 imágenes)
   └── labels/
       ├── train/  (10 etiquetas)
       └── val/    (15 etiquetas)
   ```

## 🚀 Próximos pasos

### Opción 1: Entrenamiento rápido (recomendado para pruebas)
```bash
cd /workspaces/CONTROL-DE-SIEMBRA/yolov5
python train.py \
  --img 640 \
  --batch 8 \
  --epochs 5 \
  --data data.yaml \
  --weights yolov5s.pt \
  --name semillas-argentinas \
  --device cpu
```

### Opción 2: Entrenamiento con GPU (si disponible)
```bash
python train.py \
  --img 640 \
  --batch 16 \
  --epochs 10 \
  --data data.yaml \
  --weights yolov5s.pt \
  --name semillas-argentinas \
  --device 0
```

## 📊 Archivos importantes

- `convertir-a-yolo.py` - Convierte datasets a YOLO
- `yolov5/data.yaml` - Configuración de datos
- `yolov5/train.py` - Script de entrenamiento
- `yolov5/detect.py` - Script de detección

## 📈 Monitoreo

Después del entrenamiento, los resultados estarán en:
```
yolov5/runs/detect/semillas-argentinas/
├── weights/
│   ├── best.pt
│   └── last.pt
├── results.csv
└── plots/
```

## 🔧 Troubleshooting

Si falta algún módulo:
```bash
pip install -r yolov5/requirements.txt
```

---
**Última actualización:** 2025-11-15
