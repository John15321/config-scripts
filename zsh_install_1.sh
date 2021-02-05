#!/bin/bash

echo  "Updating the system:"
sudo apt update -y && sudo apt upgrade -y

echo "Installing ZSH:"

sudo apt-get install zsh -y

echo "Installed ZSH version:"
zsh --version


echo "Setting ZSH as default shell:"
chsh -s $(which zsh)

echo -e "\n\n\n"
echo "Please log out/reboot for changes to take effect!"
echo "Then you need to run the second part of this script."

WHADUP="When opening a terminal after a reboot/log out you will
be promped with a screen where you will be configuring your ZSH.\n\n
If you dont know what to choose, choose (2), which pupulates ~/.zshrc 
with default settings.\n\n"
echo -e $WHADUP