import math;


z = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0]
z_exp = [round(math.exp(i),3)  for i in z]
print (z_exp)

sum_z_exp = sum(z_exp)
print(sum_z_exp)

softmax = [round(i / sum_z_exp , 3) for i in z_exp]
print(softmax)
