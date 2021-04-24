# 安装一个requests
FROM python:alpine3.6

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

#安装支持http/HTTPS协议客户端请求的库
#RUN pip install requests && \
#    pip install aiohttp && \
#    pip install tornado && \
#    pip install selenium && \
#    pip install appium-python-client


#安装gcc编译环境
RUN apk add --no-cache gcc musl-dev

#下列模块的安装需要gcc编译环境
RUN pip install twisted &&\
    pip install gevent


#安装 scrapy
#Ubuntu下依赖：libxml2-dev libxslt-dev zliblg-dev libffi-dev libssl-dev
RUN apk add --no-cache libxml2-dev libxslt-dev zlib-dev libffi-dev openssl-dev &&\
    pip install scrapy

#安装pyspider
#Ubuntu下依赖：
RUN apk add --no-cache curl-dev openssl-dev libxml2-dev libxslt-dev zlib-dev &&\
    pip install pyspider