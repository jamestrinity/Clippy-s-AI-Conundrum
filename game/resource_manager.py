
import pygame as pg



class ResourceManager:


    def __init__(self):

        # resources
        self.resources = {
           "paperclip": 75,
            "stone": 150,
            "energy": 50
        }

        #costs
        self.costs = {
            "factory": {"stone": 150, "paperclip": 75,  "energy": 50},
            "powerplant": {"paperclip": 100},
            "mine": {"paperclip": 200, "energy": 10}
        }

    def apply_cost_to_resource(self, building):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost

    def is_affordable(self, building):
        affordable = True
        for resource, cost in self.costs[building].items():
            if cost > self.resources[resource]:
                affordable = False
        return affordable

