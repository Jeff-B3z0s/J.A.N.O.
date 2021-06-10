
class Button:
    def __init__(self, text, x, y, color, font, chosen):
        self.x = x
        self.y = y
        self.text = text
        self.color = color

        self.chosen = chosen

        if self.chosen == True:
            self.color = "#00FFFF"

        self.font = font
        self.display = font.render(self.text, True, self.color)
        self.rect = self.display.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def show(self, screen):
        screen.blit(self.display, (self.x, self.y))
#TUHEIHU MY MOTHER DOES NOT HAVE ANY CHILDREN

    def hover(self, mousePos, cursor):

        if self.rect.collidepoint(mousePos) == 1:
            self.color = "#FFFFFF"
            cursor = "diamond"
        else:
            self.color = "#424B5C"
            cursor = "pointer"
        if self.chosen == True:
            self.color = "#00FFFF"

        self.display = self.font.render(self.text, True, self.color)
        cursor = "diamond"
