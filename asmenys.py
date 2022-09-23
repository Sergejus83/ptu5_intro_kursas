import logging
import dalyba
# import logger

# logging.basicConfig(
#     filename = "asmenys.log",
#     level = logging.INFO,
#     format="%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s"
# ) #(lineno) - line number

# sukuriam savo loggeri, kuri pavadinam paleistos programos pavadinimu
logger = logging.getLogger(__name__)
# sukuriam file handleri, kuris zinute rasys i nurodita faila
file_handler = logging.FileHandler('aritmetika.log') # failo manager, per tai eis failai
# loggeriu priskiriam file handleri
logger.addFilter(file_handler)
# nurodom, kokio lygio zinutes loggeris apdoros
logger.setLevel(logging.DEBUG)
# nusirodom zinutes formata
formater = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s")
# file henderiui priskiriam formata
file_handler.setFormatter(formater)
# sukuriam stream handleri , kuris zinute spausdins i terminala
stream_handler = logging.StreamHandler()
# priskiriam stream handleriui formatą (tą patį, kurį buvom priskyrę ir file handleriui)
stream_handler.setFormatter(formater)
# loggeriui priskiriam stream handlerį, panašiai kaip ir buvom priskyrę file handlerį
logger.addHandler(stream_handler)

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas=vardas
        self.avarde=pavarde
        logging.info(f"Sukurtas klase {self.__class__.__name__} objektas {vardas} {pavarde}")

ingrida = Asmuo("Ingrida", "Vaitkuviene")
sergejus = Asmuo("Sergejus", "Bykovas")

print(dalyba.daugyba(9, 5))

# print(logger.daugyba(2,5))
