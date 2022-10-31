load_file_in_context("main.py")

eigenvalues_test = np.array([
    8.87463018e+00, 4.22895571e+00, 1.28105028e+00, 8.18252847e-01,
    4.38286865e-01, 1.83961749e-01, 1.11624116e-01, 5.20132000e-02,
    8.26026072e-03, 1.45388993e-03, 1.05418870e-03, 2.93982938e-04,
    1.48794566e-04, 1.00102669e-05, 1.78479176e-06, 2.14611338e-06,
])

eigenvectors_col_sum_test = [
    0.53457724, 1.77867101, -1.73058567, 0.56556397, -0.36556576,
    -1.89662994, 0.63588224, -0.08970748, -0.4396687, 1.6760161,
    -1.3009462, -0.31121506, -0.4884001, 0.04863063, -0.21022297,
    0.12562839,
]

try:
    eigenvalues

    if not np.isclose(eigenvalues, eigenvalues_test, atol=1e4).all():
        fail_tests('The values for the eigenvalues seems to be incorrect. Did you use `np.linalg.eig(a_matrix)`?')
except NameError:
    fail_tests("Expected `eigenvalues` to be defined.")

try:
    eigenvectors
    if not np.isclose(eigenvectors.sum(axis=0), eigenvectors_col_sum_test, atol=1e4).all():
        fail_tests('The values for the eigenvectors seems to be incorrect. Did you use `np.linalg.eig(a_matrix)`?')
except NameError:
    fail_tests("Expected `eigenvectors` to be defined.")

pass_tests()

