import os

def mininet ():
    print ('Bienvenidos al instalador de mininet')
    os.system('sudo apt update')
    print ('Instalando git ...')
    os.system('sudo apt install git -y')
    os.system('git clone git://github.com/mininet/mininet')
    os.system('cd mininet && git checkout -b mininet-2.3.0 2.3.0')
    os.system('cd mininet/util && ./install.sh')
    os.system('sudo mn --switch ovsbr --test pingall')
=
if __name__ == '__main__':
    mininet()
