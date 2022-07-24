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
cnx = mysql.connector.connect(user='admin', password='12345678',host='blockdb-instance1.cqxy7vurxinp.us-east-1.rds.amazonaws.com',database='blockdb3')
mycoursor= cnx.cursor()
mycoursor.execute("SELECT transactions FROM blockdb3.temp_table")
myreslt=mycoursor.fetchall()
mycoursor.execute("SELECT id FROM blockdb3.temp_table;")
Id=mycoursor.fetchall()
mycoursor.execute("SELECT nonce FROM blockdb3.transaction order by nonce desc limit 1;")
nonce= mycoursor.fetchone()
mycoursor.execute("SELECT hashvalue FROM blockdb3.transaction order by hashvalue desc limit 1;")
hashvalue= mycoursor.fetchone()
for i in myreslt:
 new_hash, new_nonce, new_transactionid = mine(nonce, i, hashvalue,difficulty)
 print("Hash value : ",new_hash)
 time_taken=t.time()- begin
 print("The mining process took ",time_taken,"seconds")
 comin= "INSERT INTO `blockdb3`.`transaction`(`transaction_id`,`nonce`,`transaction`,`hashvalue`)VALUES(" "'"+ str(new_transactionid) + "'"",'" + str(new_nonce)  + "','" + str(i[0]) + "','" + str(new_hash) + "');"
 mycoursor.execute(comin)
 cnx.commit()
print(comin)
for i in Id:
 mycoursor.execute("DELETE FROM `blockdb3`.`temp_table` WHERE id = '"+ i[0] +"' ;")

#mycoursor.execute(""))
cnx.commit()
cnx.close()
