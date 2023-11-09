class InvalidJiError(Exception):
  """
  Error message for invalid emojis  or
  improperly serialized or deserialized emojis
  """
  def __init__(self, message):
    super().__init__(message)

class InvalidJiStringError(Exception):
  """
  Error message indicating that a ji string contains
  non-ji characters
  """
  def __init__(self, message):
    super().__init__(message)