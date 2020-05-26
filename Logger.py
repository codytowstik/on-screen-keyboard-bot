import logging

class Logger:
    # FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT)

    logger = logging.getLogger('maple_auto_bot')
    logger.setLevel(20)

    def debug(self, message: str, *args):
        message = self.__format_message(message, *args)

        self.logger.debug('DEBUG: %s', message)

    def info(self, message: str, *args):
        message = self.__format_message(message, *args)

        self.logger.info('INFO: %s', message)

    def warning(self, message: str, *args):
        message = self.__format_message(message, *args)
        self.logger.warning('WARN: %s', message)

    def __format_message(self, message: str, *args) -> str:
        if len(args) > 0:
            message = message.format(*args)

        return message