#!/bin/bash
yum -y install patch zlib-devel libffi-devel openssl-devel readline-devel sqlite-devel
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv install 3.5.0
pyenv install 2.7
mkdir -p ~/task1/2.7 ~/task1/3.5
cd ~/task1/2.7
git init
pyenv local 2.7
mkdir venv && echo "Virtualenv directory" > venv/README
git add venv && echo "/venv/" >> .gitignore && git add -f .gitignore
virtualenv --no-site-packages --prompt="(2.7)" 2.7

cd ~/task1/3.5
git init
pyenv local 3.5.0
mkdir venv && echo "Virtualenv directory" > venv/README
git add venv && echo "/venv/" >> .gitignore && git add -f .gitignore
virtualenv --no-site-packages --prompt="(3.5)" 3.5.0


