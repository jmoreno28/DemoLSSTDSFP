from DSFP.data import get_photometry

data = get_photometry(10)


def test_get_photometry():
    """UNIT TEST EXAMPLE"""
    
    
    assert len(data) == 10
