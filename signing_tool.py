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
if 'y' in input("Would you like to give a contract by contract specification of what was audited along with the hash of said contract?:"):
    contract_name = input("\n[+] Please enter the name of the contract. Type 'END' to finish:")
    contracts = []
    while 'END' not in contract_name:
        string = ""
        string+=contract_name
        if 'y' in input("\tDo you want to add a hash for the file '{}'?".format(contract_name)):
            hash = input("\tPlease enter the commit hash for the contract:")
            string+=": "+hash
        contracts.append(string)
        contract_name = input("\n\n[+] Please enter the name of the contract. Type 'END' to finish:")
        print("[+] Currently {} contracts listed.".format(len(contracts)))

    if len(contracts) > 0:
        message["contracts"] = contracts



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

    print ('============\nFINAL\n============\n\n')

    ####
    # GENERATE THE DARK BADGE
    ####

    badge_light = open("badge_light.html")
    contents = badge_light.read()
    badge_light.close()

    contents = contents.replace("{{link}}", "https://{}/verify?verification={}".format(dnsname_used_for_verificaiton, base64.b64encode(content.encode()).decode()))

    client_badge_light = open("client_badges/iosiro_{}_light.html".format(client.replace(" ", "")), 'w')
    client_badge_light.write(contents)
    client_badge_light.close()

    print (contents)
    ####
    # GENERATE THE DARK BADGE
    ####

    badge_dark = open("badge_dark.html")
    contents = badge_dark.read()
    badge_dark.close()

    contents = contents.replace("{{link}}", "https://{}/verify?verification={}".format(dnsname_used_for_verificaiton, base64.b64encode(content.encode()).decode()))

    client_badge_dark = open("client_badges/iosiro_{}_dark.html".format(client.replace(" ", "")), 'w')
    client_badge_dark.write(contents)
    client_badge_dark.close()


    print(contents)
