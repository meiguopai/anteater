TXCP 腾讯版权使用说明：

1、Data目录存放文件：(文件地址：\\192.168.142.199\Test\测试数据\TXCP_Data.rar)

	模板文件:offline_result.xls/tx_offline.xls/already_letter_result.xls
	sql文件：t_offline_need.sql/t_offline_record.sql/t_tort_record.sql

2、执行测试：
	
	a.根据需要可修改all_test.py文件中的基本参数值，如：AllTestParamSet类中的TEST_NUM等
	b.直接运行all_test.py文件

3、测试结果：

	结果除发送到邮箱外，TXCP/Report目录下保存all_test执行结果文件，可直接查看


PS:
	a.修改测试数据库连接：DB目录下OperateDB.py -> mysql_excute()
	b.如有模块未导入如：pykeyboard模块或Chromedriver版本(Chromedriver下载完成放在python安装目录下即可)等问题可参照开发手册：
	\\192.168.142.199\Test\测试基础文档\自动化测试\讯思雅-自动化测试框架-开发使用文档.doc