apt-get autoremove nodejs -y
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
apt-get install -y nodejs
apt-get install npm -y
node --version
pip install -r requirements.txt
npm install --prefix ./frontend