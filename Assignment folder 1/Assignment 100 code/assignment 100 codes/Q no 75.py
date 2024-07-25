import timeit

setup_code = "a = 1"
test_code = "a + 1"

running_time = timeit.timeit(setup=setup_code, stmt=test_code, number=100)
print("Running time:", running_time)