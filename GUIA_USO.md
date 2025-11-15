# 🌱 CONTROL DE SIEMBRA - Guía de Uso

## Descripción General

**Siembra Precisa** es una herramienta web basada en metodología INTA para evaluar la uniformidad de siembra de cultivos. Utiliza visión por computadora (YOLOv5) para detectar y analizar semillas en campo.

## 🚀 Acceso a la Herramienta

### Opción 1: Servidor Local
```bash
cd /workspaces/CONTROL-DE-SIEMBRA
python3 -m http.server 9000
```

Luego abre en tu navegador:
```
http://localhost:9000/index.html
```

### Opción 2: Archivo Directo
Abre directamente el archivo `index.html` en tu navegador.

---

## 📋 Funcionalidades

### 1. **Modo Campo (Verificación Rápida)**
- **Entrada de datos:**
  - Nombre/Lote
  - Densidad objetivo (semillas/ha)
  - Distancia entre surcos (cm)
  - Tramo medido (metros)
  - Distancias entre semillas (separadas por coma, espacio o enter)

- **Cálculos automáticos:**
  - Densidad real conseguida
  - Coeficiente de variación (CV)
  - Uniformidad
  - Espacios vacíos
  - Semillas dobles

### 2. **Modo Profesional**
- Análisis estadístico avanzado
- Gráficos de distribución
- Reportes detallados
- Exportación de datos

### 3. **Análisis de Imágenes (con Modelo YOLOv5)**
- Carga imágenes de siembra
- Detección automática de semillas
- Análisis de uniformidad
- Reporte visual

---

## 📊 Cálculos Disponibles

### Densidad Real
```
Densidad Real = (Semillas detectadas / Longitud del tramo) × 10,000 / Distancia entre surcos
```

### Coeficiente de Variación
```
CV = (Desviación estándar / Media) × 100
```

### Espacios Vacíos
Segmentos del tramo sin semillas dentro del patrón esperado.

### Semillas Dobles
Semillas a una distancia menor que el promedio esperado.

---

## 🎯 Flujo de Uso

### Paso 1: Recolectar Datos
1. En campo, mide un tramo de siembra
2. Registra las distancias entre semillas
3. Anota información del lote

### Paso 2: Ingresar Datos
1. Completa el formulario "Modo Campo"
2. Ingresa densidad objetivo
3. Copia las distancias medidas

### Paso 3: Analizar Resultados
1. El sistema calcula automáticamente:
   - Uniformidad
   - Variabilidad
   - Densidad real
2. Visualiza gráficos

### Paso 4: Generar Reporte
- Exporta resultados
- Comparte con agrónomo
- Archiva para histórico

---

## 💡 Consejos de Uso

### Medición en Campo
- ✅ Mide tramos de al menos 10 metros
- ✅ Usa cinta métrica precisa
- ✅ Mide en línea recta del surco
- ✅ Repite en varios surcos
- ❌ No midas en las cabeceras

### Entrada de Datos
- ✅ Separa distancias con: `,` o espacios o saltos de línea
- ✅ Usa valores en centímetros
- ✅ Revisa que la densidad objetivo sea realista
- ❌ No incluyas símbolos especiales

### Interpretación
- **CV < 20%**: Excelente uniformidad
- **CV 20-30%**: Buena uniformidad
- **CV > 30%**: Uniformidad deficiente

---

## 📱 Requisitos

- Navegador moderno (Chrome, Firefox, Safari, Edge)
- JavaScript habilitado
- Conexión a internet (solo para modelos en línea)

---

## 🔧 Características Técnicas

### Frontend
- HTML5 / CSS3
- JavaScript vanilla
- PWA (Progressive Web App)
- Funciona offline

### Backend (Servidor Local)
- Python 3.8+
- http.server
- YOLOv5 (opcional)

### Modelo de IA
- **Framework:** YOLOv5s
- **Clases:** 1 (semilla)
- **Precisión:** 71.8% (confianza promedio)
- **Entrada:** Imágenes 640x640px
- **Salida:** Bounding boxes + confianza

---

## 📁 Estructura del Proyecto

```
/workspaces/CONTROL-DE-SIEMBRA/
├── index.html              ← Interfaz principal
├── app.js                  ← Lógica de la aplicación
├── styles.css              ← Estilos
├── convertir-a-yolo.py     ← Conversión de datasets
├── entrenar_yolo.py        ← Entrenamiento del modelo
├── simular_deteccion.py    ← Simulación de detección
├── yolov5/                 ← Framework YOLOv5
│   └── runs/detect/        ← Modelos entrenados
└── datasets-yolo/          ← Datos de entrenamiento
```

---

## �� Próximas Mejoras

- [ ] Integración con base de datos
- [ ] API REST para análisis remoto
- [ ] Modelos entrenados para cultivos específicos
- [ ] Sincronización en la nube
- [ ] Reportes PDF automáticos
- [ ] Análisis de series temporales

---

## 📞 Soporte

Para problemas o sugerencias:

1. **Revisa la consola del navegador** (F12)
2. **Verifica los logs del servidor**
3. **Consulta la documentación técnica**

---

## 📜 Licencia

Proyecto de investigación INTA.
Basado en metodología de uniformidad de siembra.

---

**Última actualización:** 2025-11-15
**Versión:** 2.0
**Estado:** ✅ Funcional
