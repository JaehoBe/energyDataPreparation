# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#############################################################
# import modules

import zipfile
import os
import glob
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#############################################################
# set working paths

directory = 'C:/Users/USER/Desktop/aptEnergy/energyData/'
sub_folders = [name for name in os.listdir(directory)]

#############################################################

# extract zip files: gas use data

# directory = 'C:/Users/USER/Desktop/aptEnergy/energyData/'
# sub_folders = [name for name in os.listdir(directory)]
#
# for sub_folder in sub_folders:
#     sub_folder_path = os.path.join(directory + sub_folder)
#
#     print(sub_folder_path)
#
#     path_zipfileExtracted = os.path.join(sub_folder_path, r'zipFilesExtracted')
#     if not os.path.exists(path_zipfileExtracted):
#         os.makedirs(path_zipfileExtracted)
#
#     # Iterate over all files in the directory
#     for filename in os.listdir(sub_folder_path)[:-2]:
#         if filename.endswith('.zip'):
#             # Construct the full file path
#             file_path = os.path.join(sub_folder_path, filename)
#
#             print(file_path)
#
#             # Open the zip file for reading
#             with zipfile.ZipFile(file_path, 'r') as zip_ref:
#                 # Extract all files to the same directory
#                 zip_ref.extractall(path_zipfileExtracted)
#
#     # note: 2020, 2021 files are in another folder in each zip file. So I manually extract them and save them in the dataProcessing folder.

#############################################################
# define column names

# with open('C:/Users/USER/Desktop/aptEnergy/colNames.txt', 'r', encoding='utf-8') as f:
#     cols = f.read().split('\t')
# # print(len(cols))
# # for col in cols:
# #     print(col)

#############################################################
# define column names

# for folder in sub_folders:
#     sub_path_folder = directory + '/' + folder + '/zipFilesExtracted'
#     # print(sub_path_folder)
#     energy_use_files = glob.glob(os.path.join(sub_path_folder, "*.txt"))
#     # print(energy_use_files)
#
#     dfs_name = "dfs" + folder
#     dfs = []
#
#     for f in energy_use_files:
#         year = f[-8:-4]
#         dfName = "df" + year
#         df = pd.read_csv(f, encoding="cp949", header=None, names=cols, sep="|", low_memory=False)
#         # print(df.head())
#         dfSubset = df[['사용_년월', '대지_위치', '시군구_코드', '법정동_코드', '사용_량(KWh)']]
#         dfSubset.name = dfName
#         dfs.append(dfSubset)
#         print(year)
#
#     dfsConcat = pd.concat(dfs, axis=0)
#     dfsConcat.name = dfs_name
#     # print(dfsConcat.head())
#     file_path = os.path.join(directory + '/' + folder + '/dataProcessing', dfsConcat.name + '.csv')
#     print(file_path)
#     dfsConcat.to_csv(file_path, index=False, sep=",")

#############################################################
# open files and drop rows with nan

# directory = 'C:/Users/USER/Desktop/aptEnergy/energyData/'
# sub_folders = [name for name in os.listdir(directory)]

sub_path_gasUseData = directory + '/gas/dataProcessing/dfsgas.csv'
dfGas = pd.read_csv(sub_path_gasUseData, low_memory=False)
print(dfGas.head())

dfGas = pd.read_csv('C:/Users/USER/Desktop/aptEnergy/dataProcessing/aptEnergyUseData.csv', low_memory=False)
