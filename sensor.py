import time #library ini digunakan untuk meng-import modul waktu.
import board #library ini digunakan untuk menentukan pin GPIO yang akan digunakan pada raspberry pi dan sensor.
import adafruit_dht #pustaka khusus untuk sensor DHT.
import psutil #libraray yang digunakan untuk  mengambul informasi tentang proses yang sedang berjalan.

for proc in psutil.process_iter(): #berfungsi untuk mengembalikan iterator yang menghasilkan instance kelas proses untuk semua proses yang berjalan di mesin lokal.
	if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
		proc.kill() #perintah untuk mmenghentikan proses
sensor = adafruit_dht.DHT11(board.D23) #mendefinisikan nama sensor dan nomor pin yang digunakan.
while True: #mengulang perintah ranpa kondisi apa pun sampai pernyataan break dieksekusi di dalam loop.
	try:
		temp = sensor.temperature #membaca nilai temperatur atau suhu pada sensor.
		humidity = sensor.humidity #membaca nilai kelembaban dari sensor.
		print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity)) #mencentak hasil output pada layar.mempertimbangkan akurasi sensor yang terbatas, hasilnya dengan format tanpa desimal.
	except RuntimeError as error: #menangani error apabila terdapat kesalahan dalam proses runtime error.
		print(error.args[0]) #menampilkan output error
		time.sleep(2.0) #delay waktu selama 2 detik dalam menampilkan hasil dari sesnor.
		continue #sesnsor akan terus membaca dan menampilkan hasil.
	except Exception as error: #mendeteksi kesalahan selama dieksekusi.
		sensor.exit() #fungsi untuk keluar dari perintah.
		raise error #digunakan untuk membagkitkan ekspesi ketika kondisi error.
	time.sleep(2.0) #delay  waktu selama 2 detik dalam menampilkan hasil dari sesnor.
