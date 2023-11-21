import pytest

from egaki.blocks.default_blocks import number_role_formula
from egaki.type_files.ji import JiString, check_jistring_equality
from egaki.interpretation.lexer import Lexer

class TestNumbersBlock:

  # Construct lexable jis using Lexer's private method
  lexer = Lexer()
  lexable_jis = lexer._construct_lexable_jis()

  # Test that number_formula works properly for 1 num emoji
  def test_single_emoji(self):
    test_input = JiString(":keycap_0:")
    expected_output = JiString(":keycap_0:")
    to_parse_remaining, lexed_jis = number_role_formula(test_input, self.lexable_jis)
    assert check_jistring_equality(to_parse_remaining, JiString()) == True
    assert check_jistring_equality(expected_output, lexed_jis) == True

  # Test that number_formula works for 10 numbers
  def test_multiple_emoji(self):
    test_input = JiString(":keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0:")
    expected_output = JiString(":keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0::keycap_0:")
    to_parse_remaining, lexed_jis = number_role_formula(test_input, self.lexable_jis)
    assert check_jistring_equality(to_parse_remaining, JiString()) == True
    assert check_jistring_equality(expected_output, lexed_jis) == True

  # Test that number_formula works for nums, followed by non-nums
  def test_mixed_input(self):
    test_input = JiString(":keycap_0::keycap_1::grinning_face:")
    expected_token = JiString(":keycap_0::keycap_1:")
    expected_remaining = JiString(":grinning_face:")
    to_parse_remaining, lexed_jis = number_role_formula(test_input, self.lexable_jis)
    assert check_jistring_equality(to_parse_remaining, expected_remaining) == True
    assert check_jistring_equality(lexed_jis, expected_token) == True
              
  # Test that number_formula fails for non-numbers
  def test_no_numbers(self):
    test_input = JiString(":grinning_face:")
    expected_remaining = JiString(":grinning_face:")
    to_parse_remaining, lexed_jis = number_role_formula(test_input, self.lexable_jis)
    assert check_jistring_equality(to_parse_remaining, expected_remaining) == True
    assert check_jistring_equality(lexed_jis, JiString()) == True
              
  # Test that number_formula properly forms valid decimal numbers
  def test_proper_decimal(self):
    test_input = JiString(":keycap_1::keycap_2::record_button::keycap_2:")
    expected_token = JiString(":keycap_1::keycap_2::record_button::keycap_2:")
    to_parse_remaining, lexed_jis = number_role_formula(test_input, self.lexable_jis)
    assert check_jistring_equality(to_parse_remaining, JiString()) == True
    assert check_jistring_equality(lexed_jis, expected_token) == True
              
  # Test that number_formula fails for invalid decimal numbers (too many decimals)

  # Test that number_formula fails for numbers ending in decimal