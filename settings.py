#The dnsname that the verification server will be available at.
#This will be used to construct the URLS by signing_tool.py (e.g.)
#   - https://verify.iosiro.com/verify?verification=[....]
dnsname_used_for_verificaiton = "verify.iosiro.com"

#Used by pgp tool to sign the message as a specific user.
user_to_sign_pgp_as = "security@iosiro.com"
