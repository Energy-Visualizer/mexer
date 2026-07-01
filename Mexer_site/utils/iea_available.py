from collections.abc import MutableMapping

type ShapedQuery = MutableMapping[str, str | list[str]]


def can_all_users_access(query: ShapedQuery) -> bool:
    """This function determines whether a request from a non-IEA-authorized
    user can access IEA data. The conditions in this function's code should
    describe the IEA data which is available to all users.

    This function may:
      - Allow the request through, returning True, which means "allow".
      - Modify the disallowed query to a narrower allowed query,
        returning True, which means "allow".
      - Reject the query, returning False, which means "disallow"."""

    # Currently, no IEA data is known to be available
    # to all users.
    return False


# See example access conditions below.


def example_can_all_users_access(query: ShapedQuery) -> bool:
    """This function makes IEA data from the UK from years 2016-2019
    available to anybody."""

    # Only queries in the UK region are allowed.
    # TODO: region aggregation info could allow
    # narrowing to the UK.
    valid_country = False

    # country__in is the Django query keyword for lists of selected options.
    # This constrains the country to just the UK.
    if "country__in" in query and "United Kingdom" in query["country__in"]:
        valid_country = True
        query["country__in"] = ["United Kingdom"]

    if "country" in query and "United Kingdom" == query["country"]:
        valid_country = True

    # Also, only queries from the years 2016-2019 are allowed.
    valid_year = False

    if "year" in query and query["year"] in ("2016", "2017", "2018", "2019"):
        valid_year = True

    # year__gte and year__lte are the Django query keywords for ranges of numbers.
    if "year__gte" in query and "year__lte" in query:
        if int(query["year__gte"]) < 2016:
            query["year__gte"] = "2016"  # Query values must be strings.
        if int(query["year__lte"]) > 2019:
            query["year__lte"] = "2019"
        valid_year = True

    valid = valid_country and valid_year
    return valid
