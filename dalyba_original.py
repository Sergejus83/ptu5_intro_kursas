# DEBUG Detailed information, typically of interest only when diagnosing problems.
# INFO Confirmation that things are working as expected.
# WARNING An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL A serious error, indicating that the program itself may be unable to continue running

# gali rusiuoti klaidos(error) pagal svarbumo level DEBUG - problemu ieskojamas
import logging 
from modules.aritmetika import daugyba

logging.basicConfig(level = logging.DEBUG, filename="problem.log",format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

def dalyba(a, b):
    try:
        res = a/b
    except Exception as e:
        # ismetam pranesima kad ivyko klaida
        logging.error(f"vykdant klaida {e.__class__.__name__}: {e}")
        return None
    else:
        logging.info(f"paleista funkcija: {dalyba.__name__}: {a}/{b}={res}")
        return res
    
dalyba(7, 0)
dalyba(7, 3)
print(dalyba(7, 0))
print(dalyba(7, 3))
