import unittest



class SafePassword:
 
    # default constructor
    def __init__(self, password):
        self.password = password
 
    # a method for printing data members
    def length_password(self):
        return bool(10<=len(self.password)<=25)

    def variety_password(self):
        caraclist = list('[@!#$%^&*()<>?/|}{~:]')
        for char in self.password:
            if char in caraclist:
                return True
        return False

    def carac_password(self):
        for key in self.password:
           if bool(key.isalpha()):
               return True

    def num_password(self):
        for key in self.password:
           if bool(key.isnumeric()):
               return True

    def mini_password(self):
        count = 0
        for ele in self.password:     
            if ele.islower():
                count += 1
        if count >=1:
            return True

    def majusc_password(self):
        count = 0
        for ele in self.password:     
            if ele.isupper():
                count += 1
        if count >=1:
            return True

    def checkeasy_password(self):
       easy = ('Azertyuiop1', 'Qwertyuiop1', 'Password1', 'Password0', 'Azertyuiop0', 'a1234567890A', 'Azertyuiop1234567890')
       for obvious in easy:
            if self.password == obvious:
                return False
       return True
        
class Test_password(unittest.TestCase):

    def test_length_password(self):
        password = SafePassword("AZERTYUIOP1234")
        self.assertEqual(password.length_password(), True)

    def test_variety_password(self):
        password = SafePassword("AZERTYUIOP1234(")
        self.assertEqual(password.variety_password(), True)

    def test_carac_password(self):
        password = SafePassword("AZERTYUIOP1234")
        self.assertEqual(password.carac_password(), True)

    def test_num_password(self):
        password = SafePassword("AZERTYUIOP1234")
        self.assertEqual(password.num_password(), True)

    def test_mini_password(self):
        password = SafePassword("abAZERTYUIOP1234")
        self.assertEqual(password.mini_password(), True)

    def test_majusc_password(self):
        password = SafePassword("AZERTYUIOP1234")
        self.assertEqual(password.majusc_password(), True)

    def test_checkeasy_password(self):
        password = SafePassword("AZERTYUIOP1234")
        self.assertEqual(password.checkeasy_password(), True)



if __name__ == '__main__':
    mdp = input(f"Saisir un mot de passe : ")
    password = SafePassword(mdp)
    

