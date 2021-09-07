#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 15:29
# @Author  : zhida song
# @Site    : 
# @File    : json2excel.py
# @Software: PyCharm

import pandas as pd


# transform json 2 formatted excel
def json2excel(data, js_field, id_field, js_index, js_drop):
    data[js_field] = data[js_field].fillna('[]')
    null_list = data[data[js_field] == '[]'].index.tolist()
    data = data.drop(null_list)
    df = pd.DataFrame()

    for row in data.itertuples():
        index_list = getattr(row, id_field)
        json_list = pd.read_json(getattr(row, js_field), orient='records').set_index([js_index])
        json_list = json_list.drop([js_drop], axis=1)
        json_df = pd.DataFrame(json_list.values.T, index=[index_list], columns=json_list.index)
        df = df.append(json_df)

    df.to_csv('./resu/resu.txt', sep='\t')


if __name__ == '__main__':
    filename = r"./data/test_data.csv"
    data = pd.read_csv(filename, encoding='UTF-8', sep='\t')
    js_field = 'js'
    id_field = 'id_shp'
    js_index = 'name'
    js_drop = 'disname'
    json2excel(data, js_field, id_field, js_index, js_drop)
