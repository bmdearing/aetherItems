import random
from unittest import result

# Going down the Rarities
#region Rarity
# Common - Makes up the bulk of items                               48.0%
# Uncommon - Can have some magical properties                       30.0%
# Rare - Items that are populated with more affixes than uncommons. 20.0%
# Unique - Unique items are set items that have in game relevance.  01.0%
# Legendary - Items with access to an upper echelon of affixes.     00.01%
#endregion

count = 0
rarity = ['Common', 'Uncommon', 'Rare', 'Unique', 'Legendary']

while True:
    results = random.choices(rarity, weights=[49, 30, 20, 1, 0.01])
    print(f"{results}")
    count += 1
    if results[0] == "Legendary":
        print(f"{results}, {count}")
        break
        
    
def itemRarity():
    count = 0

def itemBaseType():
    count = 0
    
