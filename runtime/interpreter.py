from runtime import values
from frontend.enums import NodeType, ValueType, TokenType

## evaluaters
def EvaluateProgram(Program, Environment):
    lastEvaluated = values.NullValue()

    for statement in Program["body"]:
        lastEvaluated = Evaluate(statement, Environment) 

    return lastEvaluated

def EvaluateBinaryExpression(BinaryExpression, Environment):
    leftSide = Evaluate(BinaryExpression["left"], Environment)
    rightSide = Evaluate(BinaryExpression["right"], Environment)

    if leftSide["type"] == ValueType.Number and rightSide["type"] == ValueType.Number:
        return EvaluateNumericBinaryExpression(leftSide["value"], rightSide["value"], BinaryExpression["operator"], Environment)
    
    return values.NullValue()

def EvaluateNumericBinaryExpression(LeftSide, RightSide, Operator, Environment):
    result = 0

    if Operator == "+": result = LeftSide + RightSide
    elif Operator == "-": result = LeftSide - RightSide
    elif Operator == "*": result = LeftSide * RightSide 
    elif Operator == "/": result = LeftSide / RightSide #TODO: division by 0 check
    else: result = LeftSide % RightSide

    return values.NumberValue(result)

def EvaluateIdentifier(Identifier, Environment):
    return Environment.getVariable(Identifier["symbol"])

def EvaluateVariableDeclaration(Declaration, Environment):
    value = Declaration["value"]
    if value is None: 
        value = values.NullValue()
    elif value["type"] == NodeType.BinaryExpression:
        value = Evaluate(value, Environment)
    else:
        try:
            value = values.NumberValue(value["value"])
        except: pass
    
    
    return Environment.declareVariable(Declaration["identifier"], value)

def EvaluateAssignment(Node, Environment):
    if Node["variable"]["type"] != NodeType.Identifier:
        print("invalid left side")
        exit()

    varName = Node["variable"]["symbol"]
    return Environment.assignVariable(varName, Evaluate(Node["value"], Environment))

"""
def evaluateObjectExpression(object, Environmment):
    object = values.ObjectValue()

    for property in object["properties"]

    return object"""

## main
def Evaluate(SyntaxTreeNode, Environment):
    nodeType = SyntaxTreeNode["type"]

    if nodeType == NodeType.NumericLiteral:
        return values.NumberValue(SyntaxTreeNode["value"])
    
    elif nodeType == NodeType.BinaryExpression:
        return EvaluateBinaryExpression(SyntaxTreeNode, Environment)
    
    elif nodeType == NodeType.Program:
        return EvaluateProgram(SyntaxTreeNode, Environment)
    
    elif nodeType == NodeType.Identifier:
        return EvaluateIdentifier(SyntaxTreeNode, Environment)
    
    elif nodeType == NodeType.DeclareVariable:
        return EvaluateVariableDeclaration(SyntaxTreeNode, Environment)
    
    elif nodeType == NodeType.AssignmentExpression:
        return EvaluateAssignment(SyntaxTreeNode, Environment)


    else:
        print("Bad ast node: ", SyntaxTreeNode)
        exit()