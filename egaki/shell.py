from egaki.interpretation.lexer import Lexer

def shell():
  while True:

    lexer = Lexer()
    input_line = input("💰 ")
    if (input_line == "🛑"):
      break
    else:
      print(lexer.lex(input_line))

if __name__ == '__main__':
  shell()