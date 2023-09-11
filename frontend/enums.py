from enum import Enum

class TokenType(Enum):
    Number=0
    Identifier=1
    Equals=2
    OpenParenthesis=3
    ClosedParenthesis=4
    Operator=5
    Var=6 # make
    EOF=7
    String=8
    End = 9 # ;
    Const = 10 
    Comma = 11 # ,
    Colon = 12 
    OpenBrace = 13 # [
    CloseBrace = 14 # ]

class NodeType(Enum):
    Program = 1
    NumericLiteral = 2
    Identifier = 4
    BinaryExpression = 5
    DeclareVariable = 6 
    AssignmentExpression = 7
    Property = 8
    ObjectLiteral = 9

# for interpreter
class ValueType(Enum):
    Number = 2
    Boolean = 3
    NULL = 4
    Object = 5