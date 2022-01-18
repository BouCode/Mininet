import os

def mininet ():
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
    os.system("sudo bash -c \'echo JAVA_HOME=\"/usr/lib/jvm/java-8-openjdk-amd64/jre\"\'")
    os.system("source /etc/environment")
    os.system('mkdir opendaylight && cd opendaylight && wget https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.3/karaf-0.8.3.tar.gz && tar -zxvf karaf-0.8.3.tar.gz')
    os.system('cd opendaylight/karaf-0.8.3/bin && sudo ./karaf')



if __name__ == '__main__':
    opendaylight()
