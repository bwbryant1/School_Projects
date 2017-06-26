#!/usr/bin/env python
"""
I ATTEMPTED AND SUCCESSFULLY COMPLETED THE BONUS
Credits = {"author_name": "Brandon Bryant", "date": "5/3/2017", "description": "A short program to collect and extract certificate information from a given domain name","resources_used":"python 2.7,PyOpenSSL,Various Python Documentation,SSL Socket wrapper program previously made"}
"""
import sys, ssl, socket
from OpenSSL import crypto

hostname = sys.argv[1] #this stores the hostname
port = sys.argv[2] #this stores the desired port

context = ssl.create_default_context() #create the context object
s = context.wrap_socket(socket.socket(), server_hostname=hostname) #Wrap the regular socket with ssl
s.connect((hostname, int(port))) #connect to the desired port

cert = s.getpeercert() #grab the certificate information when connection is made
cert2 =ssl.get_server_certificate((hostname, port)) #this grabs the certificate plain text so i can extract my public key

#Domain Name: #All the domain names associated with the cert
print "Domain Name: ",
for x in cert['subjectAltName']:
	sys.stdout.write(x[1] + ",")

#Issue Date of the cert
print "\nIssue Date: "+cert['notBefore']

#Expiry Date: when the cert will expire
print "Expiry Date: "+cert['notAfter']

#Issuer's CN
issuer = dict(x[0] for x in cert['issuer'])
print "Issuer's CN: "+issuer['commonName']

#CA Issuers: Certificate Authority Issuers
print "CA Issuers: ",
for x in cert['caIssuers']:
        sys.stdout.write(x)

#OCSP: The Online Certificate Status Protocol
print "\nOSCP: ",
for x in cert["OCSP"]:
	sys.stdout.write(x)

#Cipher method used
print "\nCipher: "+str(s.cipher()[0])

#SSL Version
print "SSL Version: "+(s.cipher()[1])

#Secret Bits
print "Secret Bits: "+str(s.cipher()[2])

#This last bit is the bonus!
x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert2)
print crypto.dump_publickey(crypto.FILETYPE_PEM, x509.get_pubkey()) 
