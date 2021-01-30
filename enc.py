import sys,base64,time,hashlib,os
from cryptography.fernet import Fernet
#variables
f=Fernet
intr='''---------------------------
--Tsociety file encrypter--
1)encrypt
2)decrypt
99)exit
---------------------------
>'''
#gets input to turn into 32 url safe characters and convert it into md5 then byte like objects to use as fernet kney
def key():
    print('')
    key=input('password>')
    keyc=len(key)
    if keyc<=7:
        print('password must have at least 8 characters')
        sys.exit()
    elif keyc>=33:
        print('password must be less than 33 characters')
        sys.exit()
    key=hashlib.md5(str(key).encode())
    key=key.hexdigest()
    print(str(key))
    key=base64.urlsafe_b64encode(bytes(str(key),'utf-8'))
    return(key)
#uses the given key to encrypt a file with the given filename
def enc(key):
    print('')
    fi=input('filename>')
    print('')
    print('   ***reading file data...***')
    os.system('zip enc -r %s'%fi)
    fd=open('enc.zip','rb').read()
    time.sleep(0.3)
    print('')
    print('***initializing Fernet key...***')
    time.sleep(0.4)
    print('')
    os.system('rm -rf %s'%fi)
    print('   ***encrypting file data***')
    print('')
    en=f(key).encrypt(fd)
    open(fi+'.enc','wb').write(en)
    print('      ***file encrypted***')
    os.system('rm -rf enc.zip')
    print('')
#uses the given key to decrypt a file with the given filename
def dec(key):
    print('')
    fi=input('filename>')
    print('')
    print('   ***reading file data...***')
    fd=open(fi,'rb').read()
    time.sleep(0.2)
    print('')
    print('***initializing Fernet key...***')
    time.sleep(0.35)
    print('')
    print('    ***decrypting data...***')
    print('')
    de=f(key).decrypt(fd)
    open(fi.replace('.enc','.zip'),'wb').write(de)
    os.system('unzip %s'%fi.replace('.enc',''))
    print('      ***file decrypted***')
    os.system('rm -rf %s'%fi.replace('.enc','.zip'))
    os.system('rm -rf %s'%fi)
    print('')
#run
while True:
    c=input(intr)
    if c=='1':
        enc(key())
    elif c=='encrypt':
        enc(key())
    elif c=='2':
        dec(key())
    elif c=='decrypt':
        dec(key())
    elif c=='99':
        break
    elif c=='exit':
        break
    else:
        print('input a number shown')
