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

# def visualizer(request):

#     agg_query = AggEtaPFU.objects.filter(
#         Dataset = 3,
#         Country = 5,
#         Method = 1,
#         EnergyType = 2,
#         LastStage = 2,
#         IEAMW = 1,
#         IncludesNEU = 0,
#         ChoppedMat = 28,
#         ChoppedVar = 2728,
#         ProductAggregation = 1,
#         IndustryAggregation = 1,
#         GrossNet = 1
#     ).values("Year", "EXp", "EXf", "EXu", "etapf", "etafu", "etapu").query

#     # TODO: pandas only defines support for SQLAlechemy connection, it currently works with psycopg2, but could be dangerous
#     with Silent():
#         df = pd_sql.read_sql_query(str(agg_query), con=connection.cursor().connection) # clunky, but gives access to the low-level psycopg2 connection

#     scatterplot = px.scatter(
#         df, x = "Year", y = "etapu",
#         title="Efficiency of primary to useful by year for random query",
#         template="plotly_dark"
#     )
    
#     # idea for visualization rendering from this site: https://www.codingwithricky.com/2019/08/28/easy-django-plotly/
#     p = plot(scatterplot, output_type="div", include_plotlyjs="cdn")
    
#     return render(request, "viz.html", context={"plot":p})