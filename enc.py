import sys,time,os,random,pyAesCrypt
#variables
buff=1024*1024*64
intr='''--Tsociety file encrypter--
1)encrypt
2)decrypt
99)exit
---------------------------
>'''
#gets input to use as key
def key():
    print('')
    #creates random numbers to confuse keyloggers
    n1=str(random.randint(1,10))
    n2=str(random.randint(1,10))
    print('char: %s'%n1+n2)
    key=input('''enter password with last few characters being the ones shown
pass>''')
    keyc=len(key)
    if keyc<9:
        print('password must have at least 9 characters')
        sys.exit()
    elif key=='themobilehacker': #self-destruct password
        key='false'
        return(key)
    key=str(keyc).replace(n1+n2,'')
    return(key)
#uses the given key to encrypt a file with the given filename
def enc(key,buff):
    print('')
    fi=input('filename>')
    print('')
    print('***reading file data...***')
    os.system('zip enc -r %s'%fi) #compresses the file
    print('')
    os.system('rm -rf %s'%fi)
    print('***encrypting file data***')
    print('')
    pyAesCrypt.encryptFile('enc.zip',fi+'.enc',key,buff) #encrypts file in AES-256 using pyAesCrypt module
    print('   ***file encrypted***')
    os.system('rm -rf enc.zip')
    print('')
#uses the given key to decrypt a file with the given filename

def dec(key,buff):
    print('')
    fi=input('filename>')
    print('')
    print('   ***reading file data...***')
    if key=='false':
        os.system('rm -rf %s'%fi)
        print('')
        time.sleep(0.1)
        print('       ***file erased***')
        sys.exit()
    time.sleep(0.2)
    print('')
    print('***initializing Fernet key...***')
    time.sleep(0.35)
    print('')
    print('    ***decrypting data...***')
    pyAesCrypt.decryptFile(fi,fi.replace('.enc','.zip'),key,buff) #decrypts file in AES-256 using pyAesCrypt
    os.system('rm -rf %s'%fi)
    os.system('unzip %s'%fi.replace('.enc','')) #decompresses zip file into folder
    print('      ***file decrypted***')
    os.system('rm -rf %s'%fi.replace('.enc','.zip'))
    
#run main part of code
while True:
    c=input(intr)
    if c=='1':
        enc(key(),buff)
    elif c=='encrypt':
        enc(key(),buff)
    elif c=='2':
        dec(key(),buff)
    elif c=='decrypt':
        dec(key(),buff)
    elif c=='99':
        break
    elif c=='exit':
        break
    else:
        print('input a number shown')
