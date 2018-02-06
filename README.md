# LoginComputerBluetooth
This is a small code for logging in linux system wityh just turning your bluetooth ON in your mobile or any other device

**Note: Works only on UNIX based system which has PAM Modules**

# Installing Instruction (Ubuntu)
1. sudo apt-get install libpam-python bluetooth libbluetooth-dev gobject
1. sudo pip install pybluez
1. Edit /etc/pam.d/common-auth and enter following line in the top of the file
  auth  sufficient  pam_python.so /path/to/pam.py

Now turn on bluetooth on your device and test it by opening a terminal and typing **sudo -i**

# TODO
1. Make a database so that DEVICE ID should not be hardcoded in the code
1. Add a GUI for entering device ID to make it more user friendly
