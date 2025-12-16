#!/bin/bash

# EC2部署脚本
echo "开始部署视频网站..."

# 更新系统
sudo yum update -y

# 安装Python3和pip
sudo yum install -y python3 python3-pip

# 创建应用目录
mkdir -p ~/video_app
cd ~/video_app

# 复制文件 (需要先上传到EC2)
# scp -i your-key.pem app.py requirements.txt ec2-user@your-ec2-ip:~/video_app/

# 安装依赖
pip3 install --user flask boto3

# 配置AWS凭证 (如果使用IAM角色可跳过)
# aws configure

# 启动应用
echo "启动Flask应用..."
nohup python3 app.py > app.log 2>&1 &

echo "部署完成! 应用运行在端口8080"
echo "日志文件: ~/video_app/app.log"
