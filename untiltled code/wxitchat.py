#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import itchat, time
itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.send_msg("hello world.")
user=itchat.search_mps(name='金桥')
itchat.logout()