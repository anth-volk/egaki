from src.interpretation import Lexer

while True:

  lexer = Lexer()
  input_line = input("💰 ")
  if (input_line == "🛑"):
    break
  else:
    print(lexer.lex(input_line))