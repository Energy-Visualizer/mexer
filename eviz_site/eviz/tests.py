from django.test import TestCase
from eviz.utils import IndexTranslator

def test_matrix_sum(m):

    # All test values are rounded
    # as presented in the respective excel sheet 
    
    assert(m.size == 23)
    assert(round(IndexTranslator.translate(m, "Biomass", "Farms")) == 55362)
    assert(round(IndexTranslator.translate(m, "Biomass", "Feed production")) == 4047)
    assert(round(IndexTranslator.translate(m, "Biomass", "Food production")) == 51315)
    assert(round(IndexTranslator.translate(m, "Biomass [from Resources]", "Farms")) == 55362)
    assert(round(IndexTranslator.translate(m, "Charcoal", "Charcoal production plants")) == 16108)
    assert(round(IndexTranslator.translate(m, "Crude oil", "Oil refineries")) == 38104)
    assert(round(IndexTranslator.translate(m, "Electricity", "Main activity producer electricity plants")) == 22237)
    assert(round(IndexTranslator.translate(m, "Feed", "Feed production")) == 1821)
    assert(round(IndexTranslator.translate(m, "Food", "Food production")) == 26684)
    assert(round(IndexTranslator.translate(m, "Fuel oil", "Oil refineries")) == 8563)
    assert(round(IndexTranslator.translate(m, "Gas/diesel oil excl. biofuels", "Main activity producer electricity plants")) == 216)
    assert(round(IndexTranslator.translate(m, "Gas/diesel oil excl. biofuels", "Oil refineries")) == 11345)
    assert(round(IndexTranslator.translate(m, "Hydro", "Main activity producer electricity plants")) == 21949)
    assert(round(IndexTranslator.translate(m, "Hydro", "Manufacture [of Hydro]")) == 21949)
    assert(round(IndexTranslator.translate(m, "Hydro [from Resources]", "Manufacture [of Hydro]")) == 21949)
    assert(round(IndexTranslator.translate(m, "Kerosene type jet fuel excl. biofuels", "Oil refineries")) == 981)
    assert(round(IndexTranslator.translate(m, "Liquefied petroleum gases (LPG)", "Oil refineries")) == 426)
    assert(round(IndexTranslator.translate(m, "Motor gasoline excl. biofuels", "Oil refineries")) == 10349)
    assert(round(IndexTranslator.translate(m, "Other kerosene", "Oil refineries")) == 4292)
    assert(round(IndexTranslator.translate(m, "Primary solid biofuels", "Charcoal production plants")) == 50618)
    assert(round(IndexTranslator.translate(m, "Primary solid biofuels", "Manufacture [of Primary solid biofuels]")) == 175218)
    assert(round(IndexTranslator.translate(m, "Primary solid biofuels [from Resources]", "Manufacture [of Primary solid biofuels]")) == 175218)
    assert(round(IndexTranslator.translate(m, "Refinery gas", "Oil refineries")) == 1732)

    return "Passed all tests"