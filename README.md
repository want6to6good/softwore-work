# Software-Engineering
## 后端

启动:

先安装conda环境, 然后在`/recruit`目录下
```bash
conda create --name JobSystem python=3.7.9 # 创建虚拟环境, 经测试, 不是这个python版本可能会出兼容性问题
conda activate JobSystem # 启动虚拟环境
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# 如果需要退出:
conda deactivate
```
在runserver后访问http://127.0.0.1:8000/xadmin/

创建用户:
在/recruit目录下运行 (确保处于conda或能正常运行runserver的python环境)
```
python manage.py createsuperuser
```
根据提示创建用户即可.

## 前端
- npm 版本: 8.19.4
- node 版本: v16.20.2

理论上版本差异问题不大, 但是如果之前没装过npm和node还是按以上版本装吧.

进入`/frontend`目录, 运行`npm install`, 

可能会遇到https://registry.npm.taobao.org/ 过期的问题, 参考[这篇文章](https://juejin.cn/post/7336466381801324607)解决

首先删除 node_modules 文件夹, 清空 npm 缓存, 并更换镜像源:

```
rm -rf node_modules
npm cache clean --force
npm config set registry https://registry.npmmirror.com
```
这样可能还是无法解决, 接下来张麟浩同学的办法是把package-lock.json里所有淘宝源的地址换成新源 (推荐), 我的办法是按文章中最后的办法把npm的ssl检查关了 (不推荐).

接下来可能会遇到gyp ERR, 参考[这篇博客](https://github.com/nodejs/node-gyp/tree/main/docs#readme), 运行
```
npm uninstall node-sass
npm install sass --save
```
再运行
```
npm install
```
应该能解决.

Compiles and hot-reloads for development:
```
npm run serve
```

然后访问http://localhost:8080/login, 注册->可以在后端看到USER信息->登录


Compiles and minifies for production:
```
npm run build
```

计划支持的路由:
- update/: 用于更改简历投递状态, put请求, 参数: 
  - application_id: 职位申请的id
  - status: 申请状态, 以下三种:
    - 'applied', '已申请'
    - 'hired', '已录用'
    - 'rejected', '已拒绝'
- create/: 创建新的工作岗位, post请求, 参数:
  - title: 工作名称
  - description: 工作描述
  - company_id: 公司的id 
  - loaction: 工作地点
  - salary: 薪资
- change_resume/: 更改简历, post请求, 参数: 
  - jobseeker_id: 求职者id 
  - education:教育经历 
  - experience: 工作经历 
  - skills: 技能 
  - projects: 项目经历 
  - certifications: 认证和证书
- job/: 返回工作列表 (返回的参数同update, 但是多了一个posted_date: 发布日期) 
- application/: (带参数job_id或jobseeker_id, hr查看带job_id,求职者查看带jobseeker_id)返回参数 job, jobseeker, applied_date, status
返回求职者 or hr or 公司数据 (应该用不到) 
- jobseeker/
- hr/
- company/

一个笔记: 我们项目中可以登录的 (存储在db.sqlite3中)
- 后端, 帐号: wanghao, 密码: 123456
- 前端, 帐号: test_seeker, 密码: 123456
- 前端, 帐号: aaaaaa, 密码: 456789

参考项目中可以登录的 (未上传)
- 后端, 帐号: wanghao, 密码: 123456
- 前端, 帐号: 789456123, 密码: wang250188
