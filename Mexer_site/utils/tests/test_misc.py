import sys
from io import StringIO
from unittest.mock import patch

from django.test import TransactionTestCase
from Mexer.forms import SignupForm
from Mexer.models import EmailAuthCode, EvizUser, PassResetCode

from utils.misc import (
    Silent,
    get_plot_title,
    iea_valid,
    new_email_code,
    new_reset_code,
    time_view,
)


class MiscTests(TransactionTestCase):
    """Tests for utils/misc.py functions."""

    def test_time_view(self):
        """time_view decorator should return result and print timing."""

        @time_view
        def dummy_func():
            return "result"

        # redirect stdout
        stdout_buffer = StringIO()
        sys.stdout = stdout_buffer

        result = dummy_func()
        stdout_buffer.seek(0)

        self.assertIn("Time to run dummy_func:", stdout_buffer.read())
        self.assertEqual(result, "result")

    def test_silent(self):
        """Silent context manager should suppress stdout/stderr."""
        stdout_buf = StringIO()
        stderr_buf = StringIO()
        sys.stdout = stdout_buf
        sys.stderr = stderr_buf

        with Silent():
            print("This should be silent")
            sys.stderr.write("This should also be silent\n")

        stdout_buf.seek(0)
        stderr_buf.seek(0)

        self.assertEqual(stdout_buf.read(), "")
        self.assertEqual(stderr_buf.read(), "")

    # ugly mock to bypass CaptchaField requirement
    @patch("Mexer.forms.CaptchaField.clean", lambda _0, _1: "test")
    def test_new_email_code(self):
        """new_email_code should create inactive user and return code."""
        form = SignupForm(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "institution_type": "Academic",
                "country": "USA",
                "password1": "SuperUnbelievablySecretPasswordTheLikesOfWhichHasNeverBeforeBeenSeen12345",
                "password2": "SuperUnbelievablySecretPasswordTheLikesOfWhichHasNeverBeforeBeenSeen12345",
            }
        )
        self.assertTrue(form.is_valid())
        code = new_email_code(form)

        # Check user was created and deactivated
        user = EvizUser.objects.get(username="testuser")
        self.assertFalse(user.is_active)

        # Check code was created
        auth_code = EmailAuthCode.objects.get(code=code)
        self.assertEqual(auth_code.account, user)

    def test_new_reset_code(self):
        """new_reset_code should create password reset code."""
        user = EvizUser.objects.create_user(
            username="resetuser", email="reset@example.com", password="pass123456"
        )
        code = new_reset_code(user)

        # Check code was created
        reset_code = PassResetCode.objects.get(code=code)
        self.assertEqual(reset_code.user, user)

    def test_iea_valid(self):
        """iea_valid should check user authorization for IEA data."""
        user = EvizUser.objects.create_user(username="testuser", password="pass123456")

        # Non-IEA dataset should be valid
        query = {"dataset": "NonIEA"}
        result = iea_valid(user, query)
        self.assertTrue(result)

    def test_get_plot_title(self):
        """get_plot_title should format query dict into title string."""
        query = {"dataset": "CL-PFU IEA", "year": "2020", "country": "USA"}
        title = get_plot_title(query)

        self.assertIn("CL-PFU IEA", title)
        self.assertIn("2020", title)
        self.assertIn("USA", title)
