# Mira

Mira是一款文件映射工具，它可以将本地的文件映射到不同的地方。源文件发生更改时，映射文件也会随之改变，同时，映射文件改变也可以同步到源文件。

## Mira的核心功能

Mira的核心功能有两个，分别是**映射**和**同步**

### 映射

Mira可以将你的源文件映射到你磁盘的任意位置

### 同步

Mira可以将源文件同步到映射文件，也可以将映射文件同步到源文件

## 目录结构

### Mira目录结构

```
Mira/
├── etc/
│   ├── config.ini
│	├── commands.ini
│	└── directories.ini
└── end
```

### 仓库目录结构

```
.mira/
├── logs/
│	├── commit	//提交记录
│	└── reflog	//操作记录
├── staging/	//缓存区
│	└── staging.table	//缓存表
├── objects/	//对象
│	└── [Hash]
├── config	//配置文件
├── description	//描述文件
└── map.table	//映射表
```



## 开发进度

1. 配置文件 [√]
2. 仓库初始化
3. log
4. 文件映射
5. 文件同步