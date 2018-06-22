结构说明：

Lib：用于存放公用代码

Projects：按项目存放
    |
    |
     ——  BaseTest：自动化测试公共模块（eg:登录模块、用户管理模块、接口参数测试）
    |          |
    |	       |
    |		—— Data: 测试数据
    |	       |
    |		—— Pages：页面基础操作方法
    |	       |
    |		—— Report：测试报告
    |	       |
    |		—— TestCase：自动化测试用例
    |	       |
    |		—— TestPlan：测试用例- excel
    |	       |
    |		—— all_test.py：用例执行程序
    |	       |
    |		—— settings.py：参数配置文件
    |
    |
     ——  TXCP：（具体项目，目录结构同 BaseTest）
    |
    |
     ——  .....