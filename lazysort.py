import itertools
import random
import heapq

def lazy_sort(col):
	def swap(i, j):
		if i != j:
			col[j], col[i] = col[i], col[j]

	def prepare_pivot(l, r):
		p_index = random.randint(l, r)
		swap(l, p_index)

	def partition(l, r):
		prepare_pivot(l, r)
		p = col[l]

		i = l + 1
		for j in range(l + 1, r + 1):
			if col[j] < p:
				swap(i, j)
				i += 1
		swap(l, i - 1)
		return i

	size = len(col)
	last_yield = 0	
	h = []
	heapq.heappush(h, (0, size - 1))

	while h:
		l, r = heapq.heappop(h)
		if l > last_yield:
			for x in range(last_yield, l):
				yield col[x]
			last_yield = l

		i = partition(l, r)

		if l < i - 2:
			heapq.heappush(h, (l, i - 2))
		if i < r:
			heapq.heappush(h, (i, r))

	for x in range(last_yield, size):
		yield col[x]

def get_shuffled_array(n=100):
	rand_array = [i for i in range(n)]
	random.shuffle(rand_array)
	return rand_array

def sort_first(l, algorithm):
	return list(itertools.islice(algorithm(l), len(l)))

def test_lazy_sort():
	return sort_first(get_shuffled_array(), lazy_sort)

def test_sort():
	return sort_first(get_shuffled_array(), sorted)

print(test_lazy_sort())
