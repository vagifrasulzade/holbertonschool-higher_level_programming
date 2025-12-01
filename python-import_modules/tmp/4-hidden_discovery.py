#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for i in names:
        if i[:2] != "__":
            print(i)





#example
# Linux 
# mkdir /tmp
# cd /tmp
# curl -Lso hidden_4.pyc "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
