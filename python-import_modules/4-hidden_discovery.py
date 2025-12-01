#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
#terminal
# curl -Lso "hidden_4.pyc" "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"