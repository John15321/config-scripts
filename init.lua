-- ~/.config/nvim/init.lua
-- Basic Neovim configuration with terminal pane navigation

-- Basic settings
vim.opt.number = true
vim.opt.relativenumber = false
vim.opt.expandtab = true
vim.opt.shiftwidth = 2
vim.opt.tabstop = 2
vim.opt.smartindent = true
vim.opt.wrap = false
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.incsearch = true
vim.opt.hlsearch = true
vim.opt.scrolloff = 8
vim.opt.signcolumn = "yes"
vim.opt.termguicolors = true

-- Set leader key
vim.g.mapleader = " "

-- Terminal settings
vim.opt.shell = "/bin/zsh"

-- Key mappings for pane navigation (works in terminal mode too)
local keymap = vim.keymap

-- Normal mode pane navigation
keymap.set("n", "<C-h>", "<C-w>h", { desc = "Go to left window" })
keymap.set("n", "<C-j>", "<C-w>j", { desc = "Go to lower window" })
keymap.set("n", "<C-k>", "<C-w>k", { desc = "Go to upper window" })
keymap.set("n", "<C-l>", "<C-w>l", { desc = "Go to right window" })

-- Terminal mode pane navigation (essential for :terminal)
keymap.set("t", "<C-h>", "<C-\\><C-N><C-w>h", { desc = "Go to left window from terminal" })
keymap.set("t", "<C-j>", "<C-\\><C-N><C-w>j", { desc = "Go to lower window from terminal" })
keymap.set("t", "<C-k>", "<C-\\><C-N><C-w>k", { desc = "Go to upper window from terminal" })
keymap.set("t", "<C-l>", "<C-\\><C-N><C-w>l", { desc = "Go to right window from terminal" })

-- Easy escape from terminal mode
keymap.set("t", "<Esc>", "<C-\\><C-n>", { desc = "Exit terminal mode" })

-- Window management
keymap.set("n", "<leader>sv", "<C-w>v", { desc = "Split window vertically" })
keymap.set("n", "<leader>sh", "<C-w>s", { desc = "Split window horizontally" })
keymap.set("n", "<leader>se", "<C-w>=", { desc = "Make splits equal size" })
keymap.set("n", "<leader>sx", "<cmd>close<CR>", { desc = "Close current split" })

-- Terminal shortcuts
keymap.set("n", "<leader>th", "<cmd>split | terminal<CR>", { desc = "Open terminal horizontally" })
keymap.set("n", "<leader>tv", "<cmd>vsplit | terminal<CR>", { desc = "Open terminal vertically" })
keymap.set("n", "<leader>tt", "<cmd>terminal<CR>", { desc = "Open terminal in current buffer" })

-- Better copy/paste
keymap.set("v", "<leader>y", '"+y', { desc = "Copy to system clipboard" })
keymap.set("n", "<leader>p", '"+p', { desc = "Paste from system clipboard" })

-- Clear search highlights
keymap.set("n", "<leader>nh", ":nohl<CR>", { desc = "Clear search highlights" })

-- Basic file operations
keymap.set("n", "<leader>w", "<cmd>w<CR>", { desc = "Save file" })
keymap.set("n", "<leader>q", "<cmd>q<CR>", { desc = "Quit" })

-- Auto-enter insert mode when entering terminal
vim.api.nvim_create_autocmd("TermOpen", {
  group = vim.api.nvim_create_augroup("custom-term-open", { clear = true }),
  callback = function()
    vim.opt.number = false
    vim.opt.relativenumber = false
    vim.cmd("startinsert")
  end,
})

-- Auto-enter insert mode when focusing terminal
vim.api.nvim_create_autocmd("BufEnter", {
  group = vim.api.nvim_create_augroup("custom-term-enter", { clear = true }),
  pattern = "term://*",
  callback = function()
    vim.cmd("startinsert")
  end,
})