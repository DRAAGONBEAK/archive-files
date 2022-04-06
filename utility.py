import logging
import os

logger = logging.getLogger(__name__)


def get_script_name():
    return os.path.basename(__file__)


def get_root_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_app_archive_dir():
    return get_root_dir() + os.sep + 'archive' + os.sep
