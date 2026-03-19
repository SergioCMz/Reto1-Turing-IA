import functions_framework
from google.cloud import logging

@functions_framework.cloud_event
def process_metadata(cloud_event):
    # Inicialización del Logger
    logging_client = logging.Client()
    logger = logging_client.logger("turing-ia-logs")

    try:
        # Extracción de metadatos
        data = cloud_event.data
        name = data.get("name")
        size = data.get("size")
        content_type = data.get("contentType")
        bucket = data.get("bucket")

        # Construcción del log
        log_payload = {
            "evento": "Procesamiento de Archivo",
            "archivo": name,
            "tamaño_bytes": size,
            "tipo": content_type,
            "bucket_origen": bucket,
            "estado": "EXITOSO"
        }
        
        # Registro para el analisis y para la visualización en la consola
        logger.log_struct(log_payload, severity="INFO")
        print(f"Metadatos procesados para: {name}")

    except Exception as e:
        # Manejo de los errores para que no interrumpan el servicio
        logger.log_text(f"ERROR en procesamiento: {str(e)}", severity="ERROR")
