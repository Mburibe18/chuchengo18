# DADO_1 =(1,6)
# DADO_2 =(1,6)
# NUMERO_DESEADO = 12
# SUMA = DADO_1 + DADO_2
# while (SUMA = NUMERO_DESEADO):
#   print (NUMERO_DESEADO)

import random
import random

NUMERO_DADO_1 = random.randint(1,6)
NUMERO_DADO_2 = random.randint(1,6)
SUMA = (NUMERO_DADO_1 + NUMERO_DADO_2  )
NUMERO_DESEADO = 12



while (SUMA != NUMERO_DESEADO):
    print (SUMA)
    NUMERO_DADO_1 = random.randint(1,6)
    NUMERO_DADO_2 = random.randint(1,6)
    SUMA = (NUMERO_DADO_1 + NUMERO_DADO_2 )
    print (SUMA)


