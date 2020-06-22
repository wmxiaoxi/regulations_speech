import allure
import pytest
from common.config import *
from common.base import *
class Test_checkA():
    @allure.story("关键字查询")
    #@pytest.mark.parametrize('searchWord',['总局关于创建','国家广播电视','广播电视媒体'])
    @pytest.mark.parametrize('searchWord', ['总局关于创建',])
    def test_01(self,searchWord):
        data={"implementationYear":"","page":1,"regulationsScope":"全部","rows":10,"searchWord":searchWord}
        content_api=post(host1+addr1,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from police_laws_regulations  where name like '%"+searchWord+"%' or  issuer like '%"+searchWord+"%' or targets like'%"+searchWord+"%'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]




    @allure.story('时间查询')
    @pytest.mark.parametrize("implementationYear",['2019'])
    def test_02(self,implementationYear):
        data={"implementationYear":"","page":1,"regulationsScope":"全部","rows":10,"searchWord":""}
        content_api=post(host1+addr1,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from police_laws_regulations where to_char(implementation_time,'yyyy')='"+implementationYear+"'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]



    @allure.story('类型查询')
    @pytest.mark.parametrize("regulationsScope",['全部','全国','地方'])
    def test_02(self,regulationsScope):
        data = {"implementationYear": "", "page": 1, "regulationsScope": regulationsScope, "rows": 10, "searchWord": ""}
        content_api=post(host1+addr1,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from police_laws_regulations where regulations_scope='"+regulationsScope+"'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]



    @allure.story("关键字+时间查询+类型")
    @pytest.mark.parametrize('searchWord', ['总局关于创建', '国家广播电视', '广播电视媒体'])
    @pytest.mark.parametrize("implementationYear", ['2019'])
    @pytest.mark.parametrize("regulationsScope", ['全部', '全国', '地方'])
    def test_03(self,implementationYear,searchWord,regulationsScope):
        data={"implementationYear":implementationYear,"page":1,"regulationsScope":regulationsScope,"rows":10,"searchWord":searchWord}
        content_api=post(host1+addr1,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from (select * from police_laws_regulations where name like '%"+searchWord+"%' or  issuer like '%"+searchWord+"%' or targets like '%"+searchWord+"%')aa where aa.to_char(implementation_time,'yyyy')='"+implementationYear+"' and aa.regulations_scope='"+regulationsScope+"'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]




    @allure.story('查询全部得数据')
    def test_02(self):
        data = {"implementationYear": "", "page": 1, "regulationsScope": "全部", "rows": 10, "searchWord": ""}
        content_api = post(host1 + addr1, data, headers)
        count = content_api['content']['count']
        sql ="select count(*) from police_laws_regulations"
        count_sql = sqlcheck(sql)
        assert count == count_sql[0][0]





    @allure.story("分页查询")
    @pytest.mark.parametrize('page', ['2', ])
    def test_03(self,page):
        data = {"implementationYear": "", "page": page, "regulationsScope": "全部", "rows": 10, "searchWord": ""}
        content_api = post(host1 + addr1, data, headers)
        assert content_api['code'] == 0




    @allure.story("一页显示条数")
    @pytest.mark.parametrize('rows', ['20', ])
    def test_04(self,rows):
        data = {"implementationYear": "", "page": 1, "regulationsScope": "全部", "rows": rows, "searchWord": ""}
        content_api = post(host1 + addr1, data, headers)
        assert content_api['code'] == 0
        assert len(content_api['content']['value']) == 20


if __name__=="__main__":
    pytest.main(["-s","test_regulations.py"])