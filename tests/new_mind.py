# -*- coding: utf-8 -*-
"""
飞书无法导入 freemind 文件
"""
import json
import xml.etree.ElementTree as ET
from typing import Callable


def exmaple():
    """
    示例
    """
    # 创建根节点
    root = ET.Element('map')

    # 创建子节点1
    node1 = ET.SubElement(root, 'node', TEXT='Parent Node')
    ET.SubElement(node1, 'node', TEXT='Child Node 1')
    ET.SubElement(node1, 'node', TEXT='Child Node 2')

    # 创建子节点2
    node2 = ET.SubElement(root, 'node', TEXT='Another Parent Node')
    ET.SubElement(node2, 'node', TEXT='Child Node 3')
    ET.SubElement(node2, 'node', TEXT='Child Node 4')

    # 创建XML文档
    tree = ET.ElementTree(root)

    # 将XML文档保存为Freemind文件
    tree.write('my_map.mm', encoding='utf-8')


dps_map = {}
dps_tree = {}


def print_tree(data, datashow: Callable, indent=0):
    """print tree"""
    for key, value in data.items():
        print(' ' * indent + datashow(key))
        if isinstance(value, dict):
            print_tree(value, datashow, indent + 2)
        else:
            print(' ' * (indent + 2) + datashow(value))


def load_department_data():
    """
    清洗数据
    """
    parent_node = {}

    with open("./tmp/xtalpi_department.json", encoding="UTF-8") as file:
        departments = json.load(file)["data"]
        for department in departments:
            dps_map[str(department["oId"])] = department

        for department in departments:
            o_ids = department["pOIdOrgAdmin_TreePath"].split("/")

            for ix, o_id in enumerate(o_ids):
                if ix == 0:
                    parent_node = dps_tree
                else:
                    for i in range(0, ix):
                        if i == 0:
                            parent_node = dps_tree[o_ids[i]]
                        else:
                            # last parent node is exist
                            parent_node = parent_node[o_ids[i]]

                if o_id not in parent_node:
                    parent_node[o_id] = {}
    # print(dps_tree)

    with open("./tmp/xtalpi_department_ids_tree.json", mode="w", encoding="UTF-8") as file:
        json.dump(dps_tree, file)

    print_tree(dps_tree, lambda x: dps_map[str(x)]["name"])


load_department_data()
