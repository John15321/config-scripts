import argparse
import os
from ast import arg

parser = argparse.ArgumentParser(description="Installation parameters")
parser.add_argument(
    "--UI",
    type=bool,
    required=False,
    default=False,
    help="Should the installation procedure include GUI applications? (GUI || headless)",
)

parser.add_argument(
    "--add_config",
    type=bool,
    required=False,
    default=True,
    help="Do you want to add my-shell-config to your system?",
)

parser.add_argument(
    "--other_tools",
    type=bool,
    default=False,
    required=False,
    help="By default only development tools are installed, should other non dev programs (like Discord) be also installed? (yes || no)",
)

parser.add_argument(
    "--install_nf",
    type=bool,
    default=False,
    required=False,
    help="Do you want to install all nerd fonts?",
)
args = parser.parse_args()
print(args)


# With GUI
list_of_programs_with_gui_apt = [
    "sudo apt-get install tilix -y",
]

list_of_programs_with_gui_snap = [
    "sudo snap install code --classic",
]

# Without GUI
list_of_programs_without_gui_apt = [
    "sudo apt-get install neovim -y",
    "sudo apt-get install ranger -y",
    "sudo apt-get install neofetch -y",
]

list_of_programs_without_gui_cargo = [
    "cargo install exa",
    "cargo install bat",
    "cargo install hx",
    "cargo install tokei",
    "cargo install du-dust",
    "cargo install rm-improved",
    "cargo install bottom",
]

os.system("sudo apt-get update && sudo apt-get upgrade -y")
os.system("sudo apt-get install build-essential git -y")
# Other useful libraries that will comein handy at some point anyway:
os.system(
    "sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y"
)


# Install and configure ZSH

os.system("sudo apt-get install zsh -y")
os.system("sudo chsh -s $(which zsh) $USER")
os.system(
    r'sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" &'
)


# Install and configure useful command line tools


# Install and configure terminal theming/powerlevel10k etc
os.system("sudo apt-get install fonts-powerline -y")
os.system(
    r"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
)
os.system(
    r"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
)
os.system(
    r"git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
)


os.system(r"curl https://sh.rustup.rs -sSf | sh -s -- -y")
## one of them should work
# os.system(r". $HOME/.cargo/env")
# Install useful programs

# Distro neutral

for each in list_of_programs_without_gui_cargo:
    os.system(r". $HOME/.cargo/env && " + each)

if args.UI:
    for each in list_of_programs_with_gui_snap:
        os.system(each)

# Distro specific
if args.UI:
    for each in list_of_programs_with_gui_apt:
        os.system(each)
for each in list_of_programs_without_gui_apt:
    os.system(each)


# PYENV
os.system(r"git clone https://github.com/pyenv/pyenv.git ~/.pyenv")

# ZSHRC
os.system("cp ./.zshrc ~/.zshrc")

# NERD FONTS
if args.install_nf:
    os.system(
        r"git clone https://github.com/ryanoasis/nerd-fonts.git && cd ./nerd-fonts && ./install.sh"
    )
# MesloLGL Nerd Font Regular

if args.add_config:
    os.system(
        r"git clone https://github.com/John15321/my-shell-config.git $USER/.my-shell-config"
    )
