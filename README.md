# Pulsar Function Verify
  该项目主要是对 pulsar 的功能性进行验证，也是一个比较简单的 Pulsar 使用教程。该项目基于 Python Client 以及 pulsar-2.6.0 进行开发。

## Pulsar 安装及配置

### 安装包下载
wget https://mirrors.tuna.tsinghua.edu.cn/apache/pulsar/pulsar-2.6.0/apache-pulsar-2.6.0-bin.tar.gz
 
tar -xvzf apache-pulsar-2.6.0-bin.tar.gz

### standalone 模式启动 pulsar 服务
```
$ bin/pulsar standalone
```
### 创建消费者并订阅一个 topic
```
$ bin/pulsar-client consume my-topic -s "first-subscription"
```
### 创建一个生产者并生产数据
```
$ bin/pulsar-client produce my-topic --messages "hello-pulsar"
```

### 配置

在以上执行命令中，只是简单执行了 pulsar, 此时每个 topic 只有一个 partition。下面的配置是如何配置一个 topic 多个partition, 在 pulsar 中称为 Partitioned topic：
```
# 编辑 conf/standalone.conf 文件
# partition 数量通过 defaultNumPartitions设置
allowAutoTopicCreationType=partitioned
defaultNumPartitions=8192
```

## Python客户端启动
### 安装 pulsar-client
```
$ pip install pulsar-client==2.6.0
```
### 后台启动
```
$ bin/pulsar standalone
```