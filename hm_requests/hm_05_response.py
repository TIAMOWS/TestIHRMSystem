# 导包
import requests
# 发送get请求访问百度
# 1). 访问百度首页的接口`http://www.baidu.com`，获取以下响应数据
response=requests.get('http://www.baidu.com')

# 2). 获取响应状态码
print('状态码:',response.status_code)
# 3). 获取请求URL
print('获取请求URL:',response.url)

# 4). 获取响应字符编码
print('响应字符编码:',response.encoding)

# 5). 获取响应头数据
print('响应头数据:',response.headers)

# 6). 获取响应的cookie数据
print('响应的cookie数据:',response.cookies)

# 7). 获取文本形式的响应内容
print('文本形式的响应内容:',response.text)

# 8). 获取字节形式的响应内容
print('字节形式的响应内容:',response.content)

# 解决乱码情况,可以用utf-8对响应数据进行解码
print('解码后的数据:',response.content.decode(encoding='utf-8'))