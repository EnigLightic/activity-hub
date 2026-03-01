> 三翼青媒寒假的大作业项目-志愿活动报名系统

## 运行方法
### 克隆项目
在本地文件夹内git clone远程的项目
```bash
git clone https://github.com/EnigLightic/activity-hub.git
```
(如果报错大概率是网络问题)

### 打开项目
在PyCharm里面打开这个项目:activity-hub,接下来的命令若不加说明都是在Pycharm里面打开终端输入

### 创建虚拟环境
在当前目录下创建虚拟环境
```bash
python -m venv venv
```
不同电脑的python环境不一样，上面的命令可能需要写成python3而不是python

### 激活虚拟环境
```bash
source venv\bin\activate
```

### 安装依赖
```bash
cd backend
pip install -r requirements.txt
```

### 配置数据库
```bash
export FLASK_APP=app
flask db init
flask db migrate -m "init"
flask db upgrade
```

### 运行
在app下面的run.py中点击右上处绿色三角形运行
