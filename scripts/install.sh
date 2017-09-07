wget https://raw.githubusercontent.com/creationix/nvm/v0.31.0/nvm.sh -O ~/.nvm/nvm.sh
source ~/.nvm/nvm.sh
nvm install 6
node --version
pip install -r requirements.txt
cd frontend
npm install
cd ..