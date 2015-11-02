# -*- coding: utf-8 -*-

open_file = open("forenzicni_program.txt", "r")

dnk = open_file.read()

print dnk

#Lastnost barva las
barva_las_crna = "CCAGCAATCGC"

barva_las_rjava = "GCCAGTGCCG"

barva_las_korencek = "TTAGCTATCGC"

if dnk.find(barva_las_crna) !=-1:
    print "Sem nasel lastnost crni lasje"
elif dnk.find(barva_las_rjava) !=-1:
    print "Sem nasel lastnost rjavi lasje"
elif dnk.find(barva_las_korencek) !=-1:
    print "Sem nasel lastnost korencek lasje"

#Lastnost oblika obraza
oblika_obraza_kvadraten = "GCCACGG"

oblika_obraza_okrogel = "ACCACAA"

oblika_obraza_ovalen = "AGGCCTCA"

if dnk.find(oblika_obraza_kvadraten) !=-1:
    print "Sem nasel lastnost kvadraten obraz"
elif dnk.find(oblika_obraza_okrogel) !=-1:
    print "Sem nasel lastnost okrogel obraz"
elif dnk.find(oblika_obraza_ovalen) !=-1:
    print "Sem nasel lastnost ovalen obraz"

#Lastnost barva oci
barva_oci_modra = "TTGTGGTGGC"

barva_oci_zelena = "GGGAGGTGGC"

barva_oci_rjava = "AAGTAGTGAC"

if dnk.find(barva_oci_modra) !=-1:
    print "Sem nasel lastnost modre oci"
elif dnk.find(barva_oci_zelena) !=-1:
    print "Sem nasel lastnost zelene oci"
elif dnk.find(barva_oci_rjava) !=-1:
    print "Sem nasel lastnost rjave oci"

#Lastnost spol
moski = "TGCAGGAACTTC"

zenska = "TGAAGGACCTTC"

if dnk.find(moski) !=-1:
    print "Sem nasel lastnost spol moski"
elif dnk.find(zenska) !=-1:
    print "Sem nasel lasnost spol zenski"

#Lastnost rasa
rasa_belec = "AAAACCTCA"

rasa_crnec = "CGACTACAG"

rasa_azijec = "CGCGGGCCG"

if dnk.find(rasa_belec) !=-1:
    print "Sem nasel lastnost rasa belec"
elif dnk.find(rasa_crnec) !=-1:
    print "Sem nasel lastnost rasa crnec"
elif dnk.find(rasa_azijec) !=-1:
    print "Sem nasel lastnost rasa azijec"

#osumljenec Ziga
barva_las_osum = "oranzna"

oblika_obraza_osum = "okrogla"

barva_oci_osum = "rjava"

spol_osum = "moski"

rasa_osum = "belec"

#osumljenec Matej
barva_las_osum = "crna"

oblika_obraza_osum = "ovalna"

barva_oci_osum = "modra"

spol_osum = "moski"

rasa_osum = "belec"

#osumljenec Miha
barva_las_osum = "rjava"

oblika_obraza_osum = "kvadratna"

barva_oci_osum = "zelena"

spol_osum = "moski"

rasa_osum = "belec"

if barva_las_osum == "oranzna" and oblika_obraza_osum == "okrogla" and barva_oci_osum == "rjava" and spol_osum == "moski" and rasa_osum == "belec":
    print "Ziga je tisti nepridiprav, ki je pojedel ves sladoled!"
elif barva_las_osum == "crna" and oblika_obraza_osum == "ovalna" and barva_oci_osum == "modra" and spol_osum == "moski" and rasa_osum == "belec":
    print "Matej je storil zlocin in pojedel ves sladoled!"
elif barva_las_osum == "rjava" and oblika_obraza_osum == "kvadratna" and barva_oci_osum == "zelena" and spol_osum == "moski" and rasa_osum == "belec":
    print "Miha je pojedel ves sladoled in bil tako spoznan za krivega!"
else:
    print "Vsi osumljenci so imeli alibi, tako da nihce od njih ni storil zlocina"




