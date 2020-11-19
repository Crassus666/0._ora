import pygame as pg
import time
txt = open(r'C:\Users\User\AppData\Local\Temp\Rar$DRa8652.49425\Forrasok\4_Otszaz\penztar.txt', 'r')

f = 0
KEK = (0, 0, 255)

pg.init()

def vasarlo_sorszamanak_megadasa():
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    doboz = pg.Rect(840, 500, 140, 32)
    nem_aktiv_szin = pg.Color('lightskyblue3')
    aktiv_szin = pg.Color('dodgerblue2')
    aktiv = False
    n_vasarlo = ''
    fut = True
    karakterekszama = 0
    f = 0
    timesnewroman = pg.font.SysFont('Times new roman', 30)
    vasarlo_kosara = []
    kosarban_targyak_szama = 0
    while fut:

        pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:

                pg.QUIT()



            if event.type == pg.MOUSEBUTTONDOWN:

                if doboz.collidepoint(event.pos):

                    aktiv = not aktiv
                else:
                    aktiv = False

                nem_aktiv_szin = aktiv_szin if aktiv else nem_aktiv_szin



            if event.type == pg.KEYDOWN:
                if aktiv:
                    if event.key == pg.K_RETURN:
                        lefutotott_mar = True
                        sor = txt.readline()
                        while (sor != ""):

                            if (sor == "F\n"):
                                f += 1
                            try:
                                if (f == int(n_vasarlo) - 1 and sor != "F\n"):

                                    vasarlo_kosara.append(sor)
                                    kosarban_targyak_szama += 1
                                if n_vasarlo == "-":
                                    screen.blit(timesnewroman.render("Negatív szám nem értelmezhető!", False,
                                                                     (pg.Color('DARKRED'))),
                                                (780, 600))
                                if n_vasarlo == "":
                                    screen.blit(timesnewroman.render("Kérem adjon meg egy értéket!", False,
                                                                     (pg.Color('DARKRED'))),
                                                (780, 600))
                                if 0 > int(n_vasarlo):
                                    screen.blit(timesnewroman.render("Negatív szám nem értelmezhető!", False,
                                                                     (pg.Color('DARKRED'))), (780, 600))

                                if 0 < int(n_vasarlo) <= 141:

                                    for i in range(kosarban_targyak_szama):
                                        targyak_kiirata = timesnewroman.render(str(vasarlo_kosara[i]), False,
                                                                               (pg.Color('SPRINGGREEN')))
                                        screen.blit(targyak_kiirata, (900, 550 + i * 30))

                                if int(n_vasarlo) == 0:
                                    screen.blit(
                                        timesnewroman.render("Nem lehet a sorszám '0'!", False, (pg.Color('DARKRED'))),
                                        (800, 600))
                                if int(n_vasarlo) > 141:
                                    screen.blit(timesnewroman.render("Csak 141 vásárlás történt!", False,
                                                                     (pg.Color('DARKRED'))),
                                                (800, 600))

                            except TypeError:

                                if n_vasarlo != "-" and n_vasarlo != "":
                                    screen.blit(
                                        timesnewroman.render("Csak szám elfogadható!", False, (pg.Color('DARKRED'))),
                                        (800, 600))

                                pg.display.flip()
                                clock.tick(30)
                            except ValueError:
                                print("ValueError")

                            sor = txt.readline()


                    elif event.key == pg.K_BACKSPACE:
                        n_vasarlo = ''

                        karakterekszama = 0


                    else:
                        if karakterekszama <= 10:

                            n_vasarlo += event.unicode
                            karakterekszama += 1


                if event.key == pg.K_ESCAPE:
                    pg.QUIT()




        screen.fill((30, 30, 30))
        szoveg = font.render(n_vasarlo, True, nem_aktiv_szin)
        szelesseg = max(235, szoveg.get_width()+10)
        doboz.w = szelesseg
        screen.blit(szoveg, (doboz.x+5, doboz.y+5))
        pg.draw.rect(screen, nem_aktiv_szin, doboz, 2)

        try:
            if n_vasarlo == "-":
                screen.blit(timesnewroman.render("Negatív szám nem értelmezhető!", False, (pg.Color('DARKRED'))),
                            (780, 600))
            if n_vasarlo == "":
                screen.blit(timesnewroman.render("Kérem adjon meg egy értéket!", False, (pg.Color('DARKRED'))),
                            (780, 600))
            if 0 > int(n_vasarlo):
                screen.blit(timesnewroman.render("Negatív szám nem értelmezhető!", False, (pg.Color('DARKRED'))), (780, 600))

            if 0 < int(n_vasarlo) <= 141 :

                for i in range(kosarban_targyak_szama):

                    targyak_kiirata = timesnewroman.render(str(vasarlo_kosara[i]), False, (pg.Color('SPRINGGREEN')))
                    screen.blit(targyak_kiirata, (900, 550+ i*30))



            if int(n_vasarlo) == 0:
                screen.blit(
                    timesnewroman.render("Nem lehet a sorszám '0'!", False, (pg.Color('DARKRED'))),
                    (800, 600))
            if int(n_vasarlo) > 141 :
                screen.blit(timesnewroman.render("Csak 141 vásárlás történt!", False, (pg.Color('DARKRED'))),
                            (800, 600))

        except ValueError:


            if n_vasarlo != "-" and n_vasarlo != "":
                screen.blit(timesnewroman.render("Csak szám elfogadható!", False, (pg.Color('DARKRED'))),(800, 600))


        except TypeError:
            print("TypeError")

        sorszam_felirat = timesnewroman.render('Vásárló kosarának a sorszáma:', False, (pg.Color('lightskyblue3')))
        screen.blit(sorszam_felirat, (770, 400))
        pg.display.flip()
        clock.tick(30)

vasarlo_sorszamanak_megadasa()
txt.close()
