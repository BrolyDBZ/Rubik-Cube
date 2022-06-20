
"""
We'll call the six sides, as usual:
   Front Back   Up Down   Left Right
or F, B, U, D, L, R.

Permutations:

We'll number the cubie positions starting
at 0, front to back, up to down, left to right.
We give an alphabetic name to the cubies as well,
by listing the faces it contains, starting with
F or B, in clockwise order (looking in from outside).
   0th cubie = FLU
   1st cubie = FUR
   2nd cubie = FDL
   3rd cubie = FRD
   4th cubie = BUL
   5th cubie = BRU
   6th cubie = BLD
   7th cubie = BDR
Each cubie has three faces, so we have 24 face
positions.  We'll label them as 0 to 23, but also
with a 3-letter name that specifies the name
of the cubie it is on, cyclically rotated to
put the name of the face first (so cubie FLU
has faces flu, luf, and ufl, on sides F, L,
and U, respectively). We'll use lower case
here for clarity.  Here are the face names,
written as variables for later convenience.
We also save each number in a second variable,
where the positions are replaced by the colors that
would be there if the cube were solved and had its
orange-yellow-blue cubie in position 7, with yellow
facing down.
"""

rgw = flu = 0 
gwr = luf = 1  
wrg = ufl = 2  

rwb = fur = 3  
wbr = urf = 4  
brw = rfu = 5  

ryg = fdl = 6 
ygr = dlf = 7 
gry = lfd = 8  

rby = frd = 9 
byr = rdf = 10  
yrb = dfr = 11  

owg = bul = 12 
wgo = ulb = 13  
gow = lbu = 14  

obw = bru = 15  
bwo = rub = 16  
wob = ubr = 17 

ogy = bld = 18  
gyo = ldb = 19  
yog = dbl = 20 

oyb = bdr = 21  
ybo = drb = 22
boy = rbd = 23  





def perm_apply(perm, position):
    """
    Apply permutation perm to a list position (e.g. of faces).
    Face in position p[i] moves to position i.
    """
    return tuple([position[i] for i in perm])


def perm_inverse(p):
    """
    Return the inverse of permutation p.
    """
    n = len(p)
    q = [0] * n
    for i in xrange(n):
        q[p[i]] = i
    return tuple(q)


def perm_to_string(p):
    """
    Convert p to string, slightly more compact
    than list printing.
    """
    s = "("
    for x in p: s = s + "%2d " % x
    s += ")"
    return s



I = (
flu, luf, ufl, fur, urf, rfu, fdl, dlf, lfd, frd, rdf, dfr, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)

"""
When any of the following Rubik's cube permutations are applied, the
three faces on a cubie naturally stay together:
{0,1,2}, {3,4,5}, ..., {21,22,23}.
"""

# Front face rotated clockwise.
F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu,
     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
# Front face rotated counter-clockwise.
Fi = perm_inverse(F)

# Left face rotated clockwise.
L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr,
     dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)
# Left face rotated counter-clockwise.
Li = perm_inverse(L)

# Upper face rotated clockwise.
U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr,
     luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)
# Upper face rotated counter-clockwise.
Ui = perm_inverse(U)

# All 6 possible moves (assuming that the lower-bottom-right cubie
# stays fixed).
quarter_twists = (F, Fi, L, Li, U, Ui)

quarter_twists_names = {}
quarter_twists_names[F] = 'F'
quarter_twists_names[Fi] = 'Fi'
quarter_twists_names[L] = 'L'
quarter_twists_names[Li] = 'Li'
quarter_twists_names[U] = 'U'
quarter_twists_names[Ui] = 'Ui'


def input_configuration():
    """
    Prompts a user to input the current configuration of the cube, and
    translates that into a permutation.
    """
    position = [-1] * 24


    position[0] = eval(cubie)
    position[1] = eval(cubie[1:] + cubie[0])
    position[2] = eval(cubie[2] + cubie[:2])
   
    position[3] = eval(cubie)
    position[4] = eval(cubie[1:] + cubie[0])
    position[5] = eval(cubie[2] + cubie[:2])
    
    position[6] = eval(cubie)
    position[7] = eval(cubie[1:] + cubie[0])
    position[8] = eval(cubie[2] + cubie[:2])
    
    position[9] = eval(cubie)
    position[10] = eval(cubie[1:] + cubie[0])
    position[11] = eval(cubie[2] + cubie[:2])
    
    position[12] = eval(cubie)
    position[13] = eval(cubie[1:] + cubie[0])
    position[14] = eval(cubie[2] + cubie[:2])
    
    position[15] = eval(cubie)
    position[16] = eval(cubie[1:] + cubie[0])
    position[17] = eval(cubie[2] + cubie[:2])
   
    position[18] = eval(cubie)
    position[19] = eval(cubie[1:] + cubie[0])
    position[20] = eval(cubie[2] + cubie[:2])
    cubie = 'oyb'
    position[21] = eval(cubie)
    position[22] = eval(cubie[1:] + cubie[0])
    position[23] = eval(cubie[2] + cubie[:2])

    return tuple(position)
