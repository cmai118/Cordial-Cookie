import math

class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class circle:
    def __init__ (self, center, radius):
        self.center = center
        self.radius = radius
        
class rectangle:
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def point_in_circle(circle, point):
    return distance(circle.center, point) <=circle.radius

def rect_in_circle(circle,rect):
    corners = [
        point(rect.x, rect.y),
        point(rect.x + rect.width, rect.y),
        point(rect.x, rect.y + rect.height),
        point(rect.x + rect.width, rect.y + rect.height),
    ]

    for p in corners:
        if not point_in_circle(circle, p):
            return False
        return True
    
def rect_circle_overlap(circle, rect):
    corners = [
        point(rect.x, rect.y),
        point(rect.x + rect.width, rect.y),
        point(rect.x, rect.y + rect.height),
        point(rect.x + rect.width, rect.y + rect.height),
    ]

    for p in corners:
        if point_in_circle(circle, p):
            return True
        return False
    
center = point(150, 100)
circle = circle(center, 75)

p = point (160, 110)
print ("Point in circle:", point_in_circle(circle, p))

rect = rectangle (140, 90, 20, 20)
print ("rect in circle:", rect_in_circle(circle, rect))
print ("rect overlap circle:", rect_circle_overlap(circle, rect))
