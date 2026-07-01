from django.contrib.auth.models import AnonymousUser
from django.test import TransactionTestCase

from ..iea_available import can_all_users_access
from ..misc import ShapedQuery, iea_valid


class FreeIEATests(TransactionTestCase):
    def reject_all_iea(self):
        free_data = can_all_users_access({})
        self.assertFalse(free_data)

    def non_iea_exempt(self):
        query: ShapedQuery = {"dataset": "CL-PFU MW"}

        # Technically, a free data check will fail.
        # The free data check assumes we've determined it's an IEA query.
        free_data = can_all_users_access(query)
        self.assertFalse(free_data)

        # But the query is still valid for any user,
        # because the data is not IEA.
        user = AnonymousUser()
        can_access = iea_valid(user, query)
        self.assertTrue(can_access)
