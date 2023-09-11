from frontend.enums import NodeType

def Program(Body=[]):
    return {
        "type":NodeType.Program,
        "body":[]
    }

def DeclareVariable(Identifier, Value,Constant=False):
    return {
        "type":NodeType.DeclareVariable,
        "identifier":Identifier,
        "value":Value,
        "constant":Constant
    }

def BinaryExpression(Left, Right, Operator):
    return {
        "type":NodeType.BinaryExpression,
        "left":Left,
        "right":Right,
        "operator":Operator,
    }

def Identifier(Symbol):
    return {
        "type":NodeType.Identifier, 
        "symbol":Symbol
    }

def NumericLiteral(Value):
    return {
        "type":NodeType.NumericLiteral,
        "value":Value
    }

def AssignmentExpression(Variable, Value):
    return {
        "type":NodeType.AssignmentExpression,
        "variable":Variable,
        "value":Value
    }

def Property(Key, Value=None):
    return {
        "type":NodeType.Property,
        "key":Key,
        "value":Value
    }

def ObjectLiteral(Properties=[]):
    return {
        "type":NodeType.ObjectLiteral,
        "properties":Properties
    }

