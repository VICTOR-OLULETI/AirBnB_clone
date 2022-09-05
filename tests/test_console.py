"""This program contain tests for the console.py program"""

import unittest
import os
import console
from io import StringIO
from unittest.mock import patch
from re import search
import pycodestyle as pep8
import inspect


class TestConsole(unittest.TestCase):
    """Class to test the console"""
    def test_pep8_conformance_console(self):
        """Test that console conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        output = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, output)

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_fiel_HBNBCommand_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(console.HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(console.HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(console.HBNBCommand, "do_create"))
        self.assertTrue(hasattr(console.HBNBCommand, "do_show"))
        self.assertTrue(hasattr(console.HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(console.HBNBCommand, "do_update"))
        self.assertTrue(hasattr(console.HBNBCommand, "do_all"))
        self.assertTrue(hasattr(console.HBNBCommand, "default"))

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(console.HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(console.HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
    '''
    def test_count(self):
        with patch('sys.stdout', new = StringIO()) as f:
            console.HBNBCommand().precmd("User.count()")
            self.assertEqual('', f.getvalue())
    '''
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help show")
            output = """Displays the object instance\n"""
            self.assertEqual(f.getvalue(), output)
    '''
    def test_destroy(self):
        with patch('sys.stdout', new = StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            id = f.getvalue()
        with patch('sys.stdout', new = StringIO()) as f:
            console.HBNBCommand().precmd("User.count()")
            count = f.getvalue()
            self.assertEqual(count, '')
        with patch('sys.stdout', new = StringIO()) as f:
            console.HBNBCommand().onecmd(f"destroy User {id}")
        with patch('sys.stdout', new = StringIO()) as f:
            console.HBNBCommand().precmd("User.count()")
            count = f.getvalue()
            self.assertEqual('', count)
    '''
    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help all")
            output = """Displays all the object instances\n"""
            self.assertEqual(f.getvalue(), output)

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help quit")
            output = """Quit command to exit the program\n"""
            self.assertEqual(f.getvalue(), output)

    def test_help_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help create")
            output = """Creates a class of any type\n"""
            self.assertEqual(f.getvalue(), output)

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help destroy")
            output = """ destroys an instance of the obj \n"""
            self.assertEqual(f.getvalue(), output)

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help update")
            output = """updates the obj instance\n"""
            self.assertEqual(f.getvalue(), output)

    def test_create(self):
        regex = r"^[\da-f]{8}-(?:[\da-f]{4}-){3}[\da-f]{12}\n$"
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            id = f.getvalue()
            self.assertEqual(f.getvalue(), search(regex, id).string)
            console.HBNBCommand().onecmd(f"destroy User {id}")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create zzz")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            id = f.getvalue()
            self.assertEqual(f.getvalue(), search(regex, id).string)
            console.HBNBCommand().onecmd(f"destroy Place {id}")

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), """Exit the program\n""")

    def test_show(self):
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            id = f.getvalue()[0:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd(f"show User {id}")
            self.assertIn(id, f.getvalue())
            console.HBNBCommand().onecmd(f"destroy User {id}")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd(f"show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd(f"show User zzz")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd(f"all")
            self.assertIn("[User]", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd(f"all asd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            id = f.getvalue()
            console.HBNBCommand().precmd(f"all User")
            self.assertIn(id, f.getvalue())
            console.HBNBCommand().onecmd(f"destroy User {id}")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            id = f.getvalue()
            console.HBNBCommand().onecmd(f"update User {id} name GuyIncognito")
            console.HBNBCommand().onecmd(f"show User {id}")
            self.assertIn("name", f.getvalue())
            console.HBNBCommand().onecmd(f"destroy User {id}")
