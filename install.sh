#!/bin/sh
clear
echo '
     <Tsociety file encryptor>
     <made by themobilehacker>
               ___
              |   |
             _|___|_
            /#######\ 
           |-+-###-+-|
           |#########|
            \#\___/#/
             \#####/
'
echo 'installing pycrypt...'
cp enc.py ~/.pycrypt
ENC="alias pycrypt='python3 ~/.pycrypt/enc.py'"
echo $ENC>>~/.bashrc
echo $ENC>>~/.zshrc
echo $ENC>>~/.zprofile
echo 'pycrypt installed.'
echo 'run by typing pycrypt -e or -d [directory]'
