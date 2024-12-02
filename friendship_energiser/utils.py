import logging
from os import makedirs
from os.path import dirname
import time


LOGGING_FILE = f"logs/{time.strftime('%Y/%m')}/{time.strftime('%d-%m-%Y')}.log"
LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s] - %(message)s"

logger = logging.getLogger(__name__)


def init_logs() -> None:

    makedirs(
        dirname(LOGGING_FILE),
        exist_ok=True
    )

    logging.basicConfig(
        level=logging.INFO,
        filename=LOGGING_FILE,
        filemode='a',
        format=LOGGING_FORMAT
    )
