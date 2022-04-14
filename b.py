import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm
import gc, os
import logging
import time
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

# 定义数据路径
data_path = 'C:/Users/ys101/Desktop/fsdownload/'
save_path = 'C:/Users/ys101/Desktop/fsdownload/'


# 召回数据打标签
def get_rank_label_df(recall_list_df, label_df, is_test=False):
    for recall_list_df_ in recall_list_df:
        if recall_list_df_['click_article_id'] in label_df:
            recall_list_df_['label'] = '1'
        else:
            recall_list_df_['label'] = '0'
    recall_list_df_['label'] = recall_list_df_['click_timestamp'].apply(lambda x: 0.0 if np.isnan(x) else 1.0)
    print("recall_list_df_", recall_list_df_.head())
    return recall_list_df_


# 获取当前数据的历史点击和最后一次点击
def get_hist_and_last_click(all_click):
    click_article_id_list = all_click['click_article_id']
    #     click_article_id_list_new = [str(x) for x in click_article_id_list]
    #     print(click_article_id_list_new)
    return click_article_id_list


def tolist(click_article_id_list):
    list1 = []
    for index, row in click_article_id_list.iterrows():
        list1.append(row['click_ids'])
    return list1


# item_emb_df = pd.read_csv(data_path + 'articles_emb.csv')
#
# item_emb_cols = [x for x in item_emb_df.columns if 'emb' in x]
# all_click = pd.read_csv(data_path+'train_click_log.csv')
# click_article_id_list = get_hist_and_last_click(all_click)
click_article_id_list = pd.read_csv(data_path + 'click_article_id_list111.csv')
# feature_data.head()
# trn_user_items_df = recall_list_df[recall_list_df['user_id'].isin(click_trn_hist['user_id'].unique())]
list1 = tolist(click_article_id_list)
feature_data = pd.read_csv(data_path + 'trn_user_item_feats_df.csv')
print(feature_data['label'].head())
trn_user_item_label_df = get_rank_label_df(feature_data, list1, is_test=False)