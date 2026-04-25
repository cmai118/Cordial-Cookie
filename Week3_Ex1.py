import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"Tọa độ: ({self.x}, {self.y})") 

pA = Point(3, 4)
pA.print_point()

bx = float(input("Nhập x cho điểm B: "))
by = float(input("Nhập y cho điểm B: "))
pB = Point(bx, by)

pC = Point(-pB.x, -pB.y)
print("Điểm C đối xứng B qua O là: ", end="")
pC.print_point()

dist_BO = math.sqrt(pB.x**2 + pB.y**2)
dist_AB = math.sqrt((pA.x - pB.x)**2 + (pA.y - pB.y)**2)

print(f"Khoảng cách B -> O: {dist_BO:.2f}")
print(f"Khoảng cách A -> B: {dist_AB:.2f}")