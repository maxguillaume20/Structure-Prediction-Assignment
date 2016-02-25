"""T0651 target sequence domain definition"""

seq = "MGHHHHHHSHMVKDIIIASFYKFIPLNDFRSLREPILTKMHEIGIKGTIILAHEGVNGGFAGNR\
EQMNVFYDYLRSDSRFADLHFKETYDNKNPFDKAKVKLRKEIVTMGVQKVDPSYNAGTYLSPEEWHQFIQD\
PNVILLDTRNDYEYELGTFKNAINPDIENFREFPDYVQRNLIDKKDKKIAMFCTGGIRCEKTTAYMKELGF\
EHVYQLHDGILNYLESIPESESLWEGKCFVFDDRVAVDQKLDRVYPQLPQDYKYEREQK"

o = -10 # offset because of expression tag
d1_i, d1_j = (1, 95) # first domain positions
d2_i, d2_j = (111, 221) # second domain positions
d3_i, d3_j = (222, 254) # third domain positions

d1 = seq[(d1_i-o):(d1_j-o+1)]
d2 = seq[(d2_i-o):(d2_j-o+1)]
d3 = seq[(d3_i-o):(d3_j-o+1)]

print ">T0651|D1|%s-%s" %(d1_i, d1_j)
print d1
print "\n>T0651|D2|%s-%s" %(d2_i, d2_j)
print d2
print "\n>T0651|D3|%s-%s" %(d3_i, d3_j)
print d3
