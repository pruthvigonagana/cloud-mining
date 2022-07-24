import mysql.connector
import random
from hashlib import sha256
MAX_NONCE=100000000
def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()
def mine(block_number,transaction,previous_hash,prefix_zeros):
  transaction_id = random.getrandbits(32)
  prefix_str='0'*prefix_zeros
  for nonce in range(MAX_NONCE):
    text= str(block_number) + str(transaction) + str(previous_hash) + str(nonce)
    hash = SHA256(text)
    # print(hash)
    if hash.startswith(prefix_str):
      print("Bitcoin mined with nonce value :",nonce)
      print("Bitcoin mined with transaction id value :",str(transaction_id))
      return hash,nonce,str(transaction_id)
  print("Could not find a hash in the given range of upto", MAX_NONCE)


difficulty = 5

import time as t
begin=t.time()

list1=["hbdihbviHDbvhDbvDBvSB","bhbsdhbvsjhbvjhsfbvhjfsbvs", "vdvjdhfvhjdvhjdf", "bfdshbSDHJvdsjvsdhjfv ", "fhebfhjhjvhvsdhjvshjfv", "gsvfjhdvhjdvfhjdvfhjDfhjDhjfvjhfvhj"]
blockNumber=["5645498498498","456416549654","6558984984984","654584846545646584654658485","454564654445656"]
PreviousHash=["848948548948940","45645656468548960","46544184848","44646584484164"]
for i in range(0, len(list1)):
    mine(blockNumber[i],list1[i],PreviousHash[i],difficulty)
