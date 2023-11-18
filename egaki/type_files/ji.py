import emoji
import re
from typing import Optional, Union

from egaki.errors.errors import InvalidJiError

class Ji:
  """
  A class representing an individual ji, regardless of the number
  of Unicode chars it is composed of

  Args:
    text: Text representing one emoji, whether it's the 
    emoji itself or its shortcode
  """
  def __init__(self, text: str):
    # If emoji is an actual emoji, convert to shortcode
    if (emoji.is_emoji(text)):
      text = emoji.demojize(text)
    # Otherwise, if passed text, ensure it's a valid shortcode
    elif not self._is_valid_ji_code(text):
      raise InvalidJiError("Invalid ji; please pass one emoji or valid shortcode to Ji constructor")

    # If we're this far, store the code
    self.code = text

  def __repr__(self):
    return f"'{self.code}'"

  def _is_valid_ji_code(self, code: str):
    """
    Determine if a code is a valid ji by emojizing, then checking
    if the result is a valid emoji (there is currently no way to do so
    without emojizing in the Python emoji package)
    """
    if emoji.is_emoji(emoji.emojize(code)):
      return True
    return False

class JiString:
  """
  A thin wrapper class for a list of Ji objects,
  along with a series of helper methods

  Args:
    input: A string of emojis (either as emojis, shortcodes,
    or Ji instances) or None

  Methods:
    append: Appends a Ji to the JiString
  """
  def __init__(self, input: Optional[str] = None):
    self.jis: list[Ji] = self._create_jis(input)
  
  def __repr__(self):
    ji_codes: list[str] = []
    for ji in self.jis:
      ji_codes.append(ji.code)

    return ji_codes
  
  def append(self, item: Union[str, Ji]):
    if type(item) == str:
      item = Ji(item)

    assert type(item) == Ji
    assert type(self.jis) == list
    self.jis.append(item)

  def _create_jis(self, input: Optional[str]) -> list[Ji]:
    # If input is None, return an empty list
    if (input == None):
      return list()
    
    # First, deserialize the input into an array of 
    # emoji codes
    # The below line included for mypy type checking
    assert input is not None
    deserialized: list[str] = self._deserialize(input)

    # Then, convert this array into an array of jis
    output: list[Ji] = []
    for ji_code in deserialized:
      output.append(Ji(ji_code))
    
    # Finally, return the array
    return output

  def _deserialize(self, input: str) -> list[str]:
    # Note: This function will not check to ensure that non-emoji
    # textual input are valid shortcodes; Ji class handles error checking

    # Demojize the string
    deserialized_str: str = emoji.demojize(input)

    # Break the deseralized string into an array of codes
    deserialized: list[str] = self._create_deserialized_arr(deserialized_str)

    # Return the resulting array
    return deserialized
  
  def _create_deserialized_arr(self, deserialized_str: str) -> list[str]:
    # Note: The emoji package (as of 2.8.0) deserializes each ji into
    # :description:, followed by another without space between them;
    # for example:
    # :keycap_1::stop_sign::man_raising_hand::dollar_banknote:

    return re.split("(?<=:)(?=:)", deserialized_str)
