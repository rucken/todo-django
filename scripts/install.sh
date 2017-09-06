wget https://raw.githubusercontent.com/creationix/nvm/v0.31.0/nvm.sh -O ~/.nvm/nvm.sh
source ~/.nvm/nvm.sh
nvm install 6
node --version
add-apt-repository ppa:git-core/ppa -y
apt-get update
apt-get install git -y
pip install --upgrade pip
pip install -r requirements.txt
cd frontend
npm install