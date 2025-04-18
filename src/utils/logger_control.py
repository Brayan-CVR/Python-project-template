import logging


def start_logger() -> None:
    """_summary_
    """    
    # Configuración básica de logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def get_logger(name: str) -> logging.Logger:
    """_summary_

    Args:
        name (str): _description_

    Returns:
        logging.Logger: _description_
    """    
    logger = logging.getLogger(name)
    return logger


if __name__ == "__main__":
    print("Ejecutando pruebas del módulo...")
    start_logger()
    logger = get_logger(__name__)
    logger.info("Pruebas del modulo terminadas con exito.\n")
