import pygame
pygame.init()
class Score():
    def __init__(self,x,y):
        self.score = 0
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 50)
        
        
    '''def update(self):
        if #ball rentrée1:
            self.score1+=1000
        if #ball rentrée2:
            self.score2+=1000'''
        
    def draw(self,window):
        score_text = self.font.render(f'Player: {self.score}', True, (250,128,114)) #saumon color
        window.blit(score_text, (self.x, self.y))