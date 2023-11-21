import pytest
from typing import Optional, Union

from egaki.type_files.ji import Ji, JiString, check_jistring_equality
from egaki.errors.errors import InvalidJiError

class TestJi:
  
  # Test that Ji can properly handle a single emoji (non-compound)
  def test_proper_creation(self):
    input_ji = Ji("😀")
    assert input_ji.code == ":grinning_face:"

  # Test that Ji can handle single compound emoji
  def test_compound_creation(self):
    input_ji = Ji("👨‍🔬")
    assert input_ji.code == ":man_scientist:"

  # Test that Ji can handle valid shortcode
  def test_shortcode_creation(self):
    input_ji = Ji(":grinning_face:")
    assert input_ji.code == ":grinning_face:"

  # Test that Ji can handle invalid shortcode
  def test_invalid_shortcode(self):
    with pytest.raises(InvalidJiError):
      input_ji = Ji(":montaña:")

  # Test that Ji errors when given garbage values
  def test_garbage(self):
    with pytest.raises(InvalidJiError):
      input_ji = Ji("garbage_string")

  # Test that Ji errors when given more than one emoji
  def test_multiple_creation(self):
    with pytest.raises(InvalidJiError):
      input_ji = Ji("😀😀")

class TestJiString:

  # Test that, given two emoji, JiString creates list
  # of two Ji
  def test_emoji_creation(self):
    input_string = JiString("😀😀")
    test_string = JiString([
      Ji(":grinning_face:"),
      Ji(":grinning_face:")
    ])
    assert check_jistring_equality(input_string, test_string) == True

  # Test that, given two shortcodes, JiString works
  def test_shortcode_creation(self):
    input_string = JiString(":grinning_face::grinning_face:")
    test_string = JiString([
      Ji("😀"),
      Ji("😀")
    ])
    assert check_jistring_equality(input_string, test_string) == True

  # Test that, given a mix, JiString works
  def test_mixed_creation(self):
    input_string = JiString(":grinning_face:😀")
    test_string = JiString([
      Ji(":grinning_face:"),
      Ji(":grinning_face:")
    ])
    assert check_jistring_equality(input_string, test_string) == True

  # Test that append() works
  def test_append(self):
    input_string = JiString()
    input_string.append(Ji(":grinning_face:"))
    test_string = JiString([
      Ji(":grinning_face:")
    ])
    assert check_jistring_equality(input_string, test_string) == True