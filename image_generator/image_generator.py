import os
import numpy as np
import matplotlib.pyplot as plt
import skimage.draw as draw
import random
import skimage.io as io

# color_palette, image size, filename for generated files
color_palette = {'red':[255,0,0], 'green':[0,255,0], 'blue':[0,0,255]}
img_width, img_height = 128, 128
filename = 'train_result.csv'

# function for writing to file
def write_to_file(text, file):
    with open(file, 'a') as f:
        f.write(f'{text}\n')


# define triangle ("logo")
def triangle(idx, s, c, case, save=False):
    image = np.ones((img_width,img_height,3), dtype=np.uint8) * 255
    color = color_palette[c]



    Y = np.random.normal(loc=64, scale=8, size=None)
    Y = np.round(Y).astype(np.int)
    X = np.random.normal(loc=64, scale=8, size=None)
    X = np.round(X).astype(np.int)


    if case == 0:
        s = (Y, X)
    elif case == 1:
        s = (random.randint(0, img_height-8), random.randint(0, img_height-13))
    print(s)
    r = np.array([s[0], s[0]+7, s[0]])
    col = np.array([s[1]-6.5, s[1], s[1]+6.5])
    rr, cc = draw.polygon(r,col)
    image[rr, cc] = color

    # random 10 point/noises
    for k in range(10):
        image[random.randint(0, img_height-1), random.randint(0, img_width-1)] = [0,0,0]

    if save:
        fname = f'training_images/triangle_{c}_{idx:04d}.bmp'
        io.imsave(fname, image)
        write_to_file(f'{fname},triangle,{s[0]},{s[1]},{c}', filename)
    else:
        plt.imshow(image)
        plt.show()

# define hook ("logo")
def hook(idx, start, c, case, save=False):
    image = np.ones((img_width,img_height,3), dtype=np.uint8) * 255
    color = color_palette[c]


    Y = np.random.normal(loc=88, scale=8, size=None)
    Y = np.round(Y).astype(np.int)
    X = np.random.normal(loc=88, scale=8, size=None)
    X = np.round(X).astype(np.int)

    if case == 0:
        start = (Y, X)
    elif case == 1:
        start = (random.randint(12, start-12), random.randint(12, start-12))
    

    
    end = (start[0]+3, start[1]+3)
    s,e = start, end
    rr, cc = draw.line(start[0], start[1], end[0], end[1])
    image[rr, cc] = color
    image[rr-1, cc] = color
    print(start, end)

    start = end
    end = (start[0]-8, start[1]+8)
    rr, cc = draw.line(start[0], start[1], end[0], end[1])
    image[rr, cc] = color
    image[rr, cc-1] = color

    # random 10 point/noises
    for k in range(10):
        image[random.randint(0, img_height-1), random.randint(0, img_width-1)] = [0,0,0]

    if save:
        fname = f'training_images/hook_{c}_{idx:04d}.bmp'
        io.imsave(fname, image)
        write_to_file(f'{fname},hook,{s[0]},{s[1]},{c}', filename)
    else:
        plt.imshow(image)
        plt.show()

# define window ("logo")
def window(width, height, idx, start, c, case, save=False):
    image = np.ones((img_width,img_height,3), dtype=np.uint8) * 255
   
    h,w = 1, 1

    color = color_palette[c]

    Y = np.random.normal(loc=40, scale=8, size=None)
    Y = np.round(Y).astype(np.int)
    X = np.random.normal(loc=40, scale=8, size=None)
    X = np.round(X).astype(np.int)


 # big square
    if case == 0:
        start = (Y, X)
    elif case == 1:
        start = (random.randint(0, start-height), random.randint(0, start-height))
    
    end = (start[0]+height, start[1]+width)
    rr, cc = draw.rectangle(start, end=end, shape=image.shape[:2])
    image[rr, cc] = color

    # small squares (white)
    # upper left
    s = (start[0]+1, start[1]+1)
    e = (s[0]+h, s[1]+w)
    rr, cc = draw.rectangle(s, end=e, shape=image.shape[:2])
    image[rr, cc] = [255,255,255]

    # lower left
    s = (start[0]+4, start[1]+1)
    e = (s[0]+h, s[1]+w)
    rr, cc = draw.rectangle(s, end=e, shape=image.shape[:2])
    image[rr, cc] = [255,255,255]

    # upper right
    s = (start[0]+1, start[1]+4)
    e = (s[0]+h, s[1]+w)
    rr, cc = draw.rectangle(s, end=e, shape=image.shape[:2])
    image[rr, cc] = [255,255,255]

    # lower right
    s = (start[0]+4, start[1]+4)
    e = (s[0]+h, s[1]+w)
    rr, cc = draw.rectangle(s, end=e, shape=image.shape[:2])
    image[rr, cc] = [255,255,255]
    

    # random 10 point/noises
    for k in range(10):
        image[random.randint(0, img_height-1), random.randint(0, img_width-1)] = [0,0,0]


    print(idx)
    print('start:', start, 'end:', end)
    print(image.shape, image.dtype)
    print('hello world')

    if save:
        fname = f'training_images/windows_{c}_{idx:04d}.bmp'
        io.imsave(fname, image)
        write_to_file(f'{fname},windows,{start[0]},{start[1]},{c}', filename)
    else:
        plt.imshow(image)
        plt.show()

        

# draw triangle function
def draw_triangle():
    save = True

    n = [300*2,200*2,500*2]

    for i in range(3):
        c = list(color_palette.keys())[i]
        print(c)

        for j in range(n[i]):
            if j < int(n[i] * 0.9):
                triangle(s=27, idx=j, c=c, case=0, save=save)
            elif j >= int(n[i] * 0.9):
                triangle(s=128, idx=j, c=c, case=1, save=save)

# draw hook function
def draw_hook():
    save = True

    n = [370*2,350*2,280*2]

    for i in range(3):
        c = list(color_palette.keys())[i]
        print(c)

        for j in range(n[i]):
            if j < int(n[i] * 0.9):
                hook(start=128, idx=j, c=c, case=0, save=save)
            elif j >= int(n[i] * 0.9):
                hook(start=128, idx=j, c=c, case=1, save=save)


# draw window function               
def draw_windows():
    save = True

    n = [400*2,350*2,250*2]

    for i in range(3):
        c = list(color_palette.keys())[i]
        print(c)
        for j in range(n[i]):
            if j < int(n[i] * 0.9):
                window(width=6,height=6, start=42, idx=j, c=c, case=0, save=save)
            elif j >= int(n[i] * 0.9):
                window(width=6,height=6, start=128, idx=j, c=c, case=1, save=save)


if __name__=='__main__':
    import os
    os.makedirs('training_images', exist_ok=True)
    write_to_file(text='filename,logo-name,y,x,color', file=filename)
    draw_triangle()
    draw_hook()
    draw_windows()
    
    
