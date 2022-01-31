echo updating apt.apt-get
sudo apt-get update

echoinstalling pip3
sudo apt-get install python3-pip

echo installing adafruit-neopixel (ws2812-library)
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka

echo installing stupidArtnet
sudo pip3 install stupidArtnet


echo instalation complete