'''
Desc:
File: /cached.py
Project: learn-gin
File Created: Wednesday, 6th September 2023 8:30:56 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2023 Camel Lu
'''

import time
import threading
from cachetools import cached, LRUCache, TTLCache, LFUCache,RRCache
 
def compare_cache():
  # without cached
  def fib(n):
      return n if n < 2 else fib(n - 1) + fib(n - 2)
  
  
  s = time.time()
  print(fib(36))
  print("Time Taken:", time.time() - s)
  
  # Now using cached
  s = time.time()
  
  
  # Use this decorator to enable caching
  @cached(cache={})
  def fib(n):
      return n if n < 2 else fib(n - 1) + fib(n - 2)
  
  
  print(fib(36))
  print("Time Taken(cached): ", time.time() - s)


def use_lru():
  @cached(cache=LRUCache(maxsize=3))
  def my_fun(n):
      # This delay resembles some task
      s = time.time()
      time.sleep(n)
      print("\nTime Taken: ", time.time() - s)
      return f"I am executed: {n}"
  
  
  # Takes 3 seconds
  print(my_fun(3))

  # Takes no time
  print(my_fun(3))

  # Takes 2 seconds
  print(my_fun(2))
  
  # Takes 1 second
  print(my_fun(1))
  
  # Takes 4 seconds
  print(my_fun(4))

  
  # Takes no time
  print(my_fun(1))
  
  # Takes 3 seconds because maxsize = 3
  # and the 3 recent used functions had 1,
  # 2 and 4.
  print(my_fun(3))

def use_ttl():
  # Here recent 32 functions
  # will we stored for 1 minutes
  @cached(cache=TTLCache(maxsize=32, ttl=25))
  def my_fun(n):
      # This delay resembles some task
      s = time.time()
      time.sleep(n)
      print("\nTime Taken: ", time.time() - s)
      return f"I am executed: {n}"
  
  
  print(my_fun(3))
  print(my_fun(3))
  print("*" * 100)
  
  time.sleep(24)
  print(my_fun(3))
  print("*" * 100)
  
  time.sleep(26)
  print(my_fun(3))

# use_ttl()

def use_lock():
  custom_lock = threading.Lock()

  @cached(cache=TTLCache(maxsize=10, ttl=10), lock=custom_lock)
  def slow_calculation(n):
      print(f"Performing slow calculation for {n}...")
      start_time = time.time()
      nn = n
      i = 0
      while i < 1000:
          time.sleep(0.01)
          n += i
          i += 1
      end_time = time.time()
      print(f"{nn}线程耗时1：{end_time - start_time}")
      return n
  
  
  @cached(cache=TTLCache(maxsize=10, ttl=10))
  def slow_calculation2(n):
      print(f"Performing slow calculation for {n}...")
      start_time = time.time()
      nn = n
      i = 0
      while i < 1000:
          time.sleep(0.01)
          n += i
          i += 1
      end_time = time.time()
      print(f"{nn}线程耗时2：{end_time - start_time}")
      return n
  
  def task(n):
      ret = slow_calculation(n)
      time.sleep(3)
      slow_calculation(n)
      print(f"{n}线程执行结果ret:{ret}")
      ret2 = slow_calculation2(n)
      time.sleep(5)
      slow_calculation2(n)
      print(f"{n}线程执行结果ret2:{ret2}")
      # print(f"{n}线程执行结果ret1:{ret},ret2:{ret2}")
  
  
  def run_threads():
      threads = []
      for i in range(5):
          t = threading.Thread(target=task, args=(i,))
          threads.append(t)
          t.start()
  
      for t in threads:
          t.join()

  start_time = time.time()
  run_threads()
  end_time = time.time()
  print(f"总耗时：{end_time - start_time}")

def use_lfu():
  @cached(cache=LFUCache(maxsize=3))
  def my_fun(n):
      # This delay resembles some task
      s = time.time()
      time.sleep(n)
      print("\nTime Taken: ", time.time() - s)
      return f"I am executed: {n}"
  print(my_fun(3))
  print(my_fun(3))
  print(my_fun(1))
  print(my_fun(4))
  print(my_fun(2))
  print(my_fun(2))
  print(my_fun(1))
  print(my_fun(3))
  print(my_fun(3))
  print(my_fun(4))
  print(my_fun(4))
  print(my_fun(1))
  print(my_fun(2))

# use_lfu()

def use_rr():
  @cached(cache=RRCache(maxsize=3))
  def my_fun(n):
      # This delay resembles some task
      s = time.time()
      time.sleep(n)
      print("\nTime Taken: ", time.time() - s)
      return f"I am executed: {n}"
  print(my_fun(3))
  print(my_fun(3))
  print(my_fun(2))
  print(my_fun(4))
  print(my_fun(1))
  print(my_fun(1))
  print(my_fun(3))
  print(my_fun(2))
  print(my_fun(3))

use_rr()
