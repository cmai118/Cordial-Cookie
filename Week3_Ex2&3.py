class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def hien_thi(self):
        print(f"Siêu nhân: {self.ten} | Vũ khí: {self.vu_khi} | Màu: {self.mau_sac}")

danh_sach_sn = []
while True:
    choice = input("Bạn có muốn nhập siêu nhân không? (có/không): ")
    if choice.lower() == 'không':
        break
    
    ten = input("Tên: ")
    vu_khi = input("Vũ khí: ")
    mau = input("Màu sắc: ")
    
    sn = SieuNhan(ten, vu_khi, mau)
    danh_sach_sn.append(sn)

print("\n--- Danh sách siêu nhân ---")
for sn in danh_sach_sn:
    sn.hien_thi() 

