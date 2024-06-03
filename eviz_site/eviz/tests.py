from django.test import TestCase

def test_matrix_sum(m):

    # All test values are rounded
    # as presented in the respective excel sheet 
    
    assert(m.size == 23)
    assert(round(m.get("Biomass", "Farms")) == 55362)
    assert(round(m.get("Biomass", "Feed production")) == 4047)
    assert(round(m.get("Biomass", "Food production")) == 51315)
    assert(round(m.get("Biomass [from Resources]", "Farms")) == 55362)
    assert(round(m.get("Charcoal", "Charcoal production plants")) == 16108)
    assert(round(m.get("Crude oil", "Oil refineries")) == 38104)
    assert(round(m.get("Electricity", "Main activity producer electricity plants")) == 22237)
    assert(round(m.get("Feed", "Feed production")) == 1821)
    assert(round(m.get("Food", "Food production")) == 26684)
    assert(round(m.get("Fuel oil", "Oil refineries")) == 8563)
    assert(round(m.get("Gas/diesel oil excl. biofuels", "Main activity producer electricity plants")) == 216)
    assert(round(m.get("Gas/diesel oil excl. biofuels", "Oil refineries")) == 11345)
    assert(round(m.get("Hydro", "Main activity producer electricity plants")) == 21949)
    assert(round(m.get("Hydro", "Manufacture [of Hydro]")) == 21949)
    assert(round(m.get("Hydro [from Resources]", "Manufacture [of Hydro]")) == 21949)
    assert(round(m.get("Kerosene type jet fuel excl. biofuels", "Oil refineries")) == 981)
    assert(round(m.get("Liquefied petroleum gases (LPG)", "Oil refineries")) == 426)
    assert(round(m.get("Motor gasoline excl. biofuels", "Oil refineries")) == 10349)
    assert(round(m.get("Other kerosene", "Oil refineries")) == 4292)
    assert(round(m.get("Primary solid biofuels", "Charcoal production plants")) == 50618)
    assert(round(m.get("Primary solid biofuels", "Manufacture [of Primary solid biofuels]")) == 175218)
    assert(round(m.get("Primary solid biofuels [from Resources]", "Manufacture [of Primary solid biofuels]")) == 175218)
    assert(round(m.get("Refinery gas", "Oil refineries")) == 1732)

    return "Passed all tests"