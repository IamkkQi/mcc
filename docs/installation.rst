.. highlight:: shell

============
Installation
============


Stable release
--------------

To install mcc, run this command in your terminal:

.. code-block:: console

    $ pip install mcc

This is the preferred method to install mcc, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


源码安装
------------

从 github 上下载 源码 `Github repo`_.

你也可以从公共的仓库中克隆:

.. code-block:: console

    $ git clone git://github.com/iamkkqi/mcc


如果你已经克隆了项目你就可以通过下面两种方式安装使用:

方法一:

.. code-block:: console

    $ python setup.py install


方法二：

然后进入项目虚拟环境（我这里是已经创建好的虚拟环境）:

.. code-block:: console

    $ . env/bin/activate

然后把项目安装到虚拟环境中:

.. code-block:: console

    $ pip install e .



.. _Github repo: https://github.com/iamkkqi/mcc
.. _tarball: https://github.com/iamkkqi/mcc/tarball/master
