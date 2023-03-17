# nacos_vul
Nacos身份认证绕过批量检测（QVD-2023-6271）+ 直接添加用户

nacosvul.py用于漏洞批量检测，nacosadd.py用于一键添加用户

nacosvul批量检测截图：

![image](https://user-images.githubusercontent.com/88339946/225786466-6d0aa102-71f3-4a1a-a945-4cf3a2b8aecc.png)

由于secret.key值为默认，可生成可用的token登录到系统里

![image](https://user-images.githubusercontent.com/88339946/225548462-4b086984-0862-4b75-a722-24ad5ffd41d5.png)

脚本根据已公开内容编写，仅为安全研究测试提供参考～ 

使用时请注意遵守相关法律规定！本工具仅供学习和已授权情况下的安全测试，帮助发现修复漏洞

本项目包含poc和exp，未经授权禁止攻击他人机器。如个人违反安全相关法律，后果与本人无关

参考链接：

https://github.com/alibaba/nacos/issues/7182

https://mp.weixin.qq.com/s/5lE_9I6-r1CE8CYtUZG1rQ
