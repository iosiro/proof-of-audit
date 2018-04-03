import tornado.ioloop
import tornado.web
import json
import base64
import hashlib
import os
import subprocess
from subprocess import PIPE
from settings import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        verification_stringb64 = self.get_argument("verification", None)
        if verification_stringb64:
            try:
                decoded = base64.b64decode(verification_stringb64)
                checkpgp = verify_pgp_signature(decoded)
                if checkpgp:
                    msg = extract_message_from_signed_pgp(decoded.decode())
                    verification_values = json.loads(msg)

                    #In case we get passed the contracts parameter
                    print(verification_values)
                    if verification_values.get("contracts", False):
                        print (verification_values['contracts'])
                        self.render("html/success.html", client_name = verification_values['client_name'],
                    description= verification_values['description'], date_signed=verification_values['date_signed'].split(" ")[0],
                    nature_of_work=verification_values['nature_of_work'], link=verification_values['link'],
                    contracts=verification_values['contracts'])
                    else:
                        self.render("html/success.html", client_name = verification_values['client_name'],
                    description= verification_values['description'], date_signed=verification_values['date_signed'].split(" ")[0],
                    nature_of_work=verification_values['nature_of_work'], link=verification_values['link'],
                    contracts=[])
                else:
                    self.render("html/error.html", error_message="The signature on the badge is incorrect!")
            except Exception as e:
                print (e)
                self.render("html/error.html", error_message="Something went wrong, that's all we know.")
        else:
            self.render("html/error.html", error_message="Hmmmm. That badge wasn't configured correctly. Please let the website know!")

def extract_message_from_signed_pgp(text):
    start = '''-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512
'''
    end = "-----BEGIN PGP SIGNATURE-----"
    msg = text.split(start)[1].split(end)[0]
    return msg

def verify_pgp_signature(text):
    print ("verifying {}".format(text))
    md5_of_text = hashlib.md5(text).hexdigest()
    filepath = '/tmp/{}'.format(str(md5_of_text))

    if os.path.exists(filepath):
        sig_check = check_file_signature(filepath)
    else:
        data_file = open(filepath, 'w')
        data_file.write(text.decode())
        data_file.close()
        sig_check = check_file_signature(filepath)
    return sig_check

def check_file_signature(filepath):
    proc = subprocess.Popen(["gpg", "--verify-file", filepath], stdout=PIPE , stderr=PIPE)
    output = proc.stderr.read().decode()
    is_good_sig = False
    is_correct_user = False
    for i in output.splitlines():
        if '''gpg: Good signature from''' in i:
            is_good_sig = True
        if '''BAD signature from''' in i:
            is_good_sig = False
            break
        if key_fingerprint.lower() in i.lower().replace(" ", ""):
            is_correct_user = True

    if is_correct_user and is_good_sig:
        print ("[+] Good signature found...")
        return True
    else:
        print ("[!] Signature is BAD!")
        return False

class LandingPage(tornado.web.RequestHandler):
    def get(self):
        self.redirect(redirect_url)

def make_app():
    return tornado.web.Application([
        (r"/verify", MainHandler),
        (r"/", LandingPage),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'html/static/'}),
        (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""})

    ])

if __name__ == "__main__":
    #Import public key...
    os.system("gpg --import public_key.pub")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
