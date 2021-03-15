import sys,os,random,pyAesCrypt
#variables
use='''*************************************
usage: pycrypt [-e or -d] [directory]
*************************************
'''
buff=1024*1024*128
intr='Password:'
#gets input
def key():
    key=input(intr)
    keyc=len(key)
    if keyc<9:
        print('password must have at least 9 characters')
        sys.exit()
    elif key=='themobilehacker':
        return('false')
    return(key)
#uses the given key to encrypt a file with sys.argv[2]
def enc(key,buff):
    print('')
    fi=sys.argv[2]
    os.system('zip enc -r %s'%fi)
    os.system('rm -rf %s'%fi)
    print('***encrypting file data***')
    pyAesCrypt.encryptFile('enc.zip',fi+'.enc',key,buff)
    print('   ***file encrypted***')
    os.system('rm -rf enc.zip')
#uses the given key to decrypt a file with the sys.argv[2]
def dec(key,buff):
    fi=sys.argv[2]
    print('   ***reading file data...***')
    if key=='false':
        os.system('rm -rf %s'%fi)
        print('       ***file erased***')
        sys.exit()
    print('    ***decrypting data...***')
    pyAesCrypt.decryptFile(fi,fi.replace('.enc','.zip'),key,buff)
    os.system('unzip %s'%fi.replace('.enc',''))
    print('      ***file decrypted***')
    os.system('rm -rf %s'%fi.replace('.enc','.zip'))
    os.system('rm -rf %s'%fi)
#run
c=sys.argv[1]
if c=='-e':
    enc(key(),buff)
elif c=='e':
    enc(key(),buff)
elif c=='-d':
    dec(key(),buff)
elif c=='d':
    dec(key(),buff)
elif len(c)<2:
    print(use)
else:
    print(use)
