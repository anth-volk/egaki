import pytest
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