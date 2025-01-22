# 使用 官方Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /FlaskAPI

# 复制 requirements.txt 到工作目录
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到工作目录
COPY . . 

# 暴露端口
EXPOSE 5000

# 运行Flask 应用
CMD ["python", "app.py"]
