import logging
logger = logging.getLogger('nva.tbskin')

def log(message, summary='', severity=logging.INFO):
    logger.log(severity, '%s %s', summary, message)
