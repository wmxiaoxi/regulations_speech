import allure
import pytest
from common.config import *
from common.base import *
class Test_checkA():
    @allure.story("关键字查询")
    @pytest.mark.parametrize('searchWord',['全面从严治','聂辰席','党组书记','从严治党'])
    def test_01(self,searchWord):
        data={"implementationYear": "", "page": 1, "rows": 10, "searchWord": searchWord}
        content_api=post(host1+addr,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from police_important_speech where leader_name like '%"+searchWord+"%' or  important_hint like '%"+searchWord+"%' or position like '%"+searchWord+"%' or scenes like '%"+searchWord+"%' or targets like '%"+searchWord+"%'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]




    @allure.story('时间查询')
    @pytest.mark.parametrize("implementationYear",['2019'])
    def test_02(self,implementationYear):
        data = {"implementationYear": implementationYear, "page": 1, "rows": 10, "searchWord": ""}
        content_api=post(host1+addr,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from police_important_speech where to_char(date,'yyyy')='"+implementationYear+"'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]


    @allure.story("关键字+时间查询")
    @pytest.mark.parametrize('searchWord', ['全面从严治', '聂辰席', '党组书记', '从严治党'])
    @pytest.mark.parametrize("implementationYear", ['2019'])
    def test_03(self,implementationYear,searchWord):
        data={"implementationYear": implementationYear, "page": 1, "rows": 10, "searchWord": searchWord}
        content_api=post(host1+addr,data,headers)
        count=content_api['content']['count']
        sql="select count(*) from (select * from police_important_speech where leader_name like '%"+searchWord+"%' or  important_hint like '%"+searchWord+"%' or position like '%"+searchWord+"%' or scenes like '%"+searchWord+"%' or targets like '%"+searchWord+"%')aa where aa.to_char(date,'yyyy')='"+implementationYear+"'"
        count_sql=sqlcheck(sql)
        assert count == count_sql[0][0]




    @allure.story('查询全部得数据')
    def test_02(self):
        data = {"industry": "", "page": 1, "priceType": "全部", "rows": 10, "searchWord": "", "target": "", "type": "",
                "year": 0}
        content_api = post(host1 + addr, data, headers)
        count = content_api['content']['count']
        sql ="select count(*) from police_important_speech"
        count_sql = sqlcheck(sql)
        assert count == count_sql[0][0]



    @allure.story("分页查询")
    @pytest.mark.parametrize('page',['2',])
    def test_03(self,page):
        data = {"industry": "", "page": page, "priceType": "全部", "rows": 10, "searchWord": "", "target": "", "type": "",
                "year": 0}
        content_api = post(host1 + addr, data, headers)
        assert content_api['code'] == 0




    @allure.story("一页显示条数")
    @pytest.mark.parametrize('rows', ['20', ])
    def test_04(self,rows):
        data = {"industry": "", "page": 1, "priceType": "全部", "rows": rows, "searchWord": "", "target": "", "type": "",
                "year": 0}
        content_api = post(host1 + addr, data, headers)
        assert content_api['code'] == 0
        assert len(content_api['content']['value']) == 20


if __name__=="__main__":
    pytest.main(["-s","test_speech.py"])