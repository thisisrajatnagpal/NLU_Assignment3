
# coding: utf-8

# # Importing.....

# In[26]:


import nltk
from nltk import Nonterminal
#nltk.download('treebank')
from nltk.corpus import treebank
from nltk import treetransforms
from nltk import induce_pcfg
from nltk.parse import pchart
from nltk import CFG


# # Chomsky Normal Form....

# In[2]:


productions = []
for item in treebank.fileids()[:]:
    for tree in treebank.parsed_sents(item):
        # perform optional tree transformations, e.g.:
        tree.collapse_unary(collapsePOS = False)# Remove branches A-B-C into A-B+C
        tree.chomsky_normal_form(horzMarkov = 2)# Remove A->(B,C,D) into A->B,C+D->D
        productions += tree.productions()


# Making sublist of parent and child node....

# In[7]:


lhs_prod = [p.lhs() for p in productions]
rhs_prod = [p.rhs() for p in productions]
set_prod = set(productions)


# Making Token Rules.......

# In[14]:


prod = list(set_prod)
token_rule = []
for item in prod:
    if item.is_lexical():
        token_rule.append(item)


# # Creating List of Rules....

# In[19]:


list_of_rules = []
set_tok_rule = set(p.lhs() for p in token_rule)
tok_rule = list(set_tok_rule)
for word in tok_rule:
    if str(word).isalpha():
        list_of_rules.append(word)
        continue
print(list_of_rules)


# # Creating UNK tokens for all the rules....

# In[25]:


temp = []
for rule in list_of_rules:
    lhs = 'UNK'
    rhs = [u'UNK']
    UNK_production = nltk.grammar.Production(lhs, rhs)   
    lhs2 = nltk.grammar.Nonterminal(str(rule))
    temp.append(nltk.grammar.Production(lhs2, [lhs]))

    
#Adding UNK to token rules
token_rule.extend(temp)
prod.extend(temp)


# # Inducing Probabilities and making grammer out of it.......

# In[27]:


S = Nonterminal('S')
grammar = induce_pcfg(S,prod)


# In[34]:


import pickle
pickle.dump(grammar, open("grammar", 'wb'))

