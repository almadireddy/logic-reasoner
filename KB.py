class Clause:
    def __init__(self, line):
        self.elements = {}
        self.valid = True

        if line == "":
            self.valid = False
            return

        self.string = line.strip()
        self.count = 0
        split_line = line.split()
        for element in split_line:
            truth = True
            name = element
            if element[0] == "~":
                truth = False
                name = element[1:]

            if name in self.elements:
                if self.elements[name] != truth:
                    self.valid = False
                    return
                else:
                    continue

            self.elements[name] = truth

    def __hash__(self):
        ks = self.elements.keys()
        ks.sort()
        string = ""
        for k in ks:
            string += k
            string += str(self.elements[k])
        return hash(string)

    def __cmp__(self, other):
        return cmp(self.elements, other.elements)

    def __len__(self):
        return len(self.elements)

    def add_variable(self, name, truth_value):
        if name in self.elements:
            if self.elements[name] != truth_value:
                return False

        self.elements[name] = truth_value
        self.count += 1
        return True

    def is_complement(self, other):
        if len(self.elements) == 1 and len(other.elements) == 1:
            if self.elements.keys() == other.elements.keys():
                key = self.elements.keys()[0]
                if self.elements[key] != other.elements[key]:
                    return True
        return False

    def is_valid(self):
        return self.valid


class KB:
    def __init__(self, clauses):
        self.clauses = []
        self.clauseSet = set()
        self.initial_cutoff = 0
        lines = []

        for line in clauses:
            lines.append(line)  # lines[] contains all the lines in the file

        for line in lines:  # self.clauses contains first n-1 clauses
            k = Clause(line)

            if k.is_valid() and k not in self.clauses:
                self.add_clause(Clause(line))

        self.initial_cutoff = len(clauses)

    def ask(self, clause_to_test):
        negated = negate_clause(clause_to_test)
        for i in negated:
            self.add_clause(i)

        self.initial_cutoff = len(self.clauses)

        index = 0
        while index < len(self.clauses):
            current = self.clauses[index]
            current_elements = current.elements

            for i in range(0, index):
                c = self.clauses[i]
                if c is not current:
                    test_elements = c.elements
                    same = [z for z in test_elements.keys() if z in current_elements.keys()]
                    complements = [s for s in same if test_elements[s] != current_elements[s]]

                    if (len(complements)) > 0:
                        current_parent = index
                        test_parent = i

                        if c.is_complement(current):
                            print str(len(self.clauses)+1) + ". Contradiction", \
                                "{" + str(current_parent+1) + ", " + str(test_parent+1) + "}"
                            return True

                        parent1_resultants = {x: current_elements[x] for x in current_elements if x != complements[0]}
                        parent2_resultants = {x: test_elements[x] for x in test_elements if x != complements[0]}

                        for x in list(parent1_resultants.keys()):
                            if x in parent2_resultants:
                                if parent1_resultants[x] != parent2_resultants[x]:
                                    parent1_resultants = {}
                                    parent2_resultants = {}

                        new_elements = merge_two_dicts(parent1_resultants, parent2_resultants)

                        string = ""
                        for x in new_elements:
                            string += x + " " if new_elements[x] is True else "~" + x + " "

                        new_clause = Clause(string)
                        if new_clause.is_valid():
                            self.add_clause(new_clause, current_parent + 1, test_parent + 1)

            index += 1

        return False

    def add_clause(self, clause, parent1=0, parent2=0):
        if clause not in self.clauseSet:
            self.clauses.append(clause)
            self.clauseSet.add(clause)

            if parent1 != 0 and parent2 != 0:
                print str(len(self.clauses)) + ". " + clause.string, "{" + str(parent1) + ", " + str(parent2) + "}"
            else:
                print str(len(self.clauses)) + ". " + clause.string, "{}"


def negate_clause(clause_to_negate):
    clause = clause_to_negate.split()
    elements = []
    new_clauses = []
    for i in clause:
        if i[0] == '~':
            elements.append(i[1:])
        else:
            elements.append("~" + i)

    for e in elements:
        new_clauses.append(Clause(e))

    return new_clauses


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
