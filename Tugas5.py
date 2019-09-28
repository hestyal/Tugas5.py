class FakultasTeknik(object):
	def __init__ (self, u, f, ta):
		self.univ = u
		self.fak = f
		self.TahunAjaran = ta

	def cetakData0(self):
		print("Universitas\t: ", self.univ)
		print("Fakultas\t: ", self.fak)
		print("Tahun Ajaran\t: ", self.TahunAjaran)

class TeknikKomputer(FakultasTeknik):
	def __init__(self, u, f, ta, ja):
		self.univ = u
		self.fak = f
		self.TahunAjaran = ta
		self.JumlahAngkatan = ja
	def cetakData1(self):
		print("Teknik Komputer")
		print("Universitas\t: ", self.univ)
		print("Fakultas\t: ", self.fak)
		print("Tahun Ajaran\t: ", self.TahunAjaran)
		print("Jumlah Angkatan\t: ", self.JumlahAngkatan)

class PendidikanTeknikInformatikadanKomputer(FakultasTeknik):
	def __init__(self, u, f, JumlahAngkatan, TahunAjaran, ju):
		self.univ = u
		self.fak = f
		self.ja = JumlahAngkatan
		self.ta = TahunAjaran
		self.jurusan = ju

	def cetakData2(self):
		print("Pendidikan Teknik Informatika dan Komputer")
		print("Universitas\t: ", self.univ)
		print("Fakultas\t: ", self.fak)
		print("Jurusan\t: ", self.jurusan)
		print("Tahun Ajaran\t: ", self.ta)
		print("jumlah Angkatan\t: ", self.ja)
	
class PendidikanVokasionalMekatronika(FakultasTeknik):
	def __init__(self, u, f, TahunAjaran, JumlahAngkatan):
		self.univ = u
		self.fak = f
		self.ta = TahunAjaran
		self.ja = JumlahAngkatan
	def cetakData3(self):
		print("Pendidikan Vokasional Mekatronika")
		print("Universitas\t: ", self.univ)
		print("Fakultas\t: ", self.fak)
		print("TahunAjaran\t: ", self.ta)
		print("JumlahAngkatan\t: ", self.ja)
	
def main():
	ft = FakultasTeknik ('Universitas Negeri Makassar', 'Teknik', 2018)
	ft.cetakData0()

	tk = TeknikKomputer ('Universitas Negeri Makassar', 'Teknik', 2018, 2)
	tk.cetakData1()
	
	ptik = PendidikanTeknikInformatikadanKomputer ('Universitas Negeri Makassar', 'Teknik', 'Pendidikan Teknik Elektro', 2018, 10,)
	ptik.cetakData2()

	mk	 = PendidikanVokasionalMekatronika ('Universitas Negeri Makassar', 'Teknik', 2018, 2)
	mk.cetakData3()

if __name__ == "__main__":
   main()
