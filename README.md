PionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl
so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/Enseignement/Prepa/2023/07_DS/DS07
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
  endif
  let s:shortmess_save = &shortmess
  if &shortmess =~ 'A'
    set shortmess=aoOA
    else
      set shortmess=aoO
      endif
      badd +34 ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/DS07.tex
      badd +331 ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/E3/E3.tex
      badd +223 ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/P1/P1.tex
      badd +1 ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/P2/P2.tex
      badd +70 ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/E1/E1.tex
      badd +114 ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/E2/E2.tex
      argglobal
      %argdel
      $argadd DS07.tex
      edit ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/E1/E1.tex
      let s:save_splitbelow = &splitbelow
      let s:save_splitright = &splitright
      set splitbelow splitright
      let &splitbelow = s:save_splitbelow
      let &splitright = s:save_splitright
      wincmd t
      let s:save_winminheight = &winminheight
      let s:save_winminwidth = &winminwidth
      set winminheight=0
      set winheight=1
      set winminwidth=0
      set winwidth=1
      argglobal
      balt ~/Documents/Enseignement/Prepa/2023/07_DS/DS07/E2/E2.tex
      setlocal fdm=indent
      setlocal fde=0
      setlocal fmr={{{,}}}
      setlocal fdi=#
      setlocal fdl=99
      setlocal fml=1
      setlocal fdn=20
      setlocal fen
      42
      normal! zo
      43
      normal! zo
      65
      normal! zo
      102
      normal! zo
      195
      normal! zo
      224
      normal! zo
      let s:l = 70 - ((34 * winheight(0) + 45) / 91)
      if s:l < 1 | let s:l = 1 | endif
      keepjumps exe s:l
      normal! zt
      keepjumps 70
      normal! 0
      if exists(':tcd') == 2 | tcd ~/Documents/Enseignement/Prepa | endif
      tabnext 1
      if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 &&
      getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
        silent exe 'bwipe ' . s:wipebuf
        endif
        unlet! s:wipebuf
        set winheight=1 winwidth=20
        let &shortmess = s:shortmess_save
        let &winminheight = s:save_winminheight
        let &winminwidth = s:save_winminwidth
        let s:sx = expand("<sfile>:p:r")."x.vim"
        if filereadable(s:sx)
          exe "source " . fnameescape(s:sx)
          endif
          let &g:so = s:so_save | let &g:siso = s:siso_save
          set hlsearch
          nohlsearch
          doautoall SessionLoadPost
          unlet SessionLoad
          " vim: set ft=vim :
          epa
