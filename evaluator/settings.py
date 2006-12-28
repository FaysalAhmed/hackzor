# '%' is not allowed in the compilation string.
# Format Strings:
#     %i    ---  Input File Name
#     %o    ---  Ouput File Name
#     %u    ---  User Name (who submitted the code)
#     %q    ---  Question Name


C_COMPILE_STR = 'gcc -lm -w \'%i\' -o \'%o\''
CPP_COMPILE_STR = 'g++ -lm -w \'%i\' -o \'%o\''
JAVA_COMPILE_STR = 'javac \'%i\''

WORK_DIR = 'work_files'
TIME_INTERVAL = 5 # Time between poll to web server for attempts (in seconds)

CONTEST_URL = 'http://opc.kurukshetra.org.in:8000' # should typically be same as in
# ../settings.py
                                      
EVALUATOR_PATH = 'evaluators'
INPUT_PATH = 'input'

SERVER_KEYID = 'BCBDB351D1640F3F' # Enter the server's Public Key ID
