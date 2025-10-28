# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#   source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME='powerlevel10k/powerlevel10k'  # Disabled in favor of Starship

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    colored-man-pages
    colorize
    pip
    vi-mode
    python
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
# my-shell-config removed - everything consolidated here

# Environment variables
export EDITOR=nvim
export GPG_TTY=$(tty)
export NVM_DIR="$HOME/.nvm"

# Homebrew
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# Starship prompt
eval "$(starship init zsh)"

# NVM
[ -s "$(brew --prefix nvm)/nvm.sh" ] && \. "$(brew --prefix nvm)/nvm.sh"

# GVM (Go Version Manager)
[[ -s "/home/janbronicki/.gvm/scripts/gvm" ]] && source "/home/janbronicki/.gvm/scripts/gvm"

# Add Go bin to PATH (for tools like hvm)
export PATH="$HOME/go/bin:$PATH"

# tofuenv (OpenTofu version manager) - installed via Homebrew
# No additional PATH needed, managed by Homebrew

# NVM setup for Homebrew installation
[ -s "$(brew --prefix)/opt/nvm/nvm.sh" ] && \. "$(brew --prefix)/opt/nvm/nvm.sh"
[ -s "$(brew --prefix)/opt/nvm/etc/bash_completion.d/nvm" ] && \. "$(brew --prefix)/opt/nvm/etc/bash_completion.d/nvm"

# SDKMAN - THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"

# Aliases
alias cat='bat'

# --- eza (formerly exa) aliases ---
alias ls='eza -F --group-directories-first --icons'
alias l='eza --tree -L 1 -l --git --icons --group-directories-first --color=always'
alias ll='eza --tree -L 2 -l --git --icons --group-directories-first --color=always'
alias lll='eza --tree -L 3 -l --git --icons --group-directories-first --color=always'

alias la='l -a'
alias lla='ll -a'
alias llla='lll -a'
alias t='eza --tree -a -l --git --icons --group-directories-first --color=always'

alias tree='eza --tree -a -l --git --icons --group-directories-first --color=always'

# Python management via uv (replaces pyenv)
# uv manages Python versions and virtual environments

# Mcfly history search
eval "$(mcfly init zsh)"

# Local bin path
export PATH="$HOME/.local/bin:$PATH"

# UV (Python package manager) path
export PATH="$HOME/.cargo/bin:$PATH"

# Pipx path
export PATH="$HOME/.local/bin:$PATH"

# Local environment
[ -f "$HOME/.local/bin/env" ] && . "$HOME/.local/bin/env"

# ============= ALIASES =============
# Basic shell aliases
alias s='source'
alias sz='s ~/.zshrc'
alias oldcat='/bin/cat'

# Git aliases
alias gcr='git clone --recursive'

# Python development aliases
alias stdpipinstall='pip install -U pip && pip install ipython pytest black black[jupyter] flake8 pynvim matplotlib numpy pandas jupyterlab isort'
alias flint="isort . -l 88 && black . --line-length 88 && flake8 . --max-line-length 88 --exclude gti-bootstrap.py,'./venv*'"
alias pipinstallflint='pip install isort black flake8 black black[jupyter]'
alias wp='which python'
alias sa='source ./venv/bin/activate'
alias stdvenvsetup='python -m venv venv && sa && echo "Using: $(wp)" && stdpipinstall && pipinstallflint'

# UV Python management aliases
alias uvenv='uv venv'  # Create virtual environment with uv
alias uvact='source .venv/bin/activate'  # Activate uv virtual environment
alias uvrun='uv run'   # Run command in uv environment
alias uvinstall='uv add'  # Install packages with uv
alias uvpython='uv python'  # Manage Python versions

# System monitoring aliases
alias top='btop'        # Better top
alias disk='ncdu'       # Disk usage analyzer
alias ports='lsof -i'   # Show open ports
alias proc='procs'      # Modern ps replacement
alias net='bandwhich'   # Network usage monitor

# tofuenv (OpenTofu version manager) aliases
alias tflist='tofuenv list'          # List installed OpenTofu versions
alias tfuse='tofuenv use'            # Use specific OpenTofu version

# Pipx aliases
alias pxinstall='pipx install'       # Install Python apps globally
alias pxlist='pipx list'             # List installed pipx apps
alias pxupgrade='pipx upgrade-all'   # Upgrade all pipx apps
