from nose.tools import *
from assignments.assignments1 import *
def test_crossWord():
    assert_equal(CrossWord().countWords(("...X...",".X...X.", "..X.X..",
   "X..X..X", "..X.X..", ".X...X.", "...X..."),3),6)
def test_Abacus():
    assert_equal(Abacus().add(("ooooooooo---", "---ooooooooo",
                                           "ooooooooo---", "---ooooooooo",
 "oo---ooooooo", "---ooooooooo"),100000),('oooooooo---o', '---ooooooooo',
                                          'ooooooooo---', '---ooooooooo',
                                          'oo---ooooooo', '---ooooooooo'))

def test_wordfinder():
    assert_equal(WordFind().findWords(("EASYTOFINDEAGSRVHOTCJYG", "FLVENKDHCESOXXXXFAGJKEO",
                  "YHEDYNAIRQGIZECGXQLKDBI", "DEIJFKABAQSIHSNDLOMYJIN",
                  "CKXINIMMNGRNSNRGIWQLWOG", "VOFQDROQGCWDKOUYRAFUCDO",
                  "PFLXWTYKOITSURQJGEGSPGG"),
("EASYTOFIND", "DIAG", "GOING", "THISISTOOLONGTOFITINTHISPUZZLE"))
,( "0 0", "1 6", "0 22", ""))

def test_eventorder():
    assert_equal(EventOrder().getCount(2,0),13)
