import os
import argparse

def detect_distro():
    """Detect the Linux distribution"""
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('ID='):
                    distro = line.strip().split('=')[1].strip('"')
                    return distro
    except FileNotFoundError:
        pass
    return 'unknown'

distro = detect_distro()
print(f"Detected distribution: {distro}")

parser = argparse.ArgumentParser(description="Installation parameters")
parser.add_argument(
    "--UI",
    type=str,
    required=True,
    help="Should the installation procedure include GUI applications? (GUI || headless)",
)

parser.add_argument(
    "--other_tools",
    type=str,
    required=False,
    help="By default only development tools are installed, should other non dev programs (like Discord) be also installed? (yes || no)",
)
args = parser.parse_args()
print(args)


# With GUI
list_of_programs_with_gui_apt = [
    "sudo apt-get install tilix -y",
]

list_of_programs_with_gui_snap = [
    "sudo snap install code --classic",
    "sudo snap install alacritty --classic",
]

# Gentoo GUI packages
list_of_programs_with_gui_gentoo = [
    "sudo emerge --ask=n x11-terms/tilix",
    "sudo emerge --ask=n app-editors/vscode",
    "sudo emerge --ask=n x11-terms/alacritty",
]

# Without GUI
list_of_programs_without_gui_apt = [
    "sudo apt-get install neovim -y",
    "sudo apt-get install ranger -y",
    "sudo apt-get install neofetch -y",
    "sudo apt-get install tmux -y",
    "sudo apt-get install gcc g++ -y",
    "sudo apt-get install clang clangd -y",
    "sudo apt-get install cmake -y",
    "sudo apt-get install gdb -y",
    "sudo apt-get install pipx -y",
    # System administration tools
    "sudo apt-get install htop btop iotop -y",
    "sudo apt-get install ncdu tree -y",
    "sudo apt-get install lsof strace -y",
    "sudo apt-get install rsync unzip zip -y",
    # Network tools
    "sudo apt-get install curl wget -y",
    "sudo apt-get install jq gnupg -y",  # Required for tofuenv
    "sudo apt-get install nmap netcat-openbsd -y",
    "sudo apt-get install dnsutils iputils-ping -y",
    "sudo apt-get install traceroute mtr-tiny -y",
    "sudo apt-get install tcpdump wireshark-common -y",
    # Disk and filesystem tools
    "sudo apt-get install smartmontools -y",
    "sudo apt-get install parted gparted -y",
    "sudo apt-get install hdparm -y",
]

# Gentoo headless packages
list_of_programs_without_gui_gentoo = [
    "sudo emerge --ask=n app-editors/neovim app-misc/ranger app-misc/neofetch app-misc/tmux",
    "sudo emerge --ask=n sys-devel/gcc sys-devel/clang sys-devel/clang-runtime dev-util/cmake sys-devel/gdb dev-python/pipx",
    # System administration tools
    "sudo emerge --ask=n sys-process/htop sys-process/btop sys-process/iotop sys-fs/ncdu app-text/tree",
    "sudo emerge --ask=n sys-process/lsof dev-util/strace",
    "sudo emerge --ask=n net-misc/rsync app-arch/unzip app-arch/zip",
    # Network tools
    "sudo emerge --ask=n net-misc/curl net-misc/wget app-misc/jq app-crypt/gnupg net-analyzer/nmap",
    "sudo emerge --ask=n net-analyzer/netcat net-dns/bind-tools net-misc/iputils",
    "sudo emerge --ask=n net-analyzer/traceroute net-analyzer/mtr net-analyzer/tcpdump net-analyzer/wireshark",
    # Disk and filesystem tools
    "sudo emerge --ask=n sys-apps/smartmontools sys-block/parted sys-block/gparted sys-apps/hdparm",
]

list_of_programs_without_gui_cargo = [
    "cargo install eza",
    "cargo install bat",
    "cargo install hx",
    "cargo install tokei",
    "cargo install du-dust",
    "cargo install rm-improved",
    "cargo install bottom",
    "cargo install mcfly",
    
]

# Ensure we have git and basic build tools (in case running from fresh Ubuntu or Gentoo)
if distro == 'gentoo':
    # Gentoo-specific initialization
    os.system("sudo emerge --sync")
    os.system("sudo emerge --ask=n sys-devel/gcc sys-devel/make dev-vcs/git dev-lang/python")
    # Development libraries
    os.system(
        "sudo emerge --ask=n dev-libs/openssl sys-libs/zlib \
app-arch/bzip2 sys-libs/readline dev-db/sqlite net-misc/wget net-misc/curl \
sys-devel/llvm sys-libs/ncurses app-arch/xz-utils dev-lang/tk \
dev-libs/libxml2 dev-libs/xmlsec dev-libs/libffi"
    )
else:
    # Ubuntu/Debian initialization (original code)
    os.system("sudo apt-get update && sudo apt-get upgrade -y")
    os.system("sudo apt-get install build-essential git python3 -y")
    # Other useful libraries that will comein handy at some point anyway:
    os.system(
        "sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y"
    )


# Install and configure ZSH

if distro == 'gentoo':
    os.system("sudo emerge --ask=n app-shells/zsh")
else:
    os.system("sudo apt-get install zsh -y")

os.system("sudo chsh -s $(which zsh) $USER")
os.system(
    r'sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" &'
)


# Install and configure useful command line tools


# Install and configure terminal theming/powerlevel10k etc
if distro == 'gentoo':
    os.system("sudo emerge --ask=n media-fonts/powerline-fonts")
else:
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

# Install Starship prompt
os.system(r"curl -sS https://starship.rs/install.sh | sh -s -- -y")

# Install uv (Python package manager)
os.system(r"curl -LsSf https://astral.sh/uv/install.sh | sh")

# Install Python versions via uv
os.system(r". $HOME/.cargo/env && $HOME/.cargo/bin/uv python install 3.11 3.12 3.13 --default")


os.system(r"curl https://sh.rustup.rs -sSf | sh -s -- -y")
## one of them should work
#os.system(r". $HOME/.cargo/env")

# Install Homebrew
os.system(r'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

# Install version managers

# SDKMAN (for Java, Kotlin, Scala, etc.)
os.system(r'curl -s "https://get.sdkman.io" | bash')

# GVM (Go Version Manager)
os.system(r'bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)')

# NVM (Node Version Manager) - using Homebrew
os.system(r'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && brew install nvm')

# Install essential tools via Homebrew (only what's not managed by version managers)
homebrew_packages = [
    "jq",    # JSON processor (also installed via apt for tofuenv)
    "fd",    # Alternative to find
    "ripgrep",  # Alternative to grep
    "fzf",   # Fuzzy finder
    "yq",    # YAML processor
    "bandwhich", # Network utilization monitor
    "procs",  # Modern ps replacement
]

for package in homebrew_packages:
    os.system(f'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && brew install {package}')

# Install tofuenv (OpenTofu version manager) via Homebrew
os.system(r'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && brew tap tofuutils/tap && brew install tofuenv')

# VERSION MANAGERS INSTALLED:
# - SDKMAN: Java, Kotlin, Scala, Groovy, etc. (installed above)
# - GVM: Go Version Manager (installed above)
# - NVM: Node Version Manager (installed above)
# - HVM: Hugo Version Manager (installed above)
# - tofuenv: OpenTofu Version Manager (installed above)
# - UV: Python Version Manager (installed above)

# HVM (Hugo Version Manager)
os.system(r'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && go install github.com/jmooring/hvm@latest')

# Generate HVM alias for zsh (will be added at the end when zshrc is copied)
# Note: This will be handled after .zshrc is copied to avoid conflicts

# Install useful programs

# Distro neutral

for each in list_of_programs_without_gui_cargo:
    os.system(r". $HOME/.cargo/env && " + each)

if args.UI == "GUI":
    if distro == 'gentoo':
        # Install Gentoo GUI packages
        for each in list_of_programs_with_gui_gentoo:
            os.system(each)
    else:
        # Install Ubuntu/Debian GUI packages (original code)
        for each in list_of_programs_with_gui_snap:
            os.system(each)

# Distro specific
if args.UI == "GUI":
    if distro == 'gentoo':
        pass  # Already handled above
    else:
        # Ubuntu/Debian (original code)
        for each in list_of_programs_with_gui_apt:
            os.system(each)

if distro == 'gentoo':
    # Install Gentoo headless packages
    for each in list_of_programs_without_gui_gentoo:
        os.system(each)
else:
    # Ubuntu/Debian (original code)
    for each in list_of_programs_without_gui_apt:
        os.system(each)


# PYENV removed - using uv for Python management instead

# ZSHRC
os.system("cp ./.zshrc ~/.zshrc")

# TMUX CONFIG
os.system("cp ./.tmux.conf ~/.tmux.conf")

# NEOVIM CONFIG
os.system("mkdir -p ~/.config/nvim")
os.system("cp ./init.lua ~/.config/nvim/init.lua")

# ALACRITTY CONFIG (if GUI mode)
if args.UI == "GUI":
    os.system("mkdir -p ~/.config/alacritty")
    os.system("cp ./alacritty.toml ~/.config/alacritty/alacritty.toml")

# Generate HVM alias and add to zshrc
os.system(r'echo "" >> ~/.zshrc')
os.system(r'echo "# HVM (Hugo Version Manager) alias" >> ~/.zshrc')
os.system(r'$HOME/go/bin/hvm gen alias zsh >> ~/.zshrc')

# NERD FONTS
# os.system(r"git clone https://github.com/ryanoasis/nerd-fonts.git && cd ./nerd-fonts && ./install.sh")
# MesloLGL Nerd Font Regular

# my-shell-config removed - everything consolidated into .zshrc

# NERD FONTS - Install FiraCode Nerd Font for Alacritty
if args.UI == "GUI":
    if distro == 'gentoo':
        # On Gentoo, we can use emerge or manual installation
        os.system("sudo emerge --ask=n media-fonts/firacode")
        # Also install nerd-fonts version manually for full support
        os.system("mkdir -p ~/.local/share/fonts")
        os.system("wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip")
        os.system("cd ~/.local/share/fonts && unzip -o FiraCode.zip && rm FiraCode.zip")
        os.system("fc-cache -fv")
    else:
        os.system("mkdir -p ~/.local/share/fonts")
        os.system("wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip")
        os.system("cd ~/.local/share/fonts && unzip -o FiraCode.zip && rm FiraCode.zip")
        os.system("fc-cache -fv")

print("Installation completed! Please restart your shell or run 'source ~/.zshrc' to apply changes.")
print("Don't forget to:")
print("- Install a specific OpenTofu version: tofuenv use latest")
print("- Install Python versions: uv python install 3.12")
print("- Generate HVM alias: $HOME/go/bin/hvm gen alias zsh >> ~/.zshrc")
if args.UI == "GUI":
    print("- FiraCode Nerd Font installed for Alacritty")
