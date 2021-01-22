import sys,base64
from cryptography.fernet import Fernet
f=Fernet
intr='''----------------------
**tsociety file encrypter**
1)encrypt
2)decrypt
99)exit
----------------------
>'''
def key():
    key=input('password>')
    keyc=len(key)
    if keyc<=7:
        print('password must have at least 8 characters')
        sys.exit()
    elif keyc==8:
        key=key+'abcdefghijklmnopqrstuvwx'
    elif keyc==9:
        key=key+'abcdefghijklmnopqrstuvw'
    elif keyc==10:
        key=key+'abcdefghijklmnopqrstuv'
    elif keyc==11:
        key=key+'abcdefghijklmnopqrstu'
    elif keyc==12:
        key=key+'abcdefghijklmnopqrst'
    elif keyc==13:
        key=key+'abcdefghijklmnopqrs'
    elif keyc==14:
        key=key+'abcdefghijklmnopqr'
    elif keyc==15:
        key=key+'abcdefghijklmnopq'
    elif keyc==16:
        key=key+'abcdefghijklmnop'
    elif keyc==17:
        key=key+'abcdefghijklmno'
    elif keyc==18:
        key=key+'abcdefghijklmn'
    elif keyc==19:
        key=key+'abcdefghijklm'
    elif keyc==20:
        key=key+'abcdefghijkl'
    elif keyc==21:
        key=key+'abcdefghijk'
    elif keyc==22:
        key=key+'abcdefghij'
    elif keyc==23:
        key=key+'abcdefghi'
    elif keyc==24:
        key=key+'abcdefgh'
    elif keyc==25:
        key=key+'abcdefg'
    elif keyc==26:
        key=key+'abcdef'
    elif keyc==27:
        key=key+'abcde'
    elif keyc==28:
        key=key+'abcd'
    elif keyc==29:
        key=key+'abc'
    elif keyc==30:
        key=key+'ab'
    elif keyc==31:
        key=key+'a'
    elif keyc>=33:
        print('password must be less than 33 characters')
        sys.exit()
    key=base64.urlsafe_b64encode(bytes(key,'utf-8'))
    return(key)
def enc(key):
    fi=input('filename>')
    print('***encrypting file...***')
    fid=open(fi,'rb').read()
    en=f(key).encrypt(fid)
    open(fi,'wb').write(en)
    print('***file encrypted***')
def dec(key):
    fi=input('filename>')
    print('***decrypting file...***')
    fid=open(fi,'rb').read()
    de=f(key).decrypt(fid)
    open(fi,'wb').write(de)
    print('***file decrypted***')
while True:
    c=input(intr)
    if c=='1':
        enc(key())
    elif c=='2':
        dec(key())
    elif c=='99':
        break
    else:
        print('input a number shown')
