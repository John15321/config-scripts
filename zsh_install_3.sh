#!/usr/bin/zsh

echo "Installing powerlevel10k themes:"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

echo "ZSH_THEME='powerlevel10k/powerlevel10k'" >> ~/.zshrc

echo "Innstalling fonts:"

sudo apt install fonts-powerline -y


# powerline10k configure