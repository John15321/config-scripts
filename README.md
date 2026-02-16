# config-scripts
config-scripts

Multi-distribution configuration scripts for setting up a development environment.

## Supported Distributions
- Ubuntu/Debian (apt-get)
- Gentoo (emerge)

## Installation

### Ubuntu/Debian One-liner:

```bash
sudo apt-get update && sudo apt-get install git -y && git clone https://github.com/John15321/config-scripts.git && cd ./config-scripts && python3 ./install.py --UI no || python ./install.py --UI no
```

### Gentoo One-liner:

```bash
sudo emerge --sync && sudo emerge --ask=n dev-vcs/git && git clone https://github.com/John15321/config-scripts.git && cd ./config-scripts && python3 ./install.py --UI no
```

### Manual Installation:

1. Clone the repository:
```bash
git clone https://github.com/John15321/config-scripts.git
cd config-scripts
```

2. Run the installer:
```bash
# For headless installation (no GUI apps)
python3 ./install.py --UI no

# For GUI installation (includes GUI apps)
python3 ./install.py --UI GUI
```

## What Gets Installed

The script automatically detects your distribution and installs:
- Development tools (compilers, debuggers, build systems)
- System administration utilities (htop, btop, ncdu, etc.)
- Network tools (curl, wget, nmap, etc.)
- Terminal environment (zsh, oh-my-zsh, powerlevel10k, starship)
- Version managers (rustup, uv, nvm, sdkman, gvm, tofuenv)
- Configuration files (.zshrc, .tmux.conf, neovim config, alacritty config)

