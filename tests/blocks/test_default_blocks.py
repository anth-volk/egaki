import pytest

from egaki.blocks.default_blocks import number_role_formula
from egaki.type_files.ji import JiString
from egaki.interpretation.lexer import Lexer

class TestNumbersBlock:

  # Construct lexable jis using Lexer's private method
  lexer = Lexer()
  lexable_jis = lexer._construct_lexable_jis()

  # Test that number_formula works properly for 1 num emoji

  # Test that number_formula works for 10 numbers

  # Test that number_formula works for nums, followed by non-nums
              
  # Test that number_formula fails for non-numbers
              
  # Test that number_formula properly forms valid decimal numbers
              
  # Test that number_formula fails for invalid decimal numbers