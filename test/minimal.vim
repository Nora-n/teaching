set nocompatible
set number                  " add line numbers
set relativenumber          " show line number relatively to current
set cc=80                   " set an 80 column border for good coding style
set wrap                    " automatic wrap
set tw=80                   " autowrap at border
let &runtimepath  = '~/.config/nvim/plugged/vimtex,' . &runtimepath
let &runtimepath .= ',~/.config/nvim/plugged/vimtex/after'
filetype plugin indent on
syntax enable
" Add relevant options and VimTeX configuration below.

call plug#begin('~/.config/nvim/plugged')

Plug 'lervag/vimtex'

call plug#end()

fun! TeX_fmt()
    if (getline(".") != "")
    let save_cursor = getpos(".")
        let op_wrapscan = &wrapscan
        set nowrapscan
        let par_begin = '^\(%D\)\=\s*\($\|\\begin\|\\end\|\\\[\|\\\]\|\\\(sub\)*section\>\|\\item\>\|\\bitem\>\|\\clitem\>\|\\sqlitem\>\|\\nitem\>\|\\NC\>\|\\blank\>\|\\noindent\>\|\\smallbreak\>\|\\bigbreak\>\|\\label\>\|\\hfill\>\|\\tcblower\>\|\\tcbsubtitle\|\\cswitch\>\)'
        let par_end   = '^\(%D\)\=\s*\($\|\\begin\|\\end\|\\\]\|\\\[\|\\place\|\\\(sub\)*section\>\|\\item\>\|\\bitem\>\|\\clitem\>\|\\sqlitem\>\|\\nitem\>\|\\NC\>\|\\blank\>\|\\smallbreak\>\|\\bigbreak\>\|\\label\>\|\\hfill\>\|\\tcblower\>\|\\tcbsubtitle\|\\cswitch\>\)'
    try
      exe '?'.par_begin.'?+'
    catch /E384/
      1
    endtry
        norm V
    try
      exe '/'.par_end.'/-'
    catch /E385/
      $
    endtry
    norm gq
        let &wrapscan = op_wrapscan
    call setpos('.', save_cursor)
    endif
endfun

nmap Q :call TeX_fmt()<CR>

