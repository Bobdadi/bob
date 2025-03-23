@echo off
echo 正在初始化安装环境...
echo 设置清华镜像源并启用缓存...
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set global.cache-dir "%USERPROFILE%\.pip\cache"

echo 创建虚拟环境...
python -m venv venv
call venv\Scripts\activate

echo 使用并行安装依赖...
pip install --upgrade pip
pip install -r requirements.txt --progress-bar pretty

echo 安装完成！
echo 请运行以下命令激活虚拟环境：
echo call venv\Scripts\activate
pause
