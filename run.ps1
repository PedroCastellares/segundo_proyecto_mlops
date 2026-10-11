# ========================================================================
# 🛠️ SCRIPT ORQUESTADOR Y CONTROL REMOTO DE AUTOMATIZACIÓN DE MLOPS
# ========================================================================

# TAREA 1: Ejecutar la suite de auditoría de calidad con Pytest
function Ejecutar-Pruebas {
    Write-Host "`n🧪 [Fase 1] Ejecutando pruebas unitarias de calidad con Pytest..." -ForegroundColor Cyan
    python -m pytest
}

# TAREA 2: Compilar la cápsula hermética de Docker de forma automatizada
function Compilar-Contenedor {
    Write-Host "`n🐳 [Fase 2] Reconstruyendo la imagen de Docker aislada..." -ForegroundColor Cyan
    docker build -t mi_segundo_pipeline_mlops .
}

# TAREA 3: Encender el servidor científico de MLflow dentro del túnel blindado
function Encender-Servidor {
    Write-Host "`n🚀 [Fase 3] Abriendo túnel de red y encendiendo servidor web de MLflow..." -ForegroundColor Cyan
    Write-Host "🌐 Ingresa a http://localhost:5000 en tu navegador cuando finalice el arranque." -ForegroundColor Yellow
    docker run --rm -p 5000:5000 mi_segundo_pipeline_mlops
}

# --- FLUJO PRINCIPAL EN CASCADA (EL ESCUDO DE SEGURIDAD) ---
# Ejecutamos primero los exámenes de calidad automatizados
Ejecutar-Pruebas

# '\$LASTEXITCODE' es una variable interna de Windows que captura el resultado del comando anterior.
# Si es igual a 0, significa que los 2 tests de Pytest pasaron con éxito total en verde.
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Calidad certificada. Procediendo con el empaquetamiento..." -ForegroundColor Green
    Compilar-Contenedor
    Encender-Servidor
} else {
    # Si alguna prueba llega a fallar, el robot detiene la fábrica inmediatamente por seguridad.
    Write-Host "`n🛑 [ALERTA] Pruebas fallidas. El pipeline se detuvo para proteger producción." -ForegroundColor Red
}
