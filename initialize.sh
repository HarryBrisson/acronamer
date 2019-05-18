
sudo apt-get update

sudo apt-get -y install python3-pip
sudo python3 -m pip install virtualenv

virtualenv .env
source .env/bin/activate

sudo python3 -m pip install -r requirements.txt
aws configure

zappa deploy dev