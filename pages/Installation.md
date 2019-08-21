# 安装

## 警告

> Pillow 和 PIL 在同一个环境下不可共存，安装 Pillow 之前请先卸载 PIL；

> Pillow 1.0（包含） 版本之后不再支持通过“import Image”的方式进行引用，请使用“from PIL import Image”作为替代；

> Pillow 2.1.0（包含） 版本之后不再支持“import _imaging”，请使用“from PIL.Image import core as _imaging”替代。

## 说明

> Pillow对不同Python版本的支持度

|        Python        |  2.4  |  2.5  |  2.6  |  2.7  |  3.2  |  3.3  |  3.4  |  3.5  | 3.6 | 3.7 |
|  ------------------  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- | --- |
|    Pillow < 2.0.0    |  Yes  |  Yes  |  Yes  |  Yes  |       |       |       |       |     |     |
|   Pillow 2.x - 3.x   |       |       |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |     |     |
|      Pillow 4.x      |       |       |       |  Yes  |       |  Yes  |  Yes  |  Yes  | Yes |     |
| Pillow 5.0.x - 5.1.x |       |       |       |  Yes  |       |       |  Yes  |  Yes  | Yes |     |
| Pillow 5.2.x - 5.4.x |       |       |       |  Yes  |       |       |  Yes  |  Yes  | Yes | Yes |
|      Pillow 6.x      |       |       |       |  Yes  |       |       |       |  Yes  | Yes | Yes |
|   Pillow >= 7.0.0    |       |       |       |       |       |       |       |  Yes  | Yes | Yes |


## 基本安装

> 下面的步骤介绍的Pillow安装方式，只可以处理最常用的图片格式，如果需要查看完整的支持列表，请查看“[扩展类库](https://pillow.readthedocs.io/en/latest/installation.html#external-libraries)”

使用pip安装Pillow

```Python
pip install Pillow
```

### Windows安装

我们提供了兼容Windows 32位和64位的.whl、.egg和.exe格式的安装包，如果需要使用Raqm功能，则需要额外安装libraqm,fribidi,和harfbuzz

```Python
pip install Pillow
```

### macOS安装
### Linux安装
### FreeBSD安装

## 从源文件构建

### 外部类库
### 编译选项
### 在macOS上编译
### 在Windows上编辑
### 在FreeBSD上编译
### 在Linux上编译
### 在安卓上编译

## 平台支持性

### 持续集成计划
### 其他平台

## 旧版本