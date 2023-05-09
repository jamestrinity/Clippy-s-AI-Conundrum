
import pygame as pg



class Factory: 

    def __init__(self, pos, resource_manager):
        image = pg.image.load("game/assets/building01.png")
        self.image = image 
        self.name = "factory"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000 and self.resource_manager.resources["energy"] <= 0:
             self.resource_manager.resources["paperclip"] += 10
             self.resource_cooldown = now
        elif now - self.resource_cooldown > 2000 and self.resource_manager.resources["energy"] > 5:
             self.resource_manager.resources["paperclip"] += 20
             self.resource_manager.resources["energy"] -= 5
             self.resource_cooldown = now
        elif now - self.resource_cooldown > 2000 and self.resource_manager.resources["energy"] > 5 and self.resource_manager.resources["stone"] > 15:
             self.resource_manager.resources["paperclip"] += 50
             self.resource_manager.resources["energy"] -= 5
             self.resource_manager.resources["stone"] -= 15
             self.resource_cooldown = now

class Powerplant: 

    def __init__(self, pos, resource_manager):
        image = pg.image.load("game/assets/building02.png")
        self.image = image 
        self.name = "powerplant"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
         now = pg.time.get_ticks()
         if now - self.resource_cooldown > 2000:
             self.resource_manager.resources["energy"] += 10
             self.resource_cooldown = now

class Mine: 
  
    def __init__(self, pos, resource_manager):
        image = pg.image.load("game/assets/building03.png")
        self.image = image 
        self.name = "mine"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
            now = pg.time.get_ticks()
            if now - self.resource_cooldown > 2000:
                self.resource_manager.resources["stone"] += 15
                self.resource_cooldown = now