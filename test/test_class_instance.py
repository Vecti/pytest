class TestClass:

    """
    each class / fixtures has their unique instantion of the class
    so be careful with method relying on other
    """

    # ### uncomment if you want warning    
    # def __init__(self):
    #     self.value = 5

    ### uncomment if you want error (if init commented)
    value = 5
    def test_one(self):
        self.value += 1
        assert self.value == 6
    
    def test_two(self):
        assert self.value ==6