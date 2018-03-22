import os
import datetime
import base64
import json
import subprocess
import hashlib
from settings import *
client = input("Client Name:")
work_nature = input("What work was performed?:")
description = input("Enter a description of the work (e.g. commit hash, URL):")
link = input("Enter a link to the project(github/blockchain):")
date = datetime.datetime.now()

message = {
  "client_name" : client,
  "date_signed" : str(date),
  "nature_of_work" : work_nature,
  "description" : description,
  "link" : link
}
b64_msg = json.dumps(message).encode()
if 'y' in input("Are you happy with the below message:\n\n{}\n\n(y/n)".format(message)):
    print (b64_msg.decode())
    filepath = '/tmp/{}.create'.format(hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest())
    to_sign_file = open(filepath, 'w')
    to_sign_file.write(b64_msg.decode())
    to_sign_file.close()

    proc = os.system("gpg -u {} -a --clear-sign {}".format(user_to_sign_pgp_as, filepath))

    signed_file = open(filepath+'.asc', 'r')
    content = signed_file.read()
    signed_file.close()
    os.remove(filepath)
    os.remove(filepath+'.asc')
    print()
    print (content)
    print ('============\nFINAL\n============\n\n')
    print("https://{}/verify?verification={}".format(dnsname_used_for_verificaiton, base64.b64encode(content.encode()).decode()))
