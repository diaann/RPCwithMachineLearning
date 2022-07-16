# import package/library xml rpc server
from xmlrpc.server import SimpleXMLRPCServer

# import library
import pandas as pd # membaca data (csv), drop kolom, dll
from sklearn.naive_bayes import GaussianNB # untuk naive bayes
from sklearn.svm import SVC # untuk svm
from sklearn.neighbors import KNeighborsClassifier # untuk knn
import warnings # untuk warning

# jika tidak mengimport warnings, nanti pada bagian server akan muncul warning
warnings.filterwarnings('ignore') # untuk menghilangkan warning.

# dataset
# read_csv merupakan fungsi atau method yg ada pada library read_csv
data 		= pd.read_csv("dataset/heart.csv") # membaca dataset, tempatnya ada di folder dataset 

# dilakukan drop krn parameter/fitur yg digunakan hanya 10. slope, ca, thal tidak digunakan
# kolom target didrop karena kolom target merupakan kolom label (hasil yg mau diprediksi)
# 'drop' merupakan fungsi atau method yg ada pada library pandas
parameter	= data.drop(['slope','ca','thal','target'], axis=1) # parameter/feature

# target merupakan kolom label yg isinya ada klasifikasi
# ada 2 klasifikasinya 'heart disease' dan 'tidak heart disease'
target		= data['target'] # target/label

# fungsi algoritma naive bayes
def naive_bayes(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak):

	# memanggil fungsi klasifikasi dari algoritma naive bayes
	# kemudian disimpan pada variabel NB
	NB = GaussianNB()
	# memanggil fungsi training, parameter yg dimasukkan yaitu nama modelnya -> NB
	training(NB)
	
	# data test
	# menyimpan data baru yg nanti diinputkan di client
	# disimpan pada new_data
	new_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]

	# memanggil fungsi prediction
	# return atau mengembalikan prediksinya
	return str(prediction(NB, new_data))


# algoritma svm
def svm(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak):

	# training
	svm = SVC(random_state = 1)
	# function training
	training(svm)

	# data test
	new_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]

	# prediction and result
	return str(prediction(svm, new_data))


# algoritma knn
def knn(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak):

	# training
	knn = KNeighborsClassifier(n_neighbors = 2)  # n_neighbors means k
	# function training
	training(knn)

	# data test
	new_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]

	# prediction and result
	return str(prediction(knn, new_data))


# function untuk training
# parameternya ada 1, yaitu nama model
def training(model):

	# model = nama modelnya
	# fit merupakan method untuk training data
	# kolom2 pada parameter dan target akan ditraining
	model.fit(parameter, target)


# function prediction and result
# parameternya ada 2, yaitu nama model dan nama data_test(new_data)
def prediction(model, data_test):

	# model = nama model
	# predict = method untuk prediksi
	# data_test = new_data yg akan diiinputkan di client
	# prediction = variabel menyimpan hasil prediksi
	prediction = model.predict([data_test])

	# kondisi
	# jika prediksi = 0, maka akan dikembalikan 'no heart disease'
	# jika selain itu (prediksi = 1), maka akan dikembalikan 'heart disease'
	if (prediction == 0):
		return 'no heart disease'
	else:
		return 'heart disease'


# inisialisasi server
server = SimpleXMLRPCServer(("localhost", 8000))

# transmisikan fungsi2
server.register_function(naive_bayes, "naive_bayes")
server.register_function(svm, "svm")
server.register_function(knn, "knn")

print("\n## SERVER IS READY ##")

# jika dihilangkan, ketika server_heart_disease.py dijalankan maka akan muncul "server is ready"
# tetapi setelah itu akan keluar
# oleh karena itu servernya dibuat serve_forever, agar servernya jalan terus.
server.serve_forever()