"""REPL, read, evaluate, print, loop(what IDLE does)
# in cmd: python -i <file_addr> will allow you to execute the file and use the functions
# in cmd: python -m idlelib.idle will allow you to open and run that module
"""
import random

class Markov:
    def __init__(self, txt):
        
        self.table = get_table(txt)

    def predict(self, txt):
        options = self.table.get(txt, {})
        if not options:
            raise KeyError(f'{txt} not found')
                        #('{} not found'.format(txt))
        possibles = []
        for key, count in options.items():
            for i in range(count):
                possibles.append(key)
        return random.choice(possibles) #if key is in table 60% it will have 60% chance to be picked
    
    
#need to create a transition table for possible next jumps. Mapping characters with following characters and associated counts
def get_table(txt):
    """This is the get_table docstring

    >>>get_table('ab')
    {'a': {'b':1}}
    """
    results = {} #emplty dict literal
    for i in range(len(txt)):
        char = txt[i]
        try:
            dst = txt[i+1]
        except IndexError as ie:
            break
        char_dict = results.get(char, {}) #utilize get funt to check if char is in results dict
        char_dict.setdefault(dst, 0) #if dst not in char_dict then set default of dst as 0
        char_dict[dst] += 1
        results[char] = char_dict
    return results

            
