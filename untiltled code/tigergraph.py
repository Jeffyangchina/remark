#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from py2neo import Graph,Node,Relationship
tf=Graph("http://localhost:7474", username="crunchbase_pre_2013", password="crunchbase_pre_2013")
def init(person_first_name, person_last_name, attended_university_name, degree, subject, graduation_date):
    Person_node=Node(label='Person',)
def get_end_nodes(graph,EdgeName,FirstNodeName,EndNodeName):
    NodeList=[]
    lists = graph.match(rel_type=EdgeName, start_node=FirstNodeName, bidirectional=False)
    for nd in lists:
        EndNode=nd.end_node()[EndNodeName]
        if EndNode not in NodeList:
            NodeList.append(EndNode)
    return NodeList
def get_node(LabelName,NodeValue,graph,NodeProperty):
    node1 = graph.find_one(label=LabelName, property_key=NodeProperty, property_value=NodeValue)