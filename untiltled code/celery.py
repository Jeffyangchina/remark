#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun实现异步，
import asyncio
import time

def do(x):
    print("2:",x)
class a():
    async def sec_send(self,x):
        print("Waiting2 " + str(x))

    async def first_send(self,x):
        # time.sleep(x)
        print('1:', 'a'+'\n'+'b')
        return do(x)
    #await asyncio.sleep(x)两个协程会同时执行，也可以用gather，会执行两个协程有先后，
    def gosend(self, x):
        loop = asyncio.get_event_loop()  # asyncio.gather(do_some_work(1), do_some_work(3))
        print('0:',loop)
        loop.run_until_complete(asyncio.gather(self.first_send(x), self.sec_send(x)))
    def pi(self):
        return self.gosend(3)
aa=a()
aa.pi()
# def gosend(x):
#
#     loop = asyncio.get_event_loop()#asyncio.gather(do_some_work(1), do_some_work(3))
#     loop.run_until_complete(asyncio.gather(first_send(4),sec_send(3)))
# #gosend(3)
# a()