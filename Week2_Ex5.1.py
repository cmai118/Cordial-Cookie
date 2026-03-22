import time
tong_thoi_gian = time.time()

giay_trong_mot_ngay = 24 * 60 * 60
so_ngay = int(tong_thoi_gian// giay_trong_mot_ngay)
so_giay_con_lai = tong_thoi_gian % giay_trong_mot_ngay

gio = int(so_giay_con_lai // 3600)
so_giay_con_lai = int (so_giay_con_lai % 3600) 

phut = int(so_giay_con_lai // 60)
giay = int(so_giay_con_lai % 60)

print("Số ngày kể từ epoch:", so_ngay)
print("Thời gian hiện tại (GMT): {:02d}:{:02d}:{:02d}".format(gio, phut, giay))