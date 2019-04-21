
# coding: utf-8

# In[1]:


import sys
import pickle
pickle_in = open("grammar","rb")
grammar = pickle.load(pickle_in)


# # Applying CKY Algo.........

# In[2]:


import sys, time
from nltk import tokenize
from nltk.parse import pchart
from nltk.parse import ViterbiParser

sent = sys.argv[1]
#sent = "My name is Rajat Nagpal"

# Tokenize the sentence.
tokens = sent.split()

# Define a list of parsers.  We'll use all parsers.
parser = ViterbiParser(grammar)


# Replacing unknown words with UNK....

# In[3]:


replace_words_with_UNK = []
for i,item in enumerate(tokens):
    try:
        grammar.check_coverage([item])
    except:
        #print("%s -> 'UNK'" % item)
        replace_words_with_UNK.append(tokens[i])
        tokens[i] = 'UNK'


# In[4]:


trees = parser.parse_all(tokens)
for tree in trees:
    pass


# In[5]:


UNK_str = tree.__str__()

answer= UNK_str
for i in replace_words_with_UNK:
    answer = answer.replace("UNK",i,1)
    
print(answer)

