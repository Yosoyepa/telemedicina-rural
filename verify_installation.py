#!/usr/bin/env python3
"""
Script de verificación de instalación para el Sistema de Telemedicina Rural Colombia
Verifica que todas las dependencias críticas estén instaladas y funcionando correctamente.
"""

import sys
import importlib
from typing import List, Tuple

def check_dependency(module_name: str, description: str) -> Tuple[bool, str]:
    """Verifica si un módulo puede ser importado correctamente."""
    try:
        importlib.import_module(module_name)
        return True, f"✅ {description}"
    except ImportError as e:
        return False, f"❌ {description} - Error: {str(e)}"
    except Exception as e:
        return False, f"⚠️  {description} - Warning: {str(e)}"

def main():
    """Función principal que ejecuta todas las verificaciones."""
    print("🏥 Sistema de Telemedicina Rural Colombia - Verificación de Instalación")
    print("=" * 70)
    
    # Lista de dependencias críticas a verificar
    dependencies = [
        # Framework web y servidor
        ("fastapi", "FastAPI - Framework web moderno"),
        ("uvicorn", "Uvicorn - Servidor ASGI"),
        ("pydantic", "Pydantic - Validación de datos"),
        ("starlette", "Starlette - Framework ASGI base"),
        
        # Base de datos y cache
        ("sqlalchemy", "SQLAlchemy - ORM para bases de datos"),
        ("asyncpg", "AsyncPG - Driver PostgreSQL asíncrono"),
        ("redis", "Redis - Cliente para cache y colas de mensajes"),
        
        # Seguridad y autenticación
        ("passlib", "PassLib - Librería de hashing de contraseñas"),
        ("jose", "Python-JOSE - Manejo de tokens JWT"),
        ("cryptography", "Cryptography - Operaciones criptográficas"),
          # Procesamiento de datos médicos
        ("hl7", "HL7 - Estándares de intercambio de datos médicos"),
        ("pydicom", "PyDICOM - Manejo de imágenes médicas DICOM"),
        ("PIL", "Pillow - Procesamiento de imágenes"),
        ("lz4", "LZ4 - Compresión rápida de datos médicos"),
        
        # Análisis y visualización
        ("numpy", "NumPy - Computación numérica"),
        ("pandas", "Pandas - Análisis de datos"),
        ("matplotlib", "Matplotlib - Generación de gráficos"),
        ("seaborn", "Seaborn - Visualización estadística"),
        ("scipy", "SciPy - Computación científica"),
        ("sklearn", "Scikit-learn - Machine Learning"),
        
        # Red y conectividad
        ("scapy", "Scapy - Manipulación de paquetes de red"),
        ("httpx", "HTTPX - Cliente HTTP asíncrono"),
        ("ping3", "Ping3 - Testing de conectividad"),
        ("speedtest", "Speedtest-CLI - Testing de ancho de banda"),
        
        # Tareas asíncronas y colas
        ("celery", "Celery - Procesamiento de tareas distribuidas"),
        ("kombu", "Kombu - Librería de mensajería"),
        
        # Testing y desarrollo
        ("pytest", "Pytest - Framework de testing"),
        ("black", "Black - Formateador de código"),
        ("flake8", "Flake8 - Linter"),
        ("mypy", "MyPy - Verificador de tipos estáticos"),
        ("isort", "isort - Organizador de imports"),
        
        # Utilidades del sistema
        ("psutil", "PSUtil - Información del sistema"),
        ("yaml", "PyYAML - Parser YAML"),
        ("click", "Click - Interfaz de línea de comandos"),
    ]
    
    # Ejecutar verificaciones
    success_count = 0
    total_count = len(dependencies)
    failed_dependencies = []
    
    for module_name, description in dependencies:
        success, message = check_dependency(module_name, description)
        print(message)
        if success:
            success_count += 1
        else:
            failed_dependencies.append((module_name, description))
    
    print("\n" + "=" * 70)
    print(f"📊 Resumen de verificación:")
    print(f"   ✅ Dependencias exitosas: {success_count}/{total_count}")
    print(f"   ❌ Dependencias fallidas: {total_count - success_count}/{total_count}")
    
    if failed_dependencies:
        print(f"\n⚠️  Dependencias que requieren atención:")
        for module_name, description in failed_dependencies:
            print(f"   - {module_name}: {description}")
        print(f"\n💡 Para instalar dependencias faltantes, ejecuta:")
        print(f"   pip install -r requirements.txt")
    
    # Verificación de versión de Python
    python_version = sys.version_info
    print(f"\n🐍 Versión de Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major == 3 and python_version.minor >= 11:
        print("✅ Versión de Python compatible (3.11+)")
    else:
        print("⚠️  Se recomienda Python 3.11 o superior para compatibilidad completa")
    
    # Verificación básica de funcionalidad
    print(f"\n🧪 Verificaciones básicas de funcionalidad:")
    
    try:
        from fastapi import FastAPI
        app = FastAPI()
        print("✅ FastAPI puede crear instancias correctamente")
    except Exception as e:
        print(f"❌ Error creando instancia de FastAPI: {e}")
    
    try:
        import redis
        # Solo verificar que se puede crear el cliente, no conectar
        redis_client = redis.Redis()
        print("✅ Cliente Redis puede ser instanciado")
    except Exception as e:
        print(f"❌ Error creando cliente Redis: {e}")
    
    try:
        from sqlalchemy import create_engine
        # Crear engine en memoria para testing
        engine = create_engine("sqlite:///:memory:")
        print("✅ SQLAlchemy puede crear engines correctamente")
    except Exception as e:
        print(f"❌ Error creando engine SQLAlchemy: {e}")
    
    print(f"\n🎉 Verificación completada!")
    
    if success_count == total_count:
        print("🚀 ¡Todas las dependencias están instaladas y funcionando correctamente!")
        print("   El sistema está listo para el desarrollo.")
        return 0
    else:
        print("⚠️  Algunas dependencias requieren atención antes de continuar.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
