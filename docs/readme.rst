.. include:: ../README.rst

# 操作语音命令工具

用命令行的形式来操作语音，非常的方便快捷，只需要输入命令就可以完成语音的合成、切割等;

## 使用说明

先把项目 `clone` 到本地:
> git clone git@github.com:iamkkqi/mcc.git

然后进入项目虚拟环境（我这里是已经创建好的虚拟环境）:
> . env/bin/activate

然后把项目安装到虚拟环境中:
> pip install e .

然后就可以使用命令了，我这里定义的是 `sp` 是切割命令， `sy` 是批量合成命令:
> sp --help

> sy --help
