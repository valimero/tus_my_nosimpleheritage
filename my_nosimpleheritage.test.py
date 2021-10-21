import my_nosimpleheritage as m
from math import sin, sqrt, pow

# deplacement = m.Deplacement()
# deplacement.distance(1, 2, 3)

# def distance(x1, y1, z1, x2, y2, z2):
#     return(sqrt(pow(abs(x1 - x2), 2)) + pow(abs(y1 - y2), 2) + pow(abs(z1 - z2), 2))

# d = distance(0, 0, 0, 1, 2, 0)
# print(d)

# marchant = m.Marchant()
# assert marchant.move_to(1, 2, 3, "terre") == "se déplace vers 1, 2 en marchant"

# volant = m.Volant()
# assert volant.move_to(1, 2, 3, "zone") == "se déplace vers 1, 2, 3 en volant"

# courant = m.Courant()
# assert courant.move_to(1, 2, None, 'terre') == "se déplace vers 1, 2 en courant"

print("--------- humain Courant ----------")
humain1 = m.Humain()
print(humain1.x, humain1.y, humain1.z, humain1.zone, humain1.queue, humain1.patte)
assert humain1.x == 0 and humain1.y == 0 and humain1.z == 0 and humain1.zone == None and humain1.queue == False and humain1.patte == 2
assert humain1.move_to(1, 3, 0, 'terre') == "se déplace vers 1, 3 en courant"
# print(humain1.x, humain1.y, humain1.z, humain1.zone, humain1.patte, humain1.queue)
assert humain1.x == 1 and humain1.y == 3 and humain1.z == 0 and humain1.zone == 'terre' and humain1.queue == False, humain1.patte == 2


print("--------- humain Marchant ----------")
humain2 = m.Humain()
# print(humain2.x, humain2.y, humain2.z, humain2.zone, humain2.queue, humain2.patte)
assert humain2.x == 0 and humain2.y == 0 and humain2.z == 0 and humain2.zone == None and humain2.queue == False and humain2.patte == 2
assert humain2.move_to(1, 0, 0, 'terre') == "se déplace vers 1, 0 en marchant"
assert humain2.x == 1 and humain2.y == 0 and humain2.z == 0 and humain2.zone == 'terre' and humain2.queue == False and humain2.patte == 2

print("--------- humain flottant ----------")
humain2 = m.Humain()
# print(humain2.x, humain2.y, humain2.z, humain2.zone, humain2.queue, humain2.patte)
assert humain2.x == 0 and humain2.y == 0 and humain2.z == 0 and humain2.zone == None and humain2.queue == False and humain2.patte == 2
assert humain2.move_to(1, 2, 0, 'mer') == "se déplace vers 1, 2 en flottant"
assert humain2.x == 1 and humain2.y == 2 and humain2.z == 0 and humain2.zone == 'mer' and humain2.queue == False and humain2.patte == 2

print("--------- humain Nageant ----------")
humain2 = m.Humain()
# print(humain2.x, humain2.y, humain2.z, humain2.zone, humain2.queue, humain2.patte)
assert humain2.x == 0 and humain2.y == 0 and humain2.z == 0 and humain2.zone == None and humain2.queue == False and humain2.patte == 2
assert humain2.move_to(1, 11, -50, 'mer') == "se déplace vers 1, 11, -50 en nageant"
assert humain2.x == 1 and humain2.y == 11 and humain2.z == -50 and humain2.zone == 'mer' and humain2.queue == False and humain2.patte == 2


print("--------- voitureSansPermis1 ----------")
voitureSansPermis1 = m.VoitureSansPermis()
# voitureSansPermis1.print_var()
assert voitureSansPermis1.move_to(10, 15, 0, 'terre') == "se déplace vers 10, 15 en roulant"
# voitureSansPermis1.print_var()


print("--------- voiture sans permis 2 ----------")
voitureSansPermis2 = m.VoitureSansPermis()
assert voitureSansPermis2.x == 0 and voitureSansPermis2.y == 0 and voitureSansPermis2.z == 0 and voitureSansPermis2.zone == None and voitureSansPermis2.porte == 2
# voitureSansPermis2.print_var()
assert voitureSansPermis2.move_to(70, 69, 0, 'terre') == "se déplace vers 70, 69 en roulant"
assert voitureSansPermis2.x == 70 and voitureSansPermis2.y == 69 and voitureSansPermis2.z == 0 and voitureSansPermis2.zone == 'terre' and voitureSansPermis2.porte == 2

print("--------- Berline ----------")
berline = m.Berline()
assert berline.x == 0 and berline.y == 0 and berline.z == 0 and berline.zone == None and berline.porte == 5
# berline.print_var()
assert berline.move_to(0, 69, 0, 'terre') == "se déplace vers 0, 69 en roulant"
assert berline.x == 0 and berline.y == 69 and berline.z == 0 and berline.zone == 'terre' and berline.porte == 5


print("--------- Moto ----------")
moto = m.Moto()
assert moto.x == 0 and moto.y == 0 and moto.z == 0 and moto.zone == None and moto.porte == 0
assert moto.move_to(10, 20, 0, 'terre') == "se déplace vers 10, 20 en roulant"
assert moto.x == 10 and moto.y == 20 and moto.z == 0 and moto.zone == 'terre' and moto.porte == 0

print("--------- Hors_Bord ----------")
hors_bord = m.Hors_Bord()
assert hors_bord.x == 0 and hors_bord.y == 0 and hors_bord.z == 0 and hors_bord.zone == None and hors_bord.porte == 0
assert hors_bord.move_to(10, 20, 0, 'mer') == "se déplace vers 10, 20 en flottant"
assert hors_bord.x == 10 and hors_bord.y == 20 and hors_bord.z == 0 and hors_bord.zone == 'mer' and hors_bord.porte == 0

print("--------- spitfire ----------")
spitfire = m.Spitfire()
assert spitfire.x == 0 and spitfire.y == 0 and spitfire.z == 0 and spitfire.zone == None, spitfire.porte == 0
assert spitfire.move_to(15, 19, 300, 'terre') == "se déplace vers 15, 19, 300 en volant"
assert spitfire.x == 15 and spitfire.y == 19 and spitfire.z == 300 and spitfire.zone == 'terre', spitfire.porte == 0
assert spitfire.move_to(10, 20, 5, 'terre') == "se déplace vers 10, 20, 5 en volant"

print("--------- cygne ----------")
cygne = m.Cygne()
assert cygne.x == 0 and cygne.y == 0 and cygne.z == 0 and cygne.zone == None, cygne.patte == 2 and cygne.queue == True
assert cygne.move_to(15, 19, 0, 'mer') == "se déplace vers 15, 19 en flottant"
assert cygne.x == 15 and cygne.y == 19 and cygne.z == 0 and cygne.zone == 'mer', cygne.patte == 2 and cygne.queue == True
assert cygne.move_to(15, 19, 19, 'mer') == "se déplace vers 15, 19, 19 en volant"
assert cygne.x == 15 and cygne.y == 19 and cygne.z == 19 and cygne.zone == 'mer', cygne.patte == 2 and cygne.queue == True

print("--------- Canard ----------")
canard = m.Canard()
assert canard.x == 0 and canard.y == 0 and canard.z == 0 and canard.zone == None, canard.patte == 2 and canard.queue == True

# Volant
assert canard.move_to(10, 8, 19, 'mer') == "se déplace vers 10, 8, 19 en volant"
assert canard.x == 10 and canard.y == 8 and canard.z == 19 and canard.zone == 'mer', canard.patte == 2 and canard.queue == True

# Nageant
assert canard.move_to(10, 19, -19, 'mer') == "se déplace vers 10, 19, -19 en nageant"
assert canard.x == 10 and canard.y == 19 and canard.z == -19 and canard.zone == 'mer', canard.patte == 2 and canard.queue == True

# Flottant
assert canard.move_to(13, 15, 0, 'mer') == "se déplace vers 13, 15 en flottant"
assert canard.x == 13 and canard.y == 15 and canard.z == 0 and canard.zone == 'mer', canard.patte == 2 and canard.queue == True

# Courant
assert canard.move_to(13, 18, 0, 'terre') == "se déplace vers 13, 18 en courant"
assert canard.x == 13 and canard.y == 18 and canard.z == 0 and canard.zone == 'terre', canard.patte == 2 and canard.queue == True

# Marchant
assert canard.move_to(13, 18, 0, 'terre') == "se déplace vers 13, 18 en marchant"
assert canard.x == 13 and canard.y == 18 and canard.z == 0 and canard.zone == 'terre', canard.patte == 2 and canard.queue == True

print("--------- Poisson ----------")
poisson = m.Poisson()
assert poisson.x == 0 and poisson.y == 0 and poisson.z == 0 and poisson.zone == None, poisson.patte == 0 and poisson.queue == True
assert poisson.move_to(10, 8, -13, 'mer') == "se déplace vers 10, 8, -13 en nageant"
assert poisson.x == 10 and poisson.y == 8 and poisson.z == -13 and poisson.zone == 'mer', poisson.patte == 0 and poisson.queue == True




# print (humain.move_to(1, 2, 0, 'terre'))
# humain.print_var()
