import math
import logging
#logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s %(levelname)s : %(message)s")
# logger = logging.getLogger(__name__)
# console_log = logging.StreamHandler()
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
# console_log.setFormatter(formatter)
# logger.addHandler(console_log)
# testing git

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)

logger.setLevel(logging.ERROR)
#logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def get_sum(*args):
    logging.info("executing get_sum operation")
    s = sum(args)
    logger.info(f"sum of ({args}) = {s}")
    logger.debug(f"sum of ({args}) = {s}")
    return s


def get_sqrt(number):
    result = 0
    try:
        result = math.sqrt(number)
    except ValueError:
        logger.exception(f"invalid value of number. Value queals to = {number}")
    except TypeError:
        logger.exception(f"invalid value of number. Value queals to = {number}")
    else:
        logger.info(f"the result of sqrt from number {number} = {result}")
    return result


def get_number_of_symbols(sentence):

    sentence_lenght = len(sentence)
    logger.info(f"the lenght of the sentence ({sentence}) is {sentence_lenght}")
    return sentence_lenght


def get_division(x, y):
    result = 0
    try:

        result = x / y
    except ZeroDivisionError:
        logger.exception(f"You are trying to divide zero!!!! {x} / {y}")
    else:
        logger.info(f" the result of division function {x} / {y} = {result} ")

    return result
