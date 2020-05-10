#! /usr/bin/python
import numpy as np


PI = np.pi


def write_function_data(func , start, end, num, filename):
	x_array = np.linspace(start,end,num)
	y_array = func(x_array)
	with open(filename,"w") as fp:
		for x,y in zip(x_array,y_array):
			fp.write("{0:5.3f} {1:5.3f} \n".format(x,y))

def exp_sin_1(x):
	return x**2*(np.sin(x)+1.1)

def noisy_sin(x):
	noise = (np.random.rand(len(x)) - 0.5) * 0.5
	y = np.sin(x) + noise
	return y

def noisy_sin_2(x):
	noise = (np.random.rand(len(x)) - 0.5) * 0.7
	y = np.sin(x) + noise
	return y

def quadratic(x):
	return x**2

def cubic(x):
	return x**3

def sigmoid(x):
	return 1/(1 + np.exp(-x))

def write_function_data_x_random_and_fun( func_x, func_y, start, end, num, filename):
	x_initial = (np.random.randint(start*1000., end*1000., num) )/1000.
	x_array = func_x(x_initial)
	y_array = func_y(x_array) + np.random.rand(num)*(.5)

	with open(filename,"w") as fp:
		for x,y in zip(x_array,y_array):
			fp.write("{0:5.3f} {1:5.3f} \n".format(x,y))





if __name__ == "__main__":

	write_function_data(np.sin,0*PI,2*PI,6,"sin_data_0_2_6.csv")
	write_function_data(np.sin,0*PI,3.5*PI,25,"sin_data_0_35_25.csv")
	write_function_data(np.cos,0*PI,2*PI,10,"cos_data_0_2_10.csv")
	write_function_data(exp_sin_1,0*PI,3.5*PI,50,"exp_sin_1.csv")
	write_function_data(noisy_sin,0*PI,3.5*PI,50,"noisy_sin_1.csv")
	write_function_data(noisy_sin,0*PI,3.5*PI,20,"noisy_sin_2.csv")
	write_function_data(noisy_sin_2,0*PI,3.5*PI,80,"noisy_sin_3.csv")
	write_function_data(noisy_sin_2,0*PI,3.5*PI,80,"noisy_sin_4.csv")

	write_function_data(np.exp,-2,3,20,"exp_001.csv")
	write_function_data(quadratic,-2,3,20,"quad_001.csv")
	write_function_data(cubic,-2,3,20,"cubic_001.csv")
	write_function_data_x_random_and_fun(sigmoid,cubic,-5,5,400,"example_001.csv")
