#!/home/kempj/py343ve/bin/python

from sys import argv
from commutator import load_group, print_group, square_to_find_identity_scalar_up_to_order, substitute_group
from sympy import latex
from mathematica_printer import mstr

iofvars = []
split_orders = []
normdict = {}
psi = load_group(argv[1], iofvars = iofvars, split_orders = split_orders, normdict=normdict)
psi = substitute_group(psi, normdict)
prop = square_to_find_identity_scalar_up_to_order(psi, int(argv[2]), split_orders)
print(str(prop)+'\n\n')
print(mstr(prop)+'\n\n')
print(latex(prop).replace('\\\\', '\\'))
