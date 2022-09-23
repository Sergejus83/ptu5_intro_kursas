import logging 

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log') # failo manager, per tai eis failai
logger.addFilter(file_handler)
logger.setLevel(logging.DEBUG)
formater = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s")
file_handler.setFormatter(formater)

def daugyba(a, b):
    try:
        res = a*b
    except Exception as e:
        # ismetam pranesima kad ivyko klaida
        logger.error(f"vykdant klaida {daugyba.__name__}, ivyko klaida {e.__class__.__name__}: {e}")
        return None
    else:
        logger.info(f"paleista funkcija: {daugyba.__name__}: {a} * {b} = {res}")
        return res
    
daugyba(7, 0)
