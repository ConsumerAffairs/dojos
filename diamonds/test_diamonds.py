from diamonds import print_diamond


def test_A():
    assert print_diamond('A') == 'A'
    
def test_B():
    expected = ' A\nB B\n A'
    assert print_diamond('B') == expected
    

    
if __name__ == '__main__':
    # test_A()
    test_B()
