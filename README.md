# 数据安全可视分析



## 一、相关信息

### 1.官方网站

[ChinaVis 2022 数据可视化竞赛](https://chinavis.org/2022/challenge.html)

ChinaVis2022 中国可视化与可视分析大会数据可视化竞赛——**赛道1：数据安全可视分析**

### 2.官方提供数据

- 赛题详细介绍 [下载](https://chinavis.org/2022/document/赛道1赛题详细介绍：黑灰产网络资产图谱可视分析.docx)
- 作品文档答卷模版 [下载](https://chinavis.org/2022/document/赛道1作品文档答卷模版：ChinaVis Data Challenge 2022-mini challenge 1.docx)
- 数据下载链接 [下载](https://chinavis.org/2022/document/2022/get_data.php?index=1)

> ~/数据安全可视分析/官方提供文件/
>
> ![image-20240409102633326](picture\image-20240409102633326.png)

### 3.



## 二、背景调研









## 三、数据处理

### 1.数据集来源

https://github.com/csuvis/CyberAssetGraphData

### 2.数据集介绍

#### 2.1 Node.csv

​	Node.csv 数据文件大小为 229M，包括 237 万条数据记录，每一条数据记录 一个节点，包括表 1 所示的 4 个字段。图 1 展示了 Node.csv 的数据样本。

##### **表1. Node.csv 数据文件——字段说明**

| 字段         | 说明                                     | 类型   | 示例                                                         | 说明                             |
| ------------ | ---------------------------------------- | ------ | ------------------------------------------------------------ | -------------------------------- |
| **id**       | 节点 id                                  | String | Domain_34a6231f101fdfa2b051beaa4b94d463fe5f9f42b7789bbe60f6fd4c292ee7ac | 唯一标识节点                     |
| **name**     | 节点名称                                 | String | 0d9f06a82e.com                                               | 经过了 MD5 加密和 无效化脱敏处理 |
| **type**     | 节点类型                                 | String | Domain                                                       | 共 8 类，见表 2                  |
| **industry** | 黑灰产业务类型(只对 Domain 类型节点有效) | String | ['B']                                                        | 共 10 类，见表 3                 |



##### **表2.节点类型说明**

| 字段        | 说明                  | 数量    | 重要程度 |
| ----------- | --------------------- | ------- | -------- |
| Domain      | 网站域名              | 200 万  | 非常重要 |
| IP          | 网站的 IP 地址        | 20 万   | 非常重要 |
| Cert        | 网站用的 SSL 安全证书 | 13 万   | 非常重要 |
| Whois_Name  | 网站域名的注册人姓名  | 1.8 万  | 重要     |
| Whois_Phone | 网站域名的注册人电话  | 0.2 万  | 重要     |
| Whois_Email | 网站域名的注册人邮箱  | 0.4 万  | 重要     |
| IP_C        | IP 的 C 段            | 0.6 万  | 一般     |
| ASN         | IP 的自治域           | 0.03 万 | 一般     |



##### **表3.黑灰产业务类型说明**

| industry | 字段值       | 黑灰产业务类型说明                                         |
| -------- | ------------ | ---------------------------------------------------------- |
| A        | 涉黄         | 该域名的网站涉及色情传播                                   |
| B        | 涉赌         | 该域名的网站涉及网络赌博                                   |
| C        | 诈骗         | 该域名的网站涉及网络诈骗，如仿冒著名网站                   |
| D        | 涉毒         | 该域名的网站涉及毒品交易                                   |
| E        | 涉枪         | 该域名的网站涉及枪支交易                                   |
| F        | 黑客         | 该域名的网站是嵌入恶意信息的黑客网站，如嵌入木马的钓鱼网站 |
| G        | 非法交易平台 | 该域名的网站涉及非法交易，如个人信息买卖                   |
| H        | 非法支付平台 | 该域名的网站是非法支付平台                                 |
| I        | 其他         | 其他黑灰产业务网站                                         |



##### **图1. Node.csv 数据样本示例**

![image-20240409123636041](picture\image-20240409123636041.png)



#### 2.2 Link.csv

​	Link.csv 数据文件大小为 493M，包括 328 万条数据记录，每一条数据记录对 应一条边，包括表 4 所示的 3 个字段。图 2 展示了 Link.csv 的数据样本。

##### **表4. Link.csv 数据文件——字段说明**

| 字段     | 说明     | 类型   | 示例                                                         | 说明               |
| -------- | -------- | ------ | ------------------------------------------------------------ | ------------------ |
| relation | 边类型   | String | r_subdomain                                                  | 共 11 类，见表 5   |
| source   | 源节点   | String | Domain_34a6231f101fdfa2b051beaa4b94d463fe5f9f42b7789bbe60f6fd4c292ee7ac | 源节点的 id 字段值 |
| target   | 目标节点 | String | Domain_5052db3f33d5337ab631025f7d5de3c5ac559edb2c40deda5530c0051f39b1e2 | 目标节点的 id 字段 |



##### **表5. 边的名称说明**

| relation       | 说明               | 数量    | 关联强度 |
| -------------- | ------------------ | ------- | -------- |
| r_cert         | 域名使用的安全证书 | 23 万   | 很强     |
| r_subdomain    | 域名拥有的子域名   | 45 万   | 很强     |
| r_request_jump | 域名间跳转关系     | 0.06 万 | 很强     |
| r_dns_a        | 域名对应的 IP 地址 | 205 万  | 很强     |
| r_whois_name   | 域名的注册人姓名   | 10 万   | 较强     |
| r_whois_email  | 域名的注册人邮箱   | 2.8 万  | 较强     |
| r_whois_phone  | 域名的注册人电话   | 1.9 万  | 较强     |
| r_cert_chain   | 证书的证书链关系   | 1.5 万  | 一般     |
| r_cname        | 域名对应的别名     | 13 万   | 一般     |
| r_asn          | IP 所属的自治域    | 6.9 万  | 较弱     |
| r_cidr         | IP 所对应的 C 段   | 17 万   | 较弱     |



##### **图2. Link.csv 数据样本示例**

![image-20240409124258411](picture\image-20240409124258411.png)



### 3.数据预处理

#### 3.1 Node.csv

##### 1.查看数据大小

```
Size of Node_1.csv: (1000000, 4)

Size of Node_2.csv: (1000000, 4)

Size of Node_3.csv: (371558, 4)
```

##### 2.查看数据类型

```
Data types of Node_1.csv:
id          object
name        object
type        object
industry    object
dtype: object

Data types of Node_2.csv:
id          object
name        object
type        object
industry    object
dtype: object

Data types of Node_3.csv:
id          object
name        object
type        object
industry    object
dtype: object
```

##### 3.检查缺失值

```
Missing values in Node_1.csv:
id          0
name        0
type        0
industry    0
dtype: int64

Missing values in Node_2.csv:
id          0
name        0
type        0
industry    0
dtype: int64

Missing values in Node_3.csv:
id          0
name        0
type        0
industry    0
dtype: int64
```

无缺失值，故不作处理

##### 4.检查重复行

```
No duplicate rows in Node_1.csv

No duplicate rows in Node_2.csv

No duplicate rows in Node_3.csv
```

无重复行，故不做处理

##### 5. 统计industry字段为空(即等于"[]")的行的行数

```
Total null industry rows in Node_1.csv: 844762

Total null industry rows in Node_2.csv: 864867

Total null industry rows in Node_3.csv: 333773
```

##### 6.合并去除industry为空的行的表并输出文件

```py
final_node_df_delete_industry.to_csv(os.path.join(current_directory, '..', '..', 'DataVis', 'Dataset', 'nodes', 'Final_Node_delete_industry.csv'),
                     index=False)
```

##### 7.查看去除industry为空的行的表的大小

```
Size of Final_Node_delete_industry dataset: (328156, 4)
```

##### 8.合并总数据集后进行重复行检测

```
No duplicate rows in Final_Node dataset
```

无重复行，故不做处理

##### 9.输出合并后的总数据集文件

```py
final_node_df.to_csv(os.path.join(current_directory, '..', '..', 'DataVis', 'Dataset', 'nodes', 'Final_Node.csv'),
                     index=False)
```

##### 10.查看合并后的总数据集的大小

```
Size of Final_Node dataset: (2371558, 4)
```



##### **命令行输出**

```
Size of Node_1.csv: (1000000, 4)
Data types of Node_1.csv:
id          object
name        object
type        object
industry    object
dtype: object
Missing values in Node_1.csv:
id          0
name        0
type        0
industry    0
dtype: int64
No duplicate rows in Node_1.csv
Total null industry rows in Node_1.csv: 844762
-----------------------------------
Size of Node_2.csv: (1000000, 4)
Data types of Node_2.csv:
id          object
name        object
type        object
industry    object
dtype: object
Missing values in Node_2.csv:
id          0
name        0
type        0
industry    0
dtype: int64
No duplicate rows in Node_2.csv
Total null industry rows in Node_2.csv: 864867
-----------------------------------
Size of Node_3.csv: (371558, 4)
Data types of Node_3.csv:
id          object
name        object
type        object
industry    object
dtype: object
Missing values in Node_3.csv:
id          0
name        0
type        0
industry    0
dtype: int64
No duplicate rows in Node_3.csv
Total null industry rows in Node_3.csv: 333773
-----------------------------------
Size of Final_Node_delete_industry dataset: (328156, 4)
No duplicate rows in Final_Node dataset
Size of Final_Node dataset: (2371558, 4)

进程已结束，退出代码为 0
```

