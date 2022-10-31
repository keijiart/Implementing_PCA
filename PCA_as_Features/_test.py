load_file_in_context("main.py")

try:
    X
except NameError:
  fail_tests("Expected principal components,`X`, to exist, Did you use the method `fit_transform`?")

try:
    pca_1.n_features_
except NameError:
  fail_tests("Expected pca_1 to be fit and transformed using `fit_transform`.")

pass_tests()
