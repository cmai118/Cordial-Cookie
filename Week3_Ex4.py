class ConCho:
    def __init__ (self, ten, mau_sac, giong, cam_xuc):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc

        def sua(self): print (f"{self.ten} đang sủa: Gâu gâu!!!")
        def vay_duoi(self): print (f"{self.ten} đang vẫy đuôi.")
        def an(self): print (f"{self.ten} đang ăn")
        def chay(self): print (f"{self.ten} đang chạy")

class Oto:
    def __init__(self, hang, kichThuoc, mau, gia):
        self.hang = hang
        self.kichThuoc = kichThuoc
        self.mau = mau
        self.gia = gia

    def tangToc(self): print("Xe đang tăng tốc...")
    def giamToc(self): print("Xe đang giảm tốc...")
    def dam(self): print("Cảnh báo: Va chạm!")

class TaiKhoan:
    def __init__(self, tenTk, soTk, nganHang, soDu):
        self.tenTk = tenTk
        self.soTk = soTk
        self.nganHang = nganHang
        self.soDu = soDu

    def rut(self, soTien): self.soDu -= soTien
    def gui(self, soTien): self.soDu += soTien
    def kiemTraSoDu(self): return self.soDu