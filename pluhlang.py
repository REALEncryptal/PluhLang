from frontend import lexer, zparser
from runtime import interpreter, values, environment
import pprint, sys

if len(sys.argv) != 2:
    print("Usage: python pluhlang.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

source = open(file_path, "r").read()

# init
parser = zparser.Parser()
cEnvironment = environment.Environment()

# execute
parsedsource = parser.createTree(source)
results = interpreter.Evaluate(parsedsource, cEnvironment)
print("------ Last line evaluated results ------")
pprint.pp(results)
print("------ Parsed Source ------")
pprint.pp(parser)