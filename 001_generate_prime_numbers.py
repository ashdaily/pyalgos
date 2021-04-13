# -*- coding: utf-8 -*-
"""Generating list of prime numbers using Sieve Eratosthene.

Arguments available:
- N : the max number until which you wish to find the list of prime numbers.
"""

import argparse
from math import sqrt

from pprint import pprint


class Generator:
	def __init__(self, N):
		self.arr = list(range(1, N+1))
		self.arr_size = N

	def remove_divisible_by(self, x: int):
		for i in self.arr:
			if i == x:
				continue
			if i % x == 0:
				self.arr.remove(i)
	
	@property
	def prime_numbers(self):
		for i in range(2, int(sqrt(self.arr_size)+1)):
			self.remove_divisible_by(i)
	
		return self.arr


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--N",help="array size ", type=int)
	args = parser.parse_args()
	
	N = args.N
	g = Generator(N)
	pprint(g.prime_numbers,compact=True)