import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
w =1.9999559379628757
prediction = x * w
error = prediction - y
loss =np.mean(error ** 2)
gradient=np.mean(x * 2 * error)
print(gradient)
learning_rate = 0.01
w = w - learning_rate * gradient
print(w)
print(loss)

#المعادله رقم 11 مهمه جدا جدا جدا 
