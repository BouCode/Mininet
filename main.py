import os

def mininet ():
    print ('Bienvenidos al instalador de mininet')
    os.system('sudo apt update')
    os.system('sudo apt install git -y')
    os.system('git clone git://github.com/mininet/mininet && cd mininet')
    os.system('git checkout -b mininet-2.3.0 2.3.0')
    os.system('cd util')
    os.system('./install.sh')
    os.system('mn --switch ovsbr --test pingall')

    
if __name__ == '__main__':
    mininet()

