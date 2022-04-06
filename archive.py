import logging
import os.path
import shutil
import datetime

from utility import get_app_archive_dir, get_script_name

logger = logging.getLogger(__name__)


def auto_archive(filename):
    logger.info(f"{get_script_name()} execution started .")
    try:
        logger.info(f"File to be archived : {filename}")
        archive_dir = get_app_archive_dir()
        if not os.path.exists(archive_dir):
            logger.info(f"Looks like there is no archive directory, so creating one")
            os.makedirs(archive_dir)
        file_basename = os.path.splitext(filename)[0]
        file_ext = os.path.splitext(filename)[1]
        archive_filename = file_basename + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + file_ext
        archive_file = archive_dir + archive_filename
        logger.info(f"Base Filename: {filename}")
        logger.info(f"Archived Filename: {archive_filename}")
        shutil.copy(filename, archive_file)
        logger.info("Archive process was successful !!!")
    except Exception as e:
        logger.error(e)

