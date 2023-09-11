from runtime import values

def initGlobals(environment):
    environment.declareVariable("true", values.BoolValue(True), True)
    environment.declareVariable("false", values.BoolValue(False), True)
    environment.declareVariable("null", values.NullValue(), True)

class Environment:
    def __init__(self, parent = False):
        self.parent = parent
        self.variables = {}
        self.constants = []

        if not parent: initGlobals(self)

    def declareVariable(self, name, value, constant=False):
        if name in self.variables:
            print(f"Variable: {name} is already defined")
        else:
            self.variables[name] = value
            if constant: self.constants.append(name)
            
            return value
        
    def assignVariable(self, name, value):
        environment = self.resolveVariable(name)

        if name in self.constants:
            print(f"Cannot assign value to {name} as it is constant")
            exit()

        environment.variables[name] = value

        return value
    
    def getVariable(self, name):
        environment = self.resolveVariable(name)
        return environment.variables[name]
    
    def resolveVariable(self, name):
        if name in self.variables: return self
        if self.parent: return self.parent.resolveVariable(name)
        print(f"{name} does not exist")
        exit()