from django.http import HttpResponse
from eviz.models import PSUT
from django.shortcuts import render
from django.db.models import Sum, Avg, Max
from eviz.utils import time_view

@time_view
def eviz_index(request):

    #rows = PSUT.objects.select_related('LastStage','Country','Method', 'EnergyType','IEAMW', 'IncludesNEU', 'Year', 'matname', 'Dataset',"i",'j').filter(EnergyType__EnergyTypeID=1)[:10]
    #sql_query = str(rows.query)
                        
    # rows = PSUT.objects.select_related('i','j')\
    #     .filter(Dataset__Dataset= 'CLPFUv2.0a1', Country__Country= 'GHA', Method__Method= 'PCM', EnergyType__EnergyType= 'X', LastStage__ECCStage= 'Final', IEAMW__IEAMW='IEA', IncludesNEU__IncludesNEU=1, Year__Year=2015, matname__matname='R' )\
    #     .values('i__Index','j','x')
    
    R_matrix1 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='GHA', Method__Method='PCM', EnergyType__EnergyType='X', LastStage__ECCStage='Final', IEAMW__IEAMW='IEA', IncludesNEU__IncludesNEU=True, Year__Year=2015, matname__matname='R')\
    .values('i__Index', 'j__Index', 'x','i','j')
    
    sql_query = str(R_matrix1.query)
    
    U_matrix1 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='GHA', Method__Method='PCM', EnergyType__EnergyType='X', LastStage__ECCStage='Final', IEAMW__IEAMW='IEA', IncludesNEU__IncludesNEU=True, Year__Year=2015, matname__matname='U')\
    .values('i__Index', 'j__Index', 'x','i','j')

    V_matrix1 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='GHA', Method__Method='PCM', EnergyType__EnergyType='X', LastStage__ECCStage='Final', IEAMW__IEAMW='IEA', IncludesNEU__IncludesNEU=True, Year__Year=2015, matname__matname='V')\
    .values('i__Index', 'j__Index', 'x','i','j')
    
    Y_matrix1 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='GHA', Method__Method='PCM', EnergyType__EnergyType='X', LastStage__ECCStage='Final', IEAMW__IEAMW='IEA', IncludesNEU__IncludesNEU=True, Year__Year=2015, matname__matname='Y')\
    .values('i__Index', 'j__Index', 'x','i','j')
   

    
    
    R_matrix2 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='ZAF', Method__Method='PCM', EnergyType__EnergyType='E', LastStage__ECCStage='Useful', IEAMW__IEAMW='Both', IncludesNEU__IncludesNEU=False, Year__Year=1997, matname__matname='R')\
    .values('i__Index', 'j__Index', 'x','i','j')
    
    U_matrix2 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='ZAF', Method__Method='PCM', EnergyType__EnergyType='E', LastStage__ECCStage='Useful', IEAMW__IEAMW='Both', IncludesNEU__IncludesNEU=False, Year__Year=1997, matname__matname='U')\
    .values('i__Index', 'j__Index', 'x','i','j')

    V_matrix2 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='ZAF', Method__Method='PCM', EnergyType__EnergyType='E', LastStage__ECCStage='Useful', IEAMW__IEAMW='Both', IncludesNEU__IncludesNEU=False, Year__Year=1997, matname__matname='V')\
    .values('i__Index', 'j__Index', 'x','i','j')
    
    Y_matrix2 = PSUT.objects.select_related('Country', 'Method', 'EnergyType', 'LastStage', 'IEAMW', 'IncludesNEU', 'Year', 'matname', 'i', 'j')\
    .filter(Dataset__Dataset='CLPFUv2.0a1', Country__Country='ZAF', Method__Method='PCM', EnergyType__EnergyType='E', LastStage__ECCStage='Useful', IEAMW__IEAMW='IEA', IncludesNEU__IncludesNEU=False, Year__Year=1997, matname__matname='Y')\
    .values('i__Index', 'j__Index', 'x','i','j')
    
    
    context = { "R_matrix1": R_matrix1,
               "sql_query": sql_query,
               "U_matrix1": U_matrix1,
               "V_matrix1": V_matrix1,
               "Y_matrix1": Y_matrix1,
               "R_matrix2": R_matrix2,
               "U_matrix2": U_matrix2,
               "V_matrix2": V_matrix2,
               "Y_matrix2": Y_matrix2}

    return render(request, "./test.html", context)