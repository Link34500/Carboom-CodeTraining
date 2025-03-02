import random

import pygame
from pygame import locals.*
from pygame import mixer

pygame.init()

class Player:
    def __init__(self):
        self.joueur_x = 370
        self.joueur_y = 480
        self.joueur_x_changement = 0
        self.joueur_vitesse = 5


class Game:
    WIDTH, HEIGHT = 800, 600
ecran = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Space Shooter")


icone = pygame.Surface((32, 32))
icone.fill((100, 100, 255))
pygame.display.set_icon(icone)


joueur_img = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.polygon(joueur_img, (0, 255, 0), [(32, 0), (0, 64), (64, 64)])


ennemi_img = []
ennemi_x = []
ennemi_y = []
ennemi_x_changement = []
ennemi_y_changement = []
nombre_ennemis = 6

for i in range(nombre_ennemis):
    img = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(img, (255, 0, 0), (20, 20), 20)
    ennemi_img.append(img)
    ennemi_x.append(random.randint(0, 736))
    ennemi_y.append(random.randint(50, 150))
    ennemi_x_changement.append(2)
    ennemi_y_changement.append(40)


balle_img = pygame.Surface((16, 16), pygame.SRCALPHA)
pygame.draw.circle(balle_img, (255, 255, 0), (8, 8), 8)
balle_x = 0
balle_y = 480
balle_y_changement = 10
balle_etat = "pret"  # pret - la balle est prête à être tirée, tire - la balle est en mouvement


particules = []


score_valeur = 0
font = pygame.font.SysFont('arial', 32)
texte_x = 10
texte_y = 10


over_font = pygame.font.SysFont('arial', 64)


son_tir = pygame.mixer.Sound(buffer=bytearray())
son_tir.set_volume(0.4)

son_explosion = pygame.mixer.Sound(buffer=bytearray())
son_explosion.set_volume(0.5)


try:
    mixer.music.load(pygame.mixer.Sound(buffer=bytearray()))
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)
except:
    pass


def creer_particules(x, y, couleur, quantite):
    for _ in range(quantite):
        particule = {
            'x': x,
            'y': y,
            'vx': random.uniform(-1, 1),
            'vy': random.uniform(-1, 1),
            'rayon': random.uniform(2, 5),
            'couleur': couleur,
            'vie': random.randint(15, 30)
        }
        particules.append(particule)


def mettre_a_jour_particules():
    particules_restantes = []
    for p in particules:
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['vie'] -= 1

        if p['vie'] > 0:
            pygame.draw.circle(ecran, p['couleur'], (int(p['x']), int(p['y'])), int(p['rayon']))
            particules_restantes.append(p)

    return particules_restantes


def afficher_score(x, y):
    score = font.render(f"Score: {score_valeur}", True, (255, 255, 255))
    ecran.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    texte_rejouer = font.render("Appuyez sur ESPACE pour rejouer", True, (255, 255, 255))
    ecran.blit(over_text, (200, 250))
    ecran.blit(texte_rejouer, (200, 350))


def afficher_joueur(x, y):
    ecran.blit(joueur_img, (x, y))


def afficher_ennemi(x, y, i):
    ecran.blit(ennemi_img[i], (x, y))


def tirer_balle(x, y):
    global balle_etat
    balle_etat = "tire"
    ecran.blit(balle_img, (x + 24, y + 10))
    son_tir.play()


def est_collision(ennemi_x, ennemi_y, balle_x, balle_y):
    distance = math.sqrt((math.pow(ennemi_x + 20 - balle_x - 8, 2)) + (math.pow(ennemi_y + 20 - balle_y - 8, 2)))
    if distance < 28:  # 20 (rayon ennemi) + 8 (rayon balle)
        return True
    else:
        return False



running = True
game_over = False
clock = pygame.time.Clock()

while running:
    import pygame
    import random
    import math
    import time
    from pygame import mixer

    # Initialisation de pygame
    pygame.init()

    # Création de la fenêtre
    largeur, hauteur = 800, 600
    ecran = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Space Shooter")

    # Chargement des images
    icone = pygame.Surface((32, 32))
    icone.fill((100, 100, 255))
    pygame.display.set_icon(icone)

    # Joueur
    joueur_img = pygame.Surface((64, 64), pygame.SRCALPHA)
    pygame.draw.polygon(joueur_img, (0, 255, 0), [(32, 0), (0, 64), (64, 64)])
    joueur_x = 370
    joueur_y = 480
    joueur_x_changement = 0
    joueur_vitesse = 5


    # Animation de propulsion
    class PropulsionAnimation:
        def __init__(self, vaisseau_x, vaisseau_y):
            self.particles = []
            self.vaisseau_x = vaisseau_x
            self.vaisseau_y = vaisseau_y

        def update(self, vaisseau_x, vaisseau_y):
            self.vaisseau_x = vaisseau_x
            self.vaisseau_y = vaisseau_y

            # Ajouter de nouvelles particules
            for _ in range(2):
                particule = {
                    'x': self.vaisseau_x + 32 + random.uniform(-5, 5),
                    'y': self.vaisseau_y + 64,
                    'vx': random.uniform(-0.3, 0.3),
                    'vy': random.uniform(1, 3),
                    'rayon': random.uniform(3, 6),
                    'couleur': (random.randint(200, 255), random.randint(100, 180), 0),
                    'vie': random.randint(10, 20)
                }
                self.particles.append(particule)

            # Mettre à jour et dessiner les particules
            remaining_particles = []
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['rayon'] -= 0.1
                p['vie'] -= 1

                if p['vie'] > 0 and p['rayon'] > 0:
                    alpha = min(255, p['vie'] * 12)
                    couleur_avec_alpha = (*p['couleur'], alpha)
                    surf = pygame.Surface((int(p['rayon'] * 2), int(p['rayon'] * 2)), pygame.SRCALPHA)
                    pygame.draw.circle(surf, couleur_avec_alpha, (int(p['rayon']), int(p['rayon'])), int(p['rayon']))
                    ecran.blit(surf, (int(p['x'] - p['rayon']), int(p['y'] - p['rayon'])))
                    remaining_particles.append(p)

            self.particles = remaining_particles


    # Créer l'animation de propulsion du joueur
    propulsion_joueur = PropulsionAnimation(joueur_x, joueur_y)

    # Ennemis
    ennemi_img = []
    ennemi_x = []
    ennemi_y = []
    ennemi_x_changement = []
    ennemi_y_changement = []
    ennemi_rotation = []
    ennemi_rotation_speed = []
    nombre_ennemis = 6

    for i in range(nombre_ennemis):
        img = pygame.Surface((40, 40), pygame.SRCALPHA)
        couleur = (random.randint(200, 255), random.randint(0, 100), random.randint(0, 100))
        pygame.draw.circle(img, couleur, (20, 20), 20)
        # Ajouter des détails à l'ennemi
        pygame.draw.circle(img, (min(couleur[0] + 50, 255), min(couleur[1] + 50, 255), min(couleur[2] + 50, 255)),
                           (20, 20), 15)
        pygame.draw.circle(img, (0, 0, 0), (20, 20), 10)
        pygame.draw.circle(img, (255, 255, 255), (20, 20), 5)
        ennemi_img.append(img)
        ennemi_x.append(random.randint(0, 736))
        ennemi_y.append(random.randint(50, 150))
        ennemi_x_changement.append(random.choice([-1, 1]) * random.uniform(1.5, 2.5))
        ennemi_y_changement.append(40)
        ennemi_rotation.append(0)
        ennemi_rotation_speed.append(random.choice([-1, 1]) * random.uniform(2, 5))


    # Animation d'explosion
    class ExplosionAnimation:
        def __init__(self, x, y, couleur):
            self.particles = []
            self.x = x
            self.y = y
            self.couleur = couleur
            self.frame = 0
            self.duration = 30

            # Créer les particules d'explosion
            for _ in range(30):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(1, 5)
                particule = {
                    'x': self.x,
                    'y': self.y,
                    'vx': math.cos(angle) * speed,
                    'vy': math.sin(angle) * speed,
                    'rayon': random.uniform(3, 8),
                    'couleur': (
                        random.randint(couleur[0] - 50, couleur[0]),
                        random.randint(couleur[1] - 50, couleur[1]),
                        random.randint(couleur[2] - 50, couleur[2])
                    ),
                    'vie': random.randint(20, 30)
                }
                self.particles.append(particule)

        def update(self):
            self.frame += 1
            active = False

            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vx'] *= 0.95
                p['vy'] *= 0.95
                p['rayon'] -= 0.1
                p['vie'] -= 1

                if p['vie'] > 0 and p['rayon'] > 0:
                    active = True
                    alpha = min(255, p['vie'] * 8)
                    couleur_avec_alpha = (*p['couleur'], alpha)
                    surf = pygame.Surface((int(p['rayon'] * 2), int(p['rayon'] * 2)), pygame.SRCALPHA)
                    pygame.draw.circle(surf, couleur_avec_alpha, (int(p['rayon']), int(p['rayon'])), int(p['rayon']))
                    ecran.blit(surf, (int(p['x'] - p['rayon']), int(p['y'] - p['rayon'])))

            return active or self.frame < self.duration


    # Liste pour stocker les explosions
    explosions = []

    # Balle
    balle_img = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.circle(balle_img, (255, 255, 0), (8, 8), 8)
    balle_x = 0
    balle_y = 480
    balle_y_changement = 10
    balle_etat = "pret"  # pret - la balle est prête à être tirée, tire - la balle est en mouvement


    # Animation de traînée pour la balle
    class TrailAnimation:
        def __init__(self):
            self.particles = []

        def update(self, x, y):
            # Ajouter de nouvelles particules
            for _ in range(3):
                particule = {
                    'x': x + random.uniform(-3, 3),
                    'y': y + random.uniform(-3, 3),
                    'rayon': random.uniform(2, 4),
                    'couleur': (random.randint(200, 255), random.randint(200, 255), 0),
                    'vie': random.randint(5, 15)
                }
                self.particles.append(particule)

            # Mettre à jour et dessiner les particules
            remaining_particles = []
            for p in self.particles:
                p['rayon'] -= 0.2
                p['vie'] -= 1

                if p['vie'] > 0 and p['rayon'] > 0:
                    alpha = min(255, p['vie'] * 17)
                    couleur_avec_alpha = (*p['couleur'], alpha)
                    surf = pygame.Surface((int(p['rayon'] * 2), int(p['rayon'] * 2)), pygame.SRCALPHA)
                    pygame.draw.circle(surf, couleur_avec_alpha, (int(p['rayon']), int(p['rayon'])), int(p['rayon']))
                    ecran.blit(surf, (int(p['x'] - p['rayon']), int(p['y'] - p['rayon'])))
                    remaining_particles.append(p)

            self.particles = remaining_particles


    # Créer l'animation de traînée pour la balle
    trail_balle = TrailAnimation()


    # Étoiles d'arrière-plan
    class BackgroundStars:
        def __init__(self, nb_etoiles=100):
            self.stars = []
            for _ in range(nb_etoiles):
                self.stars.append({
                    'x': random.randint(0, largeur),
                    'y': random.randint(0, hauteur),
                    'taille': random.uniform(0.5, 2),
                    'scintillement': random.uniform(0, 2 * math.pi),
                    'vitesse': random.uniform(0.2, 0.8)
                })

        def update(self):
            for star in self.stars:
                # Faire scintiller les étoiles
                star['scintillement'] += 0.05
                luminosite = (math.sin(star['scintillement']) + 1) / 2 * 155 + 100

                # Faire bouger les étoiles lentement vers le bas
                star['y'] += star['vitesse']
                if star['y'] > hauteur:
                    star['y'] = 0
                    star['x'] = random.randint(0, largeur)

                # Dessiner l'étoile
                rayon = star['taille'] * (0.8 + (math.sin(star['scintillement']) + 1) / 5)
                couleur = (luminosite, luminosite, luminosite)
                pygame.draw.circle(ecran, couleur, (int(star['x']), int(star['y'])), rayon)


    # Créer les étoiles d'arrière-plan
    background_stars = BackgroundStars(150)

    # Score
    score_valeur = 0
    font = pygame.font.SysFont('arial', 32)
    texte_x = 10
    texte_y = 10

    # Texte Game Over
    over_font = pygame.font.SysFont('arial', 64)

    # Audio - on utilise des objets vides plutôt que de tenter de charger des fichiers
    son_tir = pygame.mixer.Sound(buffer=bytearray())
    son_tir.set_volume(0.4)

    son_explosion = pygame.mixer.Sound(buffer=bytearray())
    son_explosion.set_volume(0.5)

    # Désactivation de la musique pour éviter les erreurs
    try:
        mixer.music.load(pygame.mixer.Sound(buffer=bytearray()))
        mixer.music.play(-1)
        mixer.music.set_volume(0.3)
    except:
        pass


    def afficher_score(x, y):
        score = font.render(f"Score: {score_valeur}", True, (255, 255, 255))
        ecran.blit(score, (x, y))


    def game_over_text():
        # Effet d'animation sur le texte
        temps = pygame.time.get_ticks() / 1000
        echelle = 1 + 0.1 * math.sin(temps * 2)

        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        texte_rejouer = font.render("Appuyez sur ESPACE pour rejouer", True, (255, 255, 255))

        # Calculer la position avec animation
        rect_text = over_text.get_rect(center=(400, 250))
        rect_text.width *= echelle
        rect_text.height *= echelle

        # Créer une surface plus grande pour le texte redimensionné
        surf_text = pygame.Surface((int(over_text.get_width() * echelle), int(over_text.get_height() * echelle)),
                                   pygame.SRCALPHA)
        pygame.transform.scale(over_text, (int(over_text.get_width() * echelle), int(over_text.get_height() * echelle)),
                               surf_text)

        ecran.blit(surf_text, surf_text.get_rect(center=(400, 250)))
        ecran.blit(texte_rejouer, texte_rejouer.get_rect(center=(400, 350)))


    def afficher_joueur(x, y):
        # Ajouter une légère oscillation au vaisseau
        temps = pygame.time.get_ticks() / 1000
        decalage_y = math.sin(temps * 5) * 3

        ecran.blit(joueur_img, (x, y + decalage_y))


    def afficher_ennemi(x, y, i, angle):
        # Faire tourner l'ennemi
        rotated_img = pygame.transform.rotate(ennemi_img[i], angle)
        new_rect = rotated_img.get_rect(center=ennemi_img[i].get_rect(topleft=(x, y)).center)
        ecran.blit(rotated_img, new_rect.topleft)


    def tirer_balle(x, y):
        global balle_etat
        balle_etat = "tire"
        ecran.blit(balle_img, (x + 24, y + 10))
        son_tir.play()


    def est_collision(ennemi_x, ennemi_y, balle_x, balle_y):
        distance = math.sqrt((math.pow(ennemi_x + 20 - balle_x - 8, 2)) + (math.pow(ennemi_y + 20 - balle_y - 8, 2)))
        if distance < 28:  # 20 (rayon ennemi) + 8 (rayon balle)
            return True
        else:
            return False


    # Boucle de jeu
    running = True
    game_over = False
    clock = pygame.time.Clock()
    dernier_temps = time.time()

    while running:
        # Limiter le taux de rafraîchissement pour une vitesse de jeu constante
        clock.tick(60)
        delta_temps = time.time() - dernier_temps
        dernier_temps = time.time()

        # Fond d'écran - noir
        ecran.fill((0, 0, 20))

        # Mettre à jour et dessiner les étoiles d'arrière-plan
        background_stars.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Contrôles du joueur
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    joueur_x_changement = -joueur_vitesse
                if event.key == pygame.K_RIGHT:
                    joueur_x_changement = joueur_vitesse
                if event.key == pygame.K_SPACE:
                    if game_over:
                        # Réinitialiser le jeu
                        game_over = False
                        score_valeur = 0
                        explosions = []
                        for i in range(nombre_ennemis):
                            ennemi_x[i] = random.randint(0, 736)
                            ennemi_y[i] = random.randint(50, 150)
                            ennemi_x_changement[i] = random.choice([-1, 1]) * random.uniform(1.5, 2.5)
                    elif balle_etat == "pret":
                        # Corriger la position initiale de la balle pour qu'elle soit au centre du vaisseau
                        balle_x = joueur_x + 24
                        balle_y = joueur_y - 16
                        tirer_balle(joueur_x, joueur_y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    joueur_x_changement = 0

        # Mise à jour de la position du joueur
        joueur_x += joueur_x_changement

        # Limites du joueur
        if joueur_x <= 0:
            joueur_x = 0
        elif joueur_x >= 736:
            joueur_x = 736

        # Mettre à jour l'animation de propulsion du joueur
        propulsion_joueur.update(joueur_x, joueur_y)

        # Mettre à jour les explosions
        explosions = [exp for exp in explosions if exp.update()]

        if not game_over:
            # Mouvement des ennemis
            for i in range(nombre_ennemis):
                # Game Over
                if ennemi_y[i] > 440:
                    for j in range(nombre_ennemis):
                        # Ajouter une explosion finale pour chaque ennemi
                        couleur_ennemi = ennemi_img[j].get_at((20, 20))[:3]
                        explosions.append(ExplosionAnimation(ennemi_x[j] + 20, ennemi_y[j] + 20, couleur_ennemi))
                        ennemi_y[j] = 2000
                    game_over = True
                    break

                # Mettre à jour la rotation de l'ennemi
                ennemi_rotation[i] += ennemi_rotation_speed[i]

                # Mouvement des ennemis avec une légère oscillation
                temps = pygame.time.get_ticks() / 1000
                ennemi_x[i] += ennemi_x_changement[i] + math.sin(temps * 3 + i) * 0.5

                if ennemi_x[i] <= 0:
                    ennemi_x_changement[i] = abs(ennemi_x_changement[i]) + score_valeur / 200
                    ennemi_y[i] += ennemi_y_changement[i]
                elif ennemi_x[i] >= 736:
                    ennemi_x_changement[i] = -abs(ennemi_x_changement[i]) - score_valeur / 200
                    ennemi_y[i] += ennemi_y_changement[i]

                # Collision
                collision = est_collision(ennemi_x[i], ennemi_y[i], balle_x, balle_y)
                if collision and balle_etat == "tire":
                    son_explosion.play()
                    balle_y = joueur_y - 16
                    balle_etat = "pret"
                    score_valeur += 1

                    # Ajouter une explosion à la position de la collision
                    couleur_ennemi = ennemi_img[i].get_at((20, 20))[:3]
                    explosions.append(ExplosionAnimation(ennemi_x[i] + 20, ennemi_y[i] + 20, couleur_ennemi))

                    ennemi_x[i] = random.randint(0, 736)
                    ennemi_y[i] = random.randint(50, 150)

                afficher_ennemi(ennemi_x[i], ennemi_y[i], i, ennemi_rotation[i])

            # Mouvement de la balle
            if balle_y <= 0:
                balle_y = joueur_y - 16
                balle_etat = "pret"

            if balle_etat == "tire":
                # Mettre à jour la traînée de la balle
                trail_balle.update(balle_x, balle_y)

                tirer_balle(balle_x - 24, balle_y - 10)  # Correction des coordonnées
                balle_y -= balle_y_changement

        # Affichage du joueur
        afficher_joueur(joueur_x, joueur_y)

        # Affichage du score
        afficher_score(texte_x, texte_y)

        # Affichage du game over
        if game_over:
            game_over_text()

        # Mise à jour de l'écran
        pygame.display.update()

    # Fermeture du jeu
    pygame.quit()