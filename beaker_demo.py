'''
Desc:
File: /beaker.py
Project: learn-gin
File Created: Thursday, 7th September 2023 8:25:48 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2023 Camel Lu
'''
import sys
import pandas as pd
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
# detail: https://blog.csdn.net/lly1122334/article/details/108141525
# 1. 实例化CacheManager
cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': './tmp/cache/data',
    'cache.lock_dir': './tmp/cache/lock'
}

cache = CacheManager(**parse_cache_config_options(cache_opts))


def get_data(filename):
    '''获取数据的方式'''
    print('filename', filename)
    with open(filename) as f:
        return f.read()


def get_results():
    '''要缓存的函数'''
    # data = get_data(filename)
    jsonData = {
        'name': 'lxm',
        'age': 3
    }
    return jsonData

def read_dataframe():
    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is', 
                'portal', 'for', 'Geeks']
    
    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst)
    print(df)
    return df

def use_api():
    # 2. 通过编程API使用缓存
    temp_cache = cache.get_cache('temp', type='file', expire=10)  # 实例化一个缓存，命名空间为temp，使用文件缓存，过期时间为10s

    # 3. 创建&读取缓存
    jsonKey = 'jsont'
    results = temp_cache.get(key=jsonKey, createfunc=get_results)
    print('results', results)
    
    df_key = 'df_key'
    df = temp_cache.get(key=df_key, createfunc=read_dataframe)
    print('df', df)
    df2 = temp_cache.get(key=df_key, createfunc=read_dataframe)
    print('df2', df2)

@cache.cache('get_results_with_decorate', type='file', expire=10)
def get_results_with_decorate():
    '''要缓存的函数'''
    # data = get_data(filename)
    jsonData = {
        'name': 'lxm',
        'age': 3
    }
    print('here')
    return jsonData

@cache.cache('read_dataframe_with_decorate', type='file', expire=10)
def read_dataframe_with_decorate():
    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is', 
                'portal', 'for', 'Geeks']
    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst)
    print('dataframe here')
    return df

def use_decorate():
    dict_data = get_results_with_decorate()
    print("dict_data", dict_data)
    dict_data = get_results_with_decorate()
    print("dict_data", dict_data)

    df = read_dataframe_with_decorate()
    print("df", df)
    cache.invalidate(read_dataframe_with_decorate, 'read_dataframe_with_decorate', type='file')
    df = read_dataframe_with_decorate()
    print("df", df)
    

if __name__ == '__main__':
    # use_api()
    use_decorate()
    # print(sys.maxsize)
    # temp_cache = cache.get_cache('temp')
    # temp_cache.clear()  # 删除所有缓存
    # temp_cache.remove_value(key=filename)  # 删除特定缓存
