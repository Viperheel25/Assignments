from nose.tools import *
from assignments.assignments2 import *


def test_a_tale_of_three_cities():
    ax=(4,5,11,21,8,10,3,9,5,6)
    ay=(12,8,9,12,2,3,5,7,10,13)
    bx=(34,35,36,41,32,39,41,37,39,50)
    by=(51,33,41,45,48,22,33,51,41,40)
    cx=(86,75,78,81,89,77,83,88,99,77)
    cy=(10,20,30,40,50,60,70,80,90,100)
    assert_equal(ATaleOfThreeCities().connect(ax,ay,bx,by,cx,cy),50.3233977766)
def test_additiongame():
    A=3
    B=4
    C=5
    N=3
    assert_equal(AdditionGame().getMaximumPoints(A, B, C, N),13)
def test_accountbalance():
    x=100
    y=("D 50", "D 20", "D 40")
    assert_equal(AccountBalance().processTransactions(x,y),-10)
def test_into_the_matrix():
    turns=2
    N=10
    assert_equal(IntoTheMatrix().takePills(turns, N),3)
