import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("bse_v2")


def info(message):
    logger.info(message)


def warning(message):
    logger.warning(message)


def error(message):
    logger.error(message)