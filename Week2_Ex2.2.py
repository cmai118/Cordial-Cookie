import math
r = 5
V = (4/3) * math.pi * r**3
print ('1.Thể tích của một hình cầu có bán kính 5 là:', V )

gia_bia = 24.95
gia_sau_giam_gia = 24.95 * (1 - 40/100)
phi_van_chuyen = 3 + 0.75*59
print ("2. Tổng chi phí bán sỉ cho 60 cuốn là: {:.2f}". format (phi_van_chuyen + gia_sau_giam_gia * 60) )

gio_bat_dau = 6
phut_bat_dau = 52
tong_phut_bat_dau = gio_bat_dau * 60 + phut_bat_dau
dam_nhe = 8 + 15/60
dam_nhanh = 7 + 12/60
tong_phut_chay = dam_nhe + 3 * dam_nhanh + dam_nhe
tong_phut_ve = tong_phut_bat_dau + tong_phut_chay
gio_ve = int (tong_phut_ve // 60) 
phut_ve = int (tong_phut_ve % 60)
giay_ve = int ((tong_phut_ve - int(tong_phut_ve)) * 60)
print ("3.Thời gian về nhà: {}:{:02d}:{:02d}".format (gio_ve,phut_ve,giay_ve))