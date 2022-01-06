# ws2812-over-artnet
## ws2812 over artnet with a raspberrypi

## Setup:
0. **?????**
1. Connect the ws2812-Strip to the raspberry pi.  
	**??????**
2. This is an optional step to improve the communication with the ws2812 LED-Strip  
	(This step is not necessary, and can also be done later)  
	1. open the file:  
		```bash
		sudo nano /etc/modprobe.d/snd-blacklist.conf
		```
	2. and add:  
		```
		blacklist snd_bcm2835
		```
		save and exit with Ctrl + O and Ctrl + X  
	3. open the next file:  
		```bash
		sudo nano /boot/config.txt
		```
	4. and change:  
		```
		# Enable audio (loads snd_bcm2835)
		dtparam=audio=on
		```
		to:  
		```
		# Enable audio (loads snd_bcm2835)
		#dtparam=audio=on
		```
		save and exit with Ctrl + O and Ctrl + X  
	5. reboot the Raspberry pi using:  
		```bash
		sudo reboot
		```
3. Update apt-get and install pip3:  
	```bash
	sudo apt-get update
	sudo apt-get install python3-pip
	```
4. Install the following python modules:  
	```bash
	sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
	sudo python3 -m pip install --force-reinstall adafruit-blinka
	sudo pip3 install stupidArtnet
	```
	(And Yes, the libraries need to be installed in the Root-directory, more on that later)  

5. Copy the python files from the repo on your pi.  
	By either using **??????????**  
	Or by following **???these???** Instructions.

6. Set the number of pixels.  
	1. Set the number of pixels.  
	2. Set the Artnet Universe number.  
	**????????**  

7. Test the ws2812-Strip:
	```bash
	sudo python3 ws2812.py
	```
	(It is important to run the script with Root-privileges, so that it can access the pwm-function)  
	The first LED should light up in red, and the last one in blue, all in between should light up in green.  

	Debug:  
	- If no LEDs lights up, but there is no error message in the shell, check the wiring  
	- If the LEDs do not light up in the correct colour, but there is no error message in the shell, check the number of LEDs set in step 6 and/or do step 2.  
	- If you get an error message check the sudo privileges, the number of LEDs set in step 6, and/or do step 2.  

8. Check the Artnet-Network:
	1. Setup your DMX software.  
		(I used QLC+, for a tutorial how to set up QLC+ go [here](#qlc-artnet-setup))  
		If you need the IP-Address of the Raspberry pi use:
		```bash
		hostname -I
		```
	2. start the Artnet-test-script:
		```bash
		sudo python3 artnet.py
		```
		(Sudo must be used, because the library is installed in the Root-directory, to later function in combination with the ws2812-module)  

		Debug:  
		- **??????**  
	3. stop the script, by pressing any key  

9. Test the ws2818 over Artnet scipt:  
	```bash
	sudo python3 ws2812Artnet.py

	```
	stop it with Ctrl + C (the script will then crash with an error message, which can be ignored)  

10. Setup the auto-startup of the script:  
	**??????**  

11. Setup a shutdown button:  
	**??????**  


## Additional Stuff:
### QLC+ Artnet Setup:
**??????**