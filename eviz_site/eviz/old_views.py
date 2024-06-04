# This file exists to store old views,
# either for later reference or to be rebuilt later,
# that shouldn't be lumped with the current views in views.py

# # TODO: hide this test
# @time_view
# def la_extraction(request):

#     # TODO: broken after moving to a2
#     test_mat_context = {
#         "dataset": "CLPFUv2.0a1",
#         "country": "GHA",
#         "method": "PCM",
#         "energy_type": "E",
#         "last_stage": "Final",
#         "ieamw": "Both",
#         "includes_neu": True,
#         "year": 1995,
#     }

#     u = get_matrix(
#         **test_mat_context
#     )
#     v = get_matrix(
#         **test_mat_context
#     )

#     sum = u.T + v

#     s = str(sum).splitlines()

#     context = { "passed": test_matrix_sum(sum), "sum": s }

#     return render(request, "./la_extract.html", context)