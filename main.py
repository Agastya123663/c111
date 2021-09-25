import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics 
import random

db = pd.read_csv('studentMarks.csv')
data = db['Math_score'].tolist()

fig = ff.create_distplot([data],['Math_score'],show_hist=False)
#fig.show()

data_mean = statistics.mean(data)
data_stdev = statistics.stdev(data)

#print('The mean of the population data is : ', data_mean)
#
# print('The standard deviation  of the population data is : ', data_stdev)

# pass the number of data points we want as counter
def random_set_of_means(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    data_set_mean = statistics.mean(data_set)
    return data_set_mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)

#print('The mean of the sample data is : ', sample_mean)
#print('The standard deviation  of the sample data is : ', sample_stdev)

fig = ff.create_distplot([mean_list],['Math_score'],show_hist=False)
#fig.show()

first_standardDeviation_start,first_standardDeviation_end = sample_mean-sample_stdev,sample_mean+sample_stdev
second_standardDeviation_start,second_standardDeviation_end = sample_mean-2*(sample_stdev),sample_mean+2*(sample_stdev)
third_standardDeviation_start,third_standardDeviation_end = sample_mean-3*(sample_stdev),sample_mean+3*(sample_stdev)

#print("std_dev-1", first_standardDeviation_start,first_standardDeviation_end)
#print("std_dev-2", second_standardDeviation_start,second_standardDeviation_end)
#print("std_dev-3", third_standardDeviation_start,third_standardDeviation_end)


#finding mean of first data sample(students who got tablet with learning material)
df1 = pd.read_csv('data1.csv')
data1 = df1['Math_score'].tolist()
mean_sample1 = statistics.mean(data1)
#print('mean of sample 1 : ',mean_sample1)
fig1 = ff.create_distplot([data1],['Math_score'],show_hist=False)
#fig1.show()

#finding mean of second data sample(students with extra classes)
df2 = pd.read_csv('data2.csv')
data2 = df2['Math_score'].tolist()
mean_sample2 = statistics.mean(data2)
#print('mean of sample 2 : ',mean_sample2)
fig2 = ff.create_distplot([data2],['Math_score'],show_hist=False)
#fig2.show()

#finding mean of third data sample(students who got workshops)
df3 = pd.read_csv('data3.csv')
data3 = df3['Math_score'].tolist()
mean_sample3 = statistics.mean(data3)
#print('mean of sample 3 : ',mean_sample3)
fig3 = ff.create_distplot([data2],['Math_score'],show_hist=False)
#fig3.show()


z1 = (data_mean-mean_sample1)/data_stdev
z2 = (data_mean-mean_sample2)/data_stdev
z3 = (data_mean-mean_sample3)/data_stdev


print('the z score for sample one is : ',z1)
print('the z score for sample two is : ',z2)
print('the z score for sample three is : ',z3)