echo updating apt.apt-get
sudo apt-get update

echo installing python3
sudo apt-get install python3

echo installing pip3
sudo apt-get install python3-pip

echo installing adafruit neopixel ws2812-library
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka

echo installing stupidArtnet
sudo pip3 install stupidArtnet

echo installing unzip
sudo apt-get unzip

echo downloading repo
wget https://github.com/Xilef12000/ws2812-over-artnet/archive/refs/tags/v1.0.zip

echo unzipping
unzip v1.0.zip

echo cleanup
cd ws2812-over-artnet-1.0
mv * ../
rm .gitignore
cd ../
rmdir ws2812-over-artnet-1.0
rm v1.0.zip

echo installation complete