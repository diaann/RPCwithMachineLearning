import xmlrpc.client

# masuk ke lingkungan rpc
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

print('\n## HEART DISEASE EARLY PREDICTION ##\n')

# inputan2
n1 = input("1. age: ")

n2 = input("\n2. sex (1 = male; 0 = female): ")

print('\n- 0 = typical angina')
print('- 1 = atypical angina')
print('- 2 = non-anginal pain')
print('- 3 = asymptomatic')
n3 = input("3. chest pain (0/1/2/3): ")

n4 = input("\n4. resting blood pressure: ")

n5 = input("\n5. cholesterol: ")

n6 = input("\n6. fasting blood sugar > 120? (1 = yes; 0 = no): ")

print('\n- 0 = normal')
print('- 1 = abnormal')
print('- 2 = hyper')
n7 = input("7. resting electrocardiographic results (0/1/2): ")

n8 = input("\n8. maximum heart rate: ")

n9 = input("\n9. exercise induced angina (1 = yes; 0 = no): ")

n10 = input("\n10. oldpeak: ")

# eksekusi
hasil = server.naive_bayes(int(n1),int(n2),int(n3),int(n4),int(n5),int(n6),int(n7),int(n8),int(n9),float(n10))
hasil2 = server.svm(int(n1),int(n2),int(n3),int(n4),int(n5),int(n6),int(n7),int(n8),int(n9),float(n10))
hasil3 = server.knn(int(n1),int(n2),int(n3),int(n4),int(n5),int(n6),int(n7),int(n8),int(n9),float(n10))

print('\n## Prediction ##')
print('1. Naive Bayes:', hasil)
print('2. SVM:', hasil2)
print('3. KNN:', hasil3)