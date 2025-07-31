#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src
else
  echo "...Using Chrome from cache"
fi

if [[ ! -f $STORAGE_DIR/chromedriver/chromedriver ]]; then
  echo "...Downloading Chromedriver"
  mkdir -p $STORAGE_DIR/chromedriver
  cd $STORAGE_DIR/chromedriver
  wget https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.183/linux64/chromedriver-linux64.zip
  unzip chromedriver-linux64.zip
  mv chromedriver-linux64/chromedriver .
  rm -r chromedriver-linux64 chromedriver-linux64.zip
else
  echo "...Using cached Chromedriver"
fi

cd $HOME/project/src
$STORAGE_DIR/chrome/opt/google/chrome/google-chrome --version
