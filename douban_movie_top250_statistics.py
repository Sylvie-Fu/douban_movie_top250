import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

from matplotlib.font_manager import _rebuild
_rebuild() #reload一下

plt.rcParams['font.sans-serif'] = u'KaiTi' # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def check_empty(x):
    if x[1] == '':
        return x[0].strip()
    return x[1].strip()

def fetch_hit(x):
    hit = 1 / len(x)
    elements = []
    for i in x:
        elements.append(i)
    elements.append(round(hit, 3))

    return elements


def decades(data, start, end):
    num_of_bucket = int((end - start) / 10)

    buckets = [start+i*10 for i in range(num_of_bucket+1)]
    # print(buckets)
    data['first_release_year'] = data['year'].apply(lambda x: int(x.strip()[0:4]))
    # print(data['first_release_year'])
    y = []
    for i, decade in enumerate(buckets[:-1]):
        num = data[(data['first_release_year'] >= decade) & (data['first_release_year'] < buckets[i+1])]['ranking'].count()
        y.append(num)

    # print(y)
    plt.scatter(buckets[:-1], y, s=10, c='r')
    plt.title('Decade distribution')
    plt.xlabel('Decade')
    plt.ylabel('Frequency')
    plt.show()


def directors(data):
    data['chi_eng_split'] = data['director'].str.split(',')
    # print(data['chi_eng_split'])
    data['director_name'] = data['chi_eng_split'].apply(lambda x: check_empty(x))

    data['director_name'].value_counts()[data['director_name'].value_counts() > 1].plot.bar(color='g', alpha=0.5)
    plt.title('Number of movies a director has in top250 movie \n (only those who have more than one)')
    plt.xlabel('director')
    plt.ylabel('number of movies')
    plt.xticks(rotation=-95, fontsize=10)
    plt.show()


def regions(data):
    data['region_split'] = data['region'].str.split(' ')

    temp_region = []
    temp_hit = []
    data['hits_info'] = data['region_split'].apply(lambda x: fetch_hit(x))
    for item in data['hits_info']:
        for i in item[:-1]:
            temp_region.append(i)
            temp_hit.append(item[-1])
    temp_dict = {'region': temp_region, 'hit': temp_hit}
    df = DataFrame(temp_dict)

    # grouped1 = df.groupby('region')['hit'].sum()  # 按region分组，计算组内hit的sum
    grouped1 = df.groupby('region').agg({'hit': 'sum'}).sort_values(by='hit', ascending=0)

    grouped1.plot(kind='bar', color='y', alpha=0.5)
    plt.title('Contribution of a region in top250 movie')
    plt.xlabel('region')
    plt.ylabel('contribution')
    plt.show()
    # print(grouped1.sum())


def categories(data):
    data['category_split'] = data['category'].str.split(' ')

    temp_category = []
    temp_hit = []
    data['hit_info'] = data['category_split'].apply(lambda x: fetch_hit(x))
    for item in data['hit_info']:
        for i in item[:-1]:
            temp_category.append(i)
            temp_hit.append(item[-1])
    temp_dict = {'category': temp_category, 'hit': temp_hit}
    df = DataFrame(temp_dict)

    grouped1 = df.groupby('category').agg({'hit': 'sum'}).sort_values(by='hit', ascending=0)
    grouped1.plot(kind='bar', color='r', alpha=0.5)
    plt.title('Contribution of each genre in top250 movie')
    plt.xlabel('genre')
    plt.ylabel('contribution')
    plt.show()


def rates(data):
    buckets = list(np.arange(8.0, 10, 0.2))
    y = []

    for i, rate in enumerate(buckets[:-1]):
        num = data[(data['rate'] >= rate) & (data['rate'] < buckets[i+1])]['rate'].count()
        y.append(num)

    plt.scatter(buckets[:-1], y, color='purple', alpha=0.5)
    plt.title('Rate distribution')
    plt.xlabel('rate')
    plt.ylabel('frequency')
    plt.show()



if __name__ == '__main__':
    start = 1900
    end = 2020

    data = pd.read_csv('./douban_movie.csv')
    # print(data.info())


    decades(data, start, end)
    directors(data)
    regions(data)
    categories(data)
    rates(data)
