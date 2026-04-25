class NhanVien:

    LUONG_MAX = 20000000.0  

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    def inTTIn(self):
        print(f"Tên NV: {self.__tenNhanVien} | "
              f"Lương cơ bản: {self.__luongCoBan} | "
              f"Hệ số: {self.__heSoLuong} | "
              f"Tổng lương: {self.tinhLuong():.0f}")

    def tangLuong(self, delta):
        heSoMoi = self.__heSoLuong + delta
        luongMoi = self.__luongCoBan * heSoMoi
        
        if luongMoi > NhanVien.LUONG_MAX:
            print(f"Thông báo: Lương mới ({luongMoi:.0f}) vượt mức LUONG_MAX!")
            return False
        else:
            self.__heSoLuong = heSoMoi
            return True

    def getTenNhanVien(self):
        return self.__tenNhanVien
    
    def setTenNhanVien(self, ten):
        self.__tenNhanVien = ten

    def getLuongCoBan(self):
        return self.__luongCoBan
    
    def setLuongCoBan(self, luong):
        if luong > 0:
            self.__luongCoBan = luong

    def getHeSoLuong(self):
        return self.__heSoLuong
    
    def setHeSoLuong(self, heSo):
        if heSo > 0:
            self.__heSoLuong = heSo

nv1 = NhanVien("Nguyễn Văn A", 5000000, 2.0)
nv1.inTTIn()

print(f"Tăng hệ số thêm 1.5: {nv1.tangLuong(1.5)}")
nv1.inTTIn()

print(f"Tăng hệ số thêm 5.0: {nv1.tangLuong(5.0)}")