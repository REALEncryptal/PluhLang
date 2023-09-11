from frontend.enums import TokenType
from frontend import lexer, syntaxtree

class Parser:
    def __init__(self):
        self.tokens = []
        self.program = None

    # primary
    def createTree(self, SourceString):
        self.tokens = lexer.tokenize(SourceString)
        self.program = syntaxtree.Program()

        while not self.isEOF():
            self.program["body"].append(self.parseStatement())

        self.tokens = {}
        return self.program
    
    def parseStatement(self):
        tokenType = self.get().type
        
        if tokenType == TokenType.Var:
            return self.parseVariableDeclaration()
        else:
            return self.parseExpression()
        
    def parseVariableDeclaration(self):
        isConstant = self.pop().type = TokenType.Const
        identifier = self.expect(TokenType.Identifier).value

        # if we dont define the value
        if self.get().type == TokenType.End:
            self.pop()
            if isConstant:
                print(f"Constant {identifier} must be assigned value")
                exit()
            return syntaxtree.DeclareVariable(identifier, None, False)
        
        # if we do
        
        self.expect(TokenType.Equals)
        declaration = syntaxtree.DeclareVariable(identifier, self.parseExpression(), isConstant)
        self.expect(TokenType.End)

        return declaration


    def parseExpression(self):
        return self.parseAssignmentExpression()
    
    def parseAssignmentExpression(self):
        left = self.parseObjectExpression()

        if self.get().type == TokenType.Equals:
            self.pop()
            value = self.parseAssignmentExpression()
            return syntaxtree.AssignmentExpression(left, value)
        
        return left
    
    def parseObjectExpression(self):
        if self.get().type != TokenType.OpenBrace:
            return self.parseAdditionExpression()
        
        self.pop()
        properties = []

        while not self.isEOF() and self.get().type != TokenType.CloseBrace:
            key = self.expect(TokenType.Identifier).value

            if self.get().type == TokenType.Comma:
                self.pop()
                properties.append(syntaxtree.Property(key))
                continue
            elif self.get().type == TokenType.CloseBrace:
                properties.append(syntaxtree.Property(key))
                continue

            self.expect(TokenType.Colon)
            value = self.parseExpression()

            properties.append(syntaxtree.Property(key, value))
            if self.get().type != TokenType.CloseBrace:
                self.expect(TokenType.Comma) 

        self.expect(TokenType.CloseBrace)
        return syntaxtree.ObjectLiteral(properties)

    # 10 + 10 - 5
    def parseAdditionExpression(self):
        left = self.parseMultiplicationExpression() 

        while self.get().value == "+" or self.get().value == "-":
            operator = self.pop().value
            right = self.parseMultiplicationExpression()
            left = syntaxtree.BinaryExpression(left, right, operator)

        return left

    def parseMultiplicationExpression(self):
        left = self.parsePrimaryExpression() 

        while self.get().value == "*" or self.get().value == "/" or self.get().value == "%":
            operator = self.pop().value
            right = self.parsePrimaryExpression()
            left = syntaxtree.BinaryExpression(left, right, operator)

        return left

    def parsePrimaryExpression(self):
        tokenType = self.get().type

        if tokenType == TokenType.Number:
            return syntaxtree.NumericLiteral(int(self.pop().value))
        elif tokenType == TokenType.Identifier:
            return syntaxtree.Identifier(self.pop().value)
        elif tokenType == TokenType.OpenParenthesis:
            self.pop()
            value = self.parseExpression()
            self.expect(TokenType.ClosedParenthesis)
            return value
        else: 
            print(f"InvalidTokenType: {tokenType}")
            exit()
        
    # utils
    def isEOF(self):
        return self.tokens[0].type == TokenType.EOF
    
    def get(self, index=0):
        return self.tokens[index]
    
    def pop(self):
        return self.tokens.pop(0)
    
    def expect(self, type):
        previousToken = self.pop()

        if (not previousToken or previousToken.type != type):
            print(f"Expecting {type} while parsing")
            exit()

        return previousToken