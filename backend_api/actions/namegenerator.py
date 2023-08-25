import random
from datetime import datetime, timezone

def nameGenerator():
    name = 'output'
    name+=str(datetime.now(timezone.utc).timestamp())
    for i in range(6):
        name+=str(random.randint(1,10)) 
    return ''.join(name.split('.'))