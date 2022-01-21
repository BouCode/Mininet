import os

def mininet ():
    print ('Instalando mininet')
    os.system('sudo apt update')
    os.system('sudo apt install git -y')
    os.system('git clone git://github.com/mininet/mininet')
    os.system('cd mininet && git checkout -b mininet-2.3.0 2.3.0')
    os.system('cd mininet/util && ./install.sh')
    os.system('sudo mn --switch ovsbr --test pingall')

def opendaylight (): 
    print ('Opendaylight')
    os.system('sudo apt -y install openjdk -8-jre')
    os.system('sudo update-alternatives --config java')
    os.system("sudo bash -c \'echo JAVA_HOME=\"/usr/lib/jvm/java-8-openjdk-amd64/jre\"\ >> /etc/environment && source /etc/environment'")
    os.system('mkdir opendaylight && cd opendaylight && wget https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.3/karaf-0.8.3.tar.gz && tar -zxvf karaf-0.8.3.tar.gz')
    os.system('cd opendaylight/karaf-0.8.3/bin && sudo ./karaf')

def ryu ():
    print ('Ryu')
    os.system('sudo git clone git://github.com/osrg/ryu.git')
    os.system('sudo apt install python3-pip')
    os.system('cd ryu && sudo pip3 install ryu')
    os.system('cd ryu/app && sudo pip3 install eventlet==0.30.2')
    os.system('sudo git clone https://github.com/martimy/flowmanager')
    
def onos ():
    print ('Instalando ONOS')

if __name__ == '__main__':
    mininet()
