class InvalidJiError(Exception):
  """
  Error message for invalid emojis  or
  improperly serialized or deserialized emojis
  """
  def __init__(self, message):
    super().__init__(message)