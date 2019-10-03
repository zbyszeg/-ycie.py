import unittest
import io
import sys

from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.my_board = Board()

    def test_display(self):
        """To jest właściwa metoda testująca display"""
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        self.my_board.display()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        print('0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000'
              '0000000000000000', captured_output.getvalue())  # Now works as before.


unittest.main()
