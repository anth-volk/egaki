import pytest
from typing import Optional, Union

from egaki.type_files.ji import Ji, JiString
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

  def _check_equality(self, test_str: JiString, test_arr: list[Ji]) -> Union[tuple[bool, str], bool]:
    """
    Checks if a JiString is equal to a list of the same items, 
    then returns True if they are or false if not, as well as 
    an optional error string
    """
    
    # Check that input JiString is of correct type
    if not isinstance(test_str, JiString):
      return False, "JiString arg is of incorrect type"

    # Check that both args are of same length
    if len(test_str.jis) != len(test_arr):
      return False, "Args are of different lengths"
    
    # Check that each item in the JiStrings is the same
    for i in range(len(test_str.jis)):
      if test_str.jis[i].code != test_arr[i].code:
        return False, f"""Ji codes at index {i}:
        {test_str.jis[i].code}, {test_arr[i].code}"""
      
    # If all of the above pass, return true
    return True
    
  # Test that, given two emoji, JiString creates list
  # of two Ji
  def test_emoji_creation(self):
    input_string = JiString("😀😀")
    test_arr = [
      Ji(":grinning_face:"),
      Ji(":grinning_face:")
    ]
    assert self._check_equality(input_string, test_arr) == True

  # Test that, given two shortcodes, JiString works
  def test_shortcode_creation(self):
    input_string = JiString(":grinning_face::grinning_face:")
    test_arr = [
      Ji("😀"),
      Ji("😀")
    ]
    assert self._check_equality(input_string, test_arr) == True

  # Test that, given a mix, JiString works
  def test_mixed_creation(self):
    input_string = JiString(":grinning_face:😀")
    test_arr = [
      Ji(":grinning_face:"),
      Ji(":grinning_face:")
    ]
    assert self._check_equality(input_string, test_arr) == True

  # Test that, given two Ji, JiString works
  def test_ji_creation(self):
    jis = [
      Ji(":grinning_face:"),
      Ji(":grinning_face:")
    ]
    input_string = JiString(jis)
    assert self._check_equality(input_string, jis) == True

  # Test that append() works
  def test_append(self):
    input_string = JiString()
    input_string.append(Ji(":grinning_face:"))
    test_arr = [
      Ji(":grinning_face:")
    ]
    assert self._check_equality(input_string, test_arr) == True