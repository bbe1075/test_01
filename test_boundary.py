def win_b(x,y,w,h, imgx,imgy):
    new_w = 0
    new_h = 0
    inwin = 0
    if(x > imgx):
        inwin = 0
    elif((x + w) > imgx):
        inwin = 1
        new_w = imgx - int(x/w)*w
    else:
        inwin = 1
        new_w = w
    if(y > imgy):
        inwin = 0        
    elif((y + h) > imgy):
        inwin = 1
        new_h = imgy - int(y/h)*h
    else:
        inwin = 1
        new_h = h   
    if((x <= imgx) & (y <= imgy)):
        inwin = 1
    else:
        inwin = 0
    return inwin, new_w, new_h

def next_win(x,y,w,h, ix, iy):
    nx = x + w*ix
    ny = y + h*iy
    return nx, ny


######################################################

#imgx = 1216
#imgy = 1940
imgx = 480
imgy = 640

x = 0
y = 0
h = 240
w = 150
nx = 0
ny = 0
inwin = 0
new_w = 0
new_h = 0
#######################################################
for iy in range(8):
    for ix in range(8):
        nx , ny =  next_win(x,y,w,h,ix,iy)
        print("win %d,%d"%(ix,iy))
        inwin, new_w, new_h = win_b(nx,ny,w,h, imgx,imgy)
        print("inwin = %d, new_w=%d, new_h =%d, x=%d, y =%d, win_tot_pix=%d, win_tot_grad_num=%d"%(inwin,new_w,new_h,nx,ny,  new_w*new_h, new_w*new_h - new_h))
        




