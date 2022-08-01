#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Union, List


def get_request_data(file_data: Union[dict, list]) -> List[dict]:
    """
    通过解析读取的测试用例文件数据, 获取用于数据驱动的请求数据

    :param file_data: 从测试用例文件读取的测试用例数据
    :return:
    """
    # yaml
    if isinstance(file_data, dict):
        try:
            cases = file_data['test_steps']
        except KeyError:
            raise ValueError('请求测试用力数据缺少 test_steps 信息, 请检查测试用例文件内容')
        if cases is None:
            raise ValueError('请求测试用例数据缺少 test_steps 内容, 轻简查测试用例文件内容')
        elif isinstance(cases, dict):
            return [file_data]
        elif isinstance(cases, list):
            case_list = []
            for case in cases:
                if isinstance(case, dict):
                    test_steps = {'test_steps': case}
                    file_data.update(test_steps)
                    case_list.append(file_data)
                else:
                    raise ValueError('请求测试用例数据 test_steps 格式错误, 请检查测试用例文件内容')
            return case_list
    # excel
    elif isinstance(file_data, list):
        return file_data
    else:
        raise ValueError('获取请求数据失败, 传入了非法格式的测试用例数据, 请使用从测试用例文件读取的测试用例数据')
