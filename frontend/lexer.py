from frontend.enums import TokenType

tokenMap = {
    "(":TokenType.OpenParenthesis,
    ")":TokenType.ClosedParenthesis,
    "=":TokenType.Equals,
    "+":TokenType.Operator,
    "-":TokenType.Operator,
    "*":TokenType.Operator,
    "/":TokenType.Operator,
    "%":TokenType.Operator,
    ";":TokenType.End,
    "{":TokenType.OpenBrace,
    "}":TokenType.CloseBrace,
    ":":TokenType.Colon,
    ",":TokenType.Comma
}

reserved_keywords = {
    "make":TokenType.Var,
}
irrelevant_keywords = ["\n", " ", "\r", "\t", "\v"]

class Token():
    def __init__(self, value, type) -> None:
        self.value = value 
        self.type = type

    def __str__(self) -> str:
        return f"token({self.value}, {self.type})"

#           Main functions
def tokenize(SourceString):
    SourceString = list(SourceString)
    tokens = []

    while len(SourceString) > 0:
        Char = SourceString[0]
        if Char in tokenMap:
            # single char tokens
            tokens.append(Token(SourceString.pop(0), tokenMap[Char]))
        else:
            # multi char tokens
            if Char.isdigit():
                number = ""

                while len(SourceString) > 0 and SourceString[0].isdigit():
                    number += SourceString.pop(0)

                tokens.append(Token(number,TokenType.Number))
            elif Char.isalpha():
                string = ""

                while len(SourceString) > 0 and SourceString[0].isalpha():
                    string += SourceString.pop(0)
                
                try: 
                    tokens.append(Token(string,reserved_keywords[string]))
                except KeyError:
                    tokens.append(Token(string,TokenType.Identifier))
                    

            elif Char in irrelevant_keywords:
                SourceString.pop(0)
            else:
                print(f"Invalid char: {Char}]")
                exit()

    tokens.append(Token(0, TokenType.EOF))
    return tokens


#    utils