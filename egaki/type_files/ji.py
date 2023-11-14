import emoji
import re
from egaki.errors.errors import InvalidJiError, InvalidJiStringError

class Ji:
  """
  A class representing an individual ji, regardless of the number
  of Unicode chars it is composed of
  """
  def __init__(self, code: str):
    if not self._is_valid_ji_code(code):
      raise InvalidJiError("Invalid ji")
    else:
      self.code = code

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
  """A class for representing a string of emoji characters
  input: A string of emojis
  """
  def __init__(self, input: str):
    self.jis: list[Ji] = self._create_jis(input)
  
  def __repr__(self):
    ji_codes: list[str] = []
    for ji in self.jis:
      ji_codes.append(ji.code)

    return ji_codes

  def _create_jis(self, input: str) -> list[Ji]:
    # First, deserialize the input into an array of 
    # emoji codes
    deserialized: list[str] = self._deserialize(input)

    # Then, convert this array into an array of jis
    output: list[Ji] = []
    for ji_code in deserialized:
      output.append(Ji(ji_code))
    
    # Finally, return the array
    return output

  def _deserialize(self, input: str):
    # Check to make sure that the entire string is jis
    if not emoji.purely_emoji(input):
      raise InvalidJiStringError("JiString must be initialized with string of valid jis")
    else:
      # Demojize the string (can't iterate over string of jis,
      # as they can be multiple chars in length)
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
