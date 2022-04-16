# Rename Files With Date

## 背景

文件的排序方式 通常只有【创建时间、修改时间、标题】，但问题是：

* 照片的标题通常是无效的（固定前缀+编号，甚至是无意义字符串）
* 时间也是不准的（创建时间、修改时间  其实与照片的拍摄时间 是不一致的），

所以就需要基于现有排序方式  修改相关信息，以便能够已正确的排序显示



因此，我就写了这个工具：读取文件的创建时间（照片则是拍摄时间），将其重命名，以便【在以标题排序显示时  是符合预期的】

为了避免命名重复，所以命名规则为「年月日时分秒+3位随机数，共15位数字」，示例如下：

```shell
202204062217.699.png
201601011713.247.JPG
201602251612.551.JPG
201712311343.878.JPG
202204041615.719.HEIC
202204041615.813.HEIC
202204041710.478.HEIC
202204041710.595.JPG
202204041710.749.HEIC
202204041710.750.HEIC
```



## 安装

可通过如下命令 快速安装：

```shell
$ pip install amk.rename_files_with_date
```



## 使用

### 查看说明

```shell
$ rfwd -h
usage: rfwd [-h] [-d] [-v] [-l] path

Rename Photos With Date

positional arguments:
  path           待重命名的「文件/目录」的路径

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    启用调试模式
  -v, --verbose  显示详细日志
  -l, --list     仅列表显示可能的处理，但不执行具体操作，以便检查
```



### 查看将要执行的操作

```shell
$ rfwd ./photos -l
```

![](https://gitee.com/AndyM129/ImageHosting/raw/master/images/202204072105220.png)



或是指定 `-v` 以查看很多信息：

```shell
$ rfwd ./photos -lv
```

![](https://gitee.com/AndyM129/ImageHosting/raw/master/images/202204072108092.png)



### 执行重命名

```shell
# 可追加 -v、-d 以启用详情、调试模式，以查看更多信息
$ rfwd ./photos
```

![](https://gitee.com/AndyM129/ImageHosting/raw/master/images/202204072109468.png)
