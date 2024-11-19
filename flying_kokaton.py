import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    flip_img = pg.transform.flip(bg_img, True, False)

    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    kk_rct = koukaton.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0]) #screen Surfaceに背景画像を張り付ける
        screen.blit(flip_img, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(flip_img, [4800-x, 200])

        key_lst = pg.key.get_pressed()
        x = -1
        y = 0
        if key_lst[pg.K_UP]:
            y += -1
        elif key_lst[pg.K_DOWN]:
            y += 1
        if key_lst[pg.K_RIGHT]:
            x += 2
        elif key_lst[pg.K_LEFT]:
            x += -1
        kk_rct.move_ip((x, y))
        screen.blit(koukaton, kk_rct) #こうかとん
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()