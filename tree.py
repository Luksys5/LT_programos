from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
import dendropy
import networkx, pylab
#aln = AlignIO.read('Tests/TreeConstruction/msa.phy', 'phylip')
#print aln
#tree = Phylo.read("simple.dnd", 'newick')
tree = Phylo.read("apaf.xml", "phyloxml")
#tree.ladderize()
print tree
#tree_plot = Phylo.draw(tree)
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(tree)
print dm
#Phylo.draw_ascii(tree)
#tree_plot = Phylo.draw(tree)
