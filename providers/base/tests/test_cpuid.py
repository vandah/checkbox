# Copyright 2024 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import unittest

from unittest.mock import MagicMock, patch

from cpuid import cpuid_to_human_friendly, main


class CpuidTests(unittest.TestCase):
    def test_hygon_dhyana_plus(self):
        self.assertEqual(
            cpuid_to_human_friendly("0x900f22"), "Hygon Dhyana Plus"
        )

    def test_hygon_C86_4G_7490(self):
        self.assertEqual(
            cpuid_to_human_friendly("0x900f41"), "Hygon C86-4G 7490"
        )

    def test_unknown_throws(self):
        with self.assertRaises(ValueError):
            cpuid_to_human_friendly("0xdeadbeef")


class CpuidMainTests(unittest.TestCase):
    @patch("builtins.print")
    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_hygon_dhyana_plus(self, cpuid_mock, co_mock, print_mock):
        call_mock = MagicMock()
        call_mock.return_value = [0x900F22, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        main()
        expected_msg = "CPUID: {} which appears to be a {} processor".format(
            "0x900f22", "Hygon Dhyana Plus"
        )
        print_mock.assert_called_with(expected_msg)

    @patch("builtins.print")
    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_hygon_hygon_C86_4G_7490(self, cpuid_mock, co_mock, print_mock):
        call_mock = MagicMock()
        call_mock.return_value = [0x900F41, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        main()
        expected_msg = "CPUID: {} which appears to be a {} processor".format(
            "0x900f41", "Hygon C86-4G 7490"
        )
        print_mock.assert_called_with(expected_msg)

    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_unknown_cpu(self, cpuid_mock, co_mock):
        call_mock = MagicMock()
        call_mock.return_value = [0xDEADBEEF, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        with self.assertRaises(SystemExit):
            main()

    @patch("builtins.print")
    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_raptor_lake(self, cpuid_mock, co_mock, print_mock):
        call_mock = MagicMock()
        call_mock.return_value = [0xB0671, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        main()
        expected_msg = "CPUID: {} which appears to be a {} processor".format(
            "0xb0671", "Raptor Lake"
        )
        print_mock.assert_called_with(expected_msg)

    @patch("builtins.print")
    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_emerald_rapids(self, cpuid_mock, co_mock, print_mock):
        call_mock = MagicMock()
        call_mock.return_value = [0xC06F2, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        main()
        expected_msg = "CPUID: {} which appears to be a {} processor".format(
            "0xc06f2", "Emerald Rapids"
        )
        print_mock.assert_called_with(expected_msg)

    @patch("builtins.print")
    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_meteor_lake(self, cpuid_mock, co_mock, print_mock):
        call_mock = MagicMock()
        call_mock.return_value = [0xA06A4, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        main()
        expected_msg = "CPUID: {} which appears to be a {} processor".format(
            "0xa06a4", "Meteor Lake"
        )
        print_mock.assert_called_with(expected_msg)

    @patch("builtins.print")
    @patch("subprocess.check_output")
    @patch("cpuid.CPUID")
    def test_amd_siena_sp6(self, cpuid_mock, co_mock, print_mock):
        # import pdb; pdb.set_trace()
        call_mock = MagicMock()
        call_mock.return_value = [0xAA0F02, 0x0, 0x0, 0x0]
        cpuid_mock.return_value = call_mock
        co_mock.return_value = ""
        main()
        expected_msg = "CPUID: {} which appears to be a {} processor".format(
            "0xaa0f02", "AMD Siena SP6"
        )
        print_mock.assert_called_with(expected_msg)
