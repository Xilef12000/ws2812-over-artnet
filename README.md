# ws2812-over-artnet
## ws2812 over artnet with a raspberrypi


open
```bash
sudo nano /etc/modprobe.d/snd-blacklist.conf
```
and add
```
blacklist snd_bcm2835
```

open
```bash
sudo nano /boot/config.txt
```
and change
```
# Enable audio (loads snd_bcm2835)
dtparam=audio=on
```
to
```
# Enable audio (loads snd_bcm2835)
#dtparam=audio=on
```
reboot using
```bash
sudo reboot
```

update apt-get and install pip3:
```bash
sudo apt-get update
sudo apt-get install python3-pip
```

install the following python modules:
```bash
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
sudo pip3 install stupidArtnet
```