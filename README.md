# nacos_vul
Nacos身份认证绕过批量检测（QVD-2023-6271）

由于secret.key值为默认，可生成可用的token登录到系统里

![image](https://user-images.githubusercontent.com/88339946/225548462-4b086984-0862-4b75-a722-24ad5ffd41d5.png)

扫描截图：

![image](https://user-images.githubusercontent.com/88339946/225786466-6d0aa102-71f3-4a1a-a945-4cf3a2b8aecc.png)


脚本根据已公开内容编写，仅对目标进行漏洞检测，无实质危害，仅为安全研究提供参考～ 

使用时请注意遵守相关法律规定！本工具仅供学习和已授权情况下的安全测试，帮助发现修复漏洞

参考链接：

https://github.com/alibaba/nacos/issues/7182

https://mp.weixin.qq.com/s/5lE_9I6-r1CE8CYtUZG1rQ
