#The dnsname that the verification server will be available at.
#This will be used to construct the URLS by signing_tool.py (e.g.)
#   - https://verify.iosiro.com/verify?verification=[....]
dnsname_used_for_verificaiton = "verify.iosiro.com"

#Used by pgp tool to sign the message as a specific user.
user_to_sign_pgp_as = "security@iosiro.com"

#The fingerprint of the key that should sign the message
key_fingerprint = "F0F1030F44A2152DB9BCDC505192FC208D1E2DDB"

#URL to redirect to if landing page is visited
redirect_url = "https://www.iosiro.com/"
