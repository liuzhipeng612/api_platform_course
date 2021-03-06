from django.db.models import Count

from configures.models import Configures
from interfaces.models import Interfaces
from testcases.models import Testcases


def get_class_time_formatting(class_datas):
    create_time = class_datas.create_time
    create_time_split = str(create_time).split('.')
    create_time_index = create_time_split[0]
    class_datas.create_time = create_time_index

    return class_datas


def get_count_by_interface(datas):
    for item in datas:
        create_time_list = item.get('create_time').split('T')
        first_part = create_time_list[0]
        second_part = create_time_list[1].split('.')[0]
        item['create_time'] = first_part + ' ' + second_part

        # 获取项目ID值
        get_interface_id = item['id']

        # 当前项目的用例总数
        interfaces_testcases = Testcases.objects.filter(interface_id=get_interface_id).count()

        # 当前项目的配置总数
        interfaces_configures = Configures.objects.filter(interface_id=get_interface_id).count()

        # 更新datas
        item['create_time'] = item['create_time']
        item['testcases'] = interfaces_testcases
        item['configures'] = interfaces_configures

    return datas
