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
chmod +x enc.py
ENC="alias pycrypt='python3 ${PWD}/enc.py'"
echo $ENC>>~/.bashrc
echo $ENC>>~/.zshrc
echo $ENC>>~/.zprofile
