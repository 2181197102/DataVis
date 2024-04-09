import pandas as pd
import hashlib

# 读取三个文件并进行处理
node_df_list = []

for i in range(1, 4):
    node_df = pd.read_csv(f'D:/course/DataVis/Dataset/nodes/Node_{i}.csv')

    # 初始化重复行计数器
    total_duplicate_rows = 0

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

    # 8. 分隔符
    print("-----------------------------------")


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
    print("No duplicate rows in final dataset")

# 查看合并后的数据大小
print(f"Size of final dataset: {final_node_df.shape}")

    # . 对数据进行清洗和转换，以及其他操作
    # 解密节点名称
    # def decrypt_name(name):
    #     # 在这里编写解密逻辑，这里使用简单的MD5解密示例
    #     return hashlib.md5(name.encode()).hexdigest()
    #
    # node_df['name'] = node_df['name'].apply(decrypt_name)
    #
    # # 转换节点类型和行业类型为数值
    # type_mapping = {'Domain': 0, 'IP': 1, 'Cert': 2, 'Whois_Name': 3, 'Whois_Phone': 4, 'Whois_Email': 5, 'IP_C': 6, 'ASN': 7}
    # industry_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
    #
    # node_df['type'] = node_df['type'].map(type_mapping)
    # node_df['industry'] = node_df['industry'].map(industry_mapping)

    # node_df_list.append(node_df)