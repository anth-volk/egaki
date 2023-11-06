from src.type_files.ji import JiString

class Token:
  def __init__(self, text, role):
    self.text = text
    self.role = role

  def __repr__(self):
    if (self.role):
      return f"{self.text}: {self.role}"
    else:
      return f"{self.text}: role null"

