load_file_in_context("main.py")

try:
    data_matrix
except NameError:
    fail_tests("Expected `data_matrix` to be defined.")

if 'Class' in data_matrix.columns:
    fail_tests("Expected `Class` not to appear in the `data_matrix` columns.")

pass_tests()
