import os, shutil, json, logging
from pathlib import Path

# === LOGGING ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# === CONFIGURACIÓN ===
DATASETS_DIR = "/workspaces/CONTROL-DE-SIEMBRA/datasets-argentina"
YOLO_DIR = "/workspaces/CONTROL-DE-SIEMBRA/datasets-yolo"
DATASETS = {
    "maiz": f"{DATASETS_DIR}/MaizeSeedlingDetectionDataset",
    "soja": f"{DATASETS_DIR}/digital-agriculture-datasets"
}

# === FUNCIÓN: CONVERTIR MSDD (maíz) ===
def convertir_msdd():
    try:
        src_img = Path(DATASETS["maiz"]) / "images"
        src_lbl = Path(DATASETS["maiz"]) / "labels"
        
        if not src_img.exists():
            raise FileNotFoundError(f"No existe: {src_img}")
        
        # Crear carpetas YOLO
        (Path(YOLO_DIR) / "images" / "train").mkdir(parents=True, exist_ok=True)
        (Path(YOLO_DIR) / "labels" / "train").mkdir(parents=True, exist_ok=True)
        
        # Copiar imágenes (múltiples formatos)
        img_copiadas = 0
        for ext in ["*.jpg", "*.jpeg", "*.png", "*.ppm"]:
            for img in src_img.glob(ext):
                shutil.copy(img, Path(YOLO_DIR) / "images" / "train" / img.name)
                img_copiadas += 1
        
        # Copiar etiquetas
        lbl_copiadas = 0
        for lbl in src_lbl.glob("*.txt"):
            shutil.copy(lbl, Path(YOLO_DIR) / "labels" / "train" / lbl.name)
            lbl_copiadas += 1
            
        logging.info(f"✅ MSDD: {img_copiadas} imágenes, {lbl_copiadas} etiquetas")
        
    except Exception as e:
        logging.error(f"❌ Error en MSDD: {e}")

# === FUNCIÓN: CONVERTIR ROSARIO (soja) ===
def convertir_rosario():
    try:
        src = Path(DATASETS["soja"])
        src_imgs = src / "images"
        
        if not src_imgs.exists():
            raise FileNotFoundError(f"No existe: {src_imgs}")
        
        # Crear carpetas YOLO
        (Path(YOLO_DIR) / "images" / "val").mkdir(parents=True, exist_ok=True)
        (Path(YOLO_DIR) / "labels" / "val").mkdir(parents=True, exist_ok=True)
        
        # Buscar imágenes (múltiples formatos)
        imgs = []
        for ext in ["*.jpg", "*.jpeg", "*.png", "*.ppm"]:
            imgs.extend(src_imgs.glob(ext))
        
        img_procesadas = 0
        
        for i, img in enumerate(imgs[:50]):  # primeras 50 como validación
            new_name = f"rosario_{i:03d}.jpg"
            shutil.copy(img, Path(YOLO_DIR) / "images" / "val" / new_name)
            
            # Crear etiqueta dummy (centro de imagen)
            lbl_path = Path(YOLO_DIR) / "labels" / "val" / f"rosario_{i:03d}.txt"
            lbl_path.write_text("0 0.5 0.5 0.1 0.1\n")  # centrado, 10% de imagen
            img_procesadas += 1
            
        logging.info(f"✅ Rosario: {img_procesadas} imágenes procesadas")
        
    except Exception as e:
        logging.error(f"❌ Error en Rosario: {e}")

# === EJECUCIÓN ===
if __name__ == "__main__":
    logging.info("🔧 Iniciando conversión a YOLO...")
    convertir_msdd()
    convertir_rosario()
    logging.info("✅ Conversión completada!")
    logging.info(f"📁 Archivos YOLO en: {YOLO_DIR}")
