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

    # If country is omitted or UK is present,
    # restrict to just UK.
    if "country" not in query or "United Kingdom" in query["country"]:
        query["country__in"] = ["United Kingdom"]
    else:
        # Invalid country specified; no data.
        return False

    # Also restrict year range.
    if "year" in query:
        from_year = int(query["year"])
        if from_year < 2016:
            query["year"] = "2016"
    if "to_year" in query:
        to_year = int(query["to_year"])
        if to_year > 2019:
            query["year"] = "2019"

    return True
