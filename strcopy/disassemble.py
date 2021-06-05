import r2pipe

r = r2pipe.open()
r.cmd('db main; dc;db s+ 8')
