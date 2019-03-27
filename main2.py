import sys
from KB import KB

args = sys.argv[:]

if not len(args) == 2:
    print "Expected single file to form initial KB. Exiting."
    exit(0)

lines = []

open_file = open(args[1])
for line in open_file:
    lines.append(line)
open_file.close()

kb = KB(lines[0:len(lines)-1])
clause_to_test = lines[-1]

if kb.ask(clause_to_test):
    print "Valid"

else:
    print "Invalid"
