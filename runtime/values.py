from frontend.enums import ValueType

def NullValue():
    return {
        "type":ValueType.NULL,
        "value":"null"
    }

def NumberValue(Value):
    return {
        "type":ValueType.Number,
        "value":Value
    }

def BoolValue(Value):
    return {
        "type":ValueType.Boolean,
        "value":Value
    }


def ObjectValue(properties = {}):
    return {
        "type":ValueType.Object,
        "properties":properties
    }