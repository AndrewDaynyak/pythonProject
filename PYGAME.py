import pygame
import random
import BUTTON


pygame.init()

clock = pygame.time.Clock()
fps = 60

bottom_panel=150
screen_width=800
screen_height=400+bottom_panel

screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fight')

#defining game variables
current_fighter=1
total_fighters=3
action_cooldown=0
action_wait_time=90
attack=False
potion=False
potion_effect=15
clicked=False
game_over=0



#defining fonts
font=pygame.font.SysFont('Prince Valiant', 26)
#define colors
red=(255, 0,0)
green=(0,255,0)

#images
#background for the game
background_image=pygame.image.load('C:/Users/Lenovo/Desktop/background.png').convert_alpha()
#panel image
bottom_panel_image=pygame.image.load('C:/Users/Lenovo/Desktop/python game/panel.png').convert_alpha()
#sword image
sword_image=pygame.image.load('C:/Users/Lenovo/Desktop/python game/Icons/sword.png').convert_alpha()
#potion image
potion_image=pygame.image.load('C:/Users/Lenovo/Desktop/python game/Icons/potion.png').convert_alpha()
#defeat and victory images
victory_image=pygame.image.load('C:/Users/Lenovo/Desktop/python game/Icons/victory.png').convert_alpha()
defeat_image=pygame.image.load('C:/Users/Lenovo/Desktop/python game/Icons/defeat.png').convert_alpha()
#restart image
restart_image=pygame.image.load('C:/Users/Lenovo/Desktop/python game/Icons/restart.png').convert_alpha()




#FUNCTION FOR ADDING TEXT
def draw_text(text, font, text_color, x,y):
    img=font.render(text, True, text_color)
    screen.blit(img,(x,y))


#Drawing background
def draw_background():
    screen.blit(background_image, (0,0))

#Drawing bottom panel
def draw_bottom_panel():
    screen.blit(bottom_panel_image, (0, screen_height-bottom_panel))
    #DRAW KNIGHT STATS
    draw_text(f'{knight.name} HP:{knight.hp}', font, red, 100, screen_height-bottom_panel+10)
    for count, i in enumerate(bandit_list):
        #'i' is bandit_list items and 'count' allows to keep a running count of where I am within this
        draw_text(f'{i.name} HP:{i.hp}', font, red, 550, (screen_height - bottom_panel + 10)+count*60)

class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name=name
        self.max_hp=max_hp
        self.hp=max_hp
        self.strength=strength
        self.start_potions=potions
        self.potions=potions
        self.alive=True
        self.animation_list=[]
        self.frame_index=0
        self.action=0 #0-idle 1-attack 2-hurt 3-dead
        self.update_time=pygame.time.get_ticks()
        #LOAD IDLE IMAGES
        temp_list=[]
        for i in range(8):
            img=self.image= pygame.image.load(f'C:/Users/Lenovo/Desktop/python game/{self.name}/idle/{i}.png')
        #SCALE UP THE IMAGE
            img=pygame.transform.scale(img, (img.get_width()* 3, img.get_height()*3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # LOAD ATTACK IMAGES
        temp_list = []
        for i in range(8):
            img = self.image = pygame.image.load(f'C:/Users/Lenovo/Desktop/python game/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(3):
            img = self.image = pygame.image.load(f'C:/Users/Lenovo/Desktop/python game/{self.name}/Hurt/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        #Death animation
        for i in range(10):
            img = self.image = pygame.image.load(f'C:/Users/Lenovo/Desktop/python game/{self.name}/Death/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image=self.animation_list[self.action][self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    #Drawing animation
    def update(self):
        animation_cooldown=100
        #Animation handling
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time=pygame.time.get_ticks()
            self.frame_index+=1
        #reset back to the start if animation has ended
        if self.frame_index>=len(self.animation_list[self.action]):
            if self.action==3:
                self.frame_index=len(self.animation_list[self.action])-1
            else:
                self.idle()




    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self, target):
        # damage to the opponent
        rand=random.randint(-5, 5)
        damage=self.strength + rand
        target.hp -= damage
        #run hurt animation for an enemy
        target.hurt()
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        damage_text=DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        #execute the attack animation
        self.action=1
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()

    def hurt(self):
        #set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        #set variables to hurt animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive=True
        self.potions=self.start_potions
        self.hp=self.max_hp
        self.frame_index=0
        self.action=0
        self.update_time=pygame.time.get_ticks()


    def draw(self):
        screen.blit(self.image, self.rect)

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x=x
        self.y=y
        self.hp=hp
        self.max_hp=max_hp


    def draw(self, hp):
        #update health
        self.hp=hp
        #current health ratio
        ratio=self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150*ratio, 20))


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image=font.render(damage, True, colour)
        self.rect=self.image.get_rect()
        self.rect.center=(x, y)
        self.counter=0

    def update(self):
        #move damage up
        self.rect.y-=1
        #delete the text
        self.counter+=1
        if self.counter>30:
            self.kill()


damage_text_group=pygame.sprite.Group()



knight=Fighter(200, 260, 'Knight', 30,10, 3 )
bandit1=Fighter(550, 270, 'Bandit',20, 6, 1)
bandit2=Fighter(700, 270, 'Bandit',20, 6, 1)

bandit_list=[]
bandit_list.append(bandit1)
bandit_list.append(bandit2)

#INSTANCES OF HEALTHBAR. (minus bottom panel is used cause it gets me to the top of the panel as a starting point)
knight_health_bar=HealthBar(100, screen_height-bottom_panel+40, knight.hp, knight.max_hp)
bandit1_health_bar=HealthBar(550, screen_height-bottom_panel+40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar=HealthBar(550, screen_height-bottom_panel+100, bandit2.hp, bandit2.max_hp)

#Creating buttons
#create potion button
potion_button=BUTTON.Button(screen, 100, screen_height-bottom_panel+70, potion_image, 64, 64)
restart_button=BUTTON.Button(screen, 335, 120, restart_image, 120, 30)
run=True
while run:
    draw_background()
    draw_bottom_panel()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()
    #DRAW THE KNIGHT
    knight.update()
    knight.draw()

    #Drawing the damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    #control player actions
    #reseting action variables
    attack=False
    potion=False
    target=None
    #make sure that at each iteration the mouse is visible
    pygame.mouse.set_visible(True)
    pos=pygame.mouse.get_pos()
    for count, bandit in enumerate(bandit_list):
        if bandit.rect.collidepoint(pos):
            #hide the mouse
            pygame.mouse.set_visible(False)
            #show sword instead of the cursor
            screen.blit(sword_image, pos)
            if clicked==True and bandit.alive==True:
                attack=True
                target=bandit_list[count]
    if potion_button.draw():
        potion=True
    draw_text(str(knight.potions), font, red, 150, screen_height-bottom_panel+70)


        #player action
    if game_over==0:
        if knight.alive == True:
            if current_fighter==1:
                action_cooldown+=1
                if action_cooldown>=action_wait_time:
                    #look for player action
                    #attack
                    if attack==True and target!=None:
                        knight.attack(target)
                        current_fighter+=1
                        action_cooldown = 0
                    if potion==True:
                        if knight.potions>0:
                            #make sure potion heal doesn't go beyond max hp
                            if knight.max_hp - knight.hp>potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = knight.max_hp-knight.hp
                            knight.hp+=heal_amount
                            knight.potions-=1
                            damage_text = DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            current_fighter+=1
                            action_cooldown=0
        else:
            game_over=-1


        #enemy action
        for count, bandit in enumerate(bandit_list):
            if current_fighter == 2+count:
                if bandit.alive==True:
                    action_cooldown+=1
                    if action_cooldown>=action_wait_time:
                        if bandit.hp / bandit.max_hp <0.5 and bandit.potions>0:
                            if bandit.max_hp - bandit.hp>potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = bandit.max_hp-bandit.hp
                            bandit.hp+=heal_amount
                            bandit.potions-=1
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            current_fighter+=1
                            action_cooldown=0
                        else:
                            bandit.attack(knight)
                            current_fighter+=1
                            action_cooldown=0
                else:
                    current_fighter+=1
        #reset if all fighters have had a turn
        if current_fighter>total_fighters:
            current_fighter=1

#check if all bandits are dead
    alive_bandits=0
    for bandit in bandit_list:
        if bandit.alive==True:
            alive_bandits+=1
    if alive_bandits==0:
        game_over=1

    #check if game is over
    if game_over !=0:
        if game_over==1:
            screen.blit(victory_image, (250, 50))
        if game_over==-1:
            screen.blit(defeat_image, (250, 50))
        if restart_button.draw():
            knight.reset()
            for bandit in bandit_list:
                bandit.reset()
                current_fighter=1
                action_cooldown
                game_over=0




    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            clicked=True
        else:
            clicked=False


    pygame.display.update()
pygame.quit()
