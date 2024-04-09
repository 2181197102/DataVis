import pandas as pd
import os

# 获取当前代码文件的目录路径
current_directory = os.path.dirname(os.path.abspath(__file__))

# 合并列表
node_df_list = []

# 去除industry为空的行的合并列表
node_df_list_delete_industry = []

for i in range(1, 4):
    # 构建数据文件的相对路径
    data_file_path = os.path.join(current_directory, '..', '..', 'DataVis', 'Dataset', 'nodes', f'Node_{i}.csv')
    node_df = pd.read_csv(data_file_path)

    # 初始化重复行计数器
    total_duplicate_rows = 0

    # 初始化industry值为空的行数计数器
    total_null_industry_rows = 0

    # 1. 查看数据大小
    print(f"Size of Node_{i}.csv: {node_df.shape}")

    # 2. 查看数据类型
    print(f"Data types of Node_{i}.csv:")
    print(node_df.dtypes)

    # 3. 检查缺失值
    print(f"Missing values in Node_{i}.csv:")
    print(node_df.isnull().sum())

    # 4. 处理空缺值，这里只是简单地用 0 填充缺失值，具体处理方法可以根据数据情况来定制
    # node_df.fillna(0, inplace=True)
    #
    # node_df_list.append(node_df)

    # 5. 检查重复行
    duplicate_rows = node_df[node_df.duplicated()]
    if not duplicate_rows.empty:
        print(f"Duplicate rows in Node_{i}.csv:")
        print(duplicate_rows)
        total_duplicate_rows += len(duplicate_rows)
        print(f"Total duplicate rows in Node_{i}.csv: {total_duplicate_rows}")
    else:
        print(f"No duplicate rows in Node_{i}.csv")
    # 6. 删除重复行
    # node_df.drop_duplicates(inplace=True)

    # 7. 合并
    node_df_list.append(node_df)

    # 8. 统计industry字段为空(即等于"[]")的行的行数
    # 将 industry 字段为 "[]" 的行转换为 NaN
    node_df['industry'].replace('[]', pd.NA, inplace=True)

    null_industry_rows = node_df['industry'].isnull().sum()
    total_null_industry_rows += null_industry_rows
    print(f"Total null industry rows in Node_{i}.csv: {total_null_industry_rows}")

    # 9. 删除industry字段为空的行
    node_df_delete_industry = node_df.dropna(subset=['industry'])
    node_df_list_delete_industry.append(node_df_delete_industry)

    # 10. 分隔符
    print("-----------------------------------")

# 合并去除industry为空的行的表
final_node_df_delete_industry = pd.concat(node_df_list_delete_industry)

# 输出去除industry为空的行
final_node_df_delete_industry.to_csv(os.path.join(current_directory, '..', '..', 'DataVis', 'Dataset', 'nodes', 'Final_Node_delete_industry.csv'),
                     index=False)

# 输出去除industry为空的行的表的大小
print(f"Size of Final_Node_delete_industry dataset: {final_node_df_delete_industry.shape}")

# 合并三个数据集为一个
final_node_df = pd.concat(node_df_list)

# 检查重复行
final_total_duplicate_rows = 0

duplicate_rows_final = final_node_df[final_node_df.duplicated()]
if not duplicate_rows_final.empty:
    print("Duplicate rows in final dataset:")
    print(duplicate_rows_final)
    final_total_duplicate_rows = len(duplicate_rows_final)
    print(f"Total duplicate rows in final dataset: {final_total_duplicate_rows}")
else:
    print("No duplicate rows in Final_Node dataset")

# 查看合并后的数据大小
print(f"Size of Final_Node dataset: {final_node_df.shape}")

# 输出合并后的数据集
# index=False 表示不输出行索引
final_node_df.to_csv(os.path.join(current_directory, '..', '..', 'DataVis', 'Dataset', 'nodes', 'Final_Node.csv'),
                     index=False)
