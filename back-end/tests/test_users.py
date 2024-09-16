import unittest
from models.user import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        # Configuration initiale pour chaque test
        self.user = User(name='Test User', email='testuser@example.com')
    
    def test_password_hashing(self):
        """Test du hashage du mot de passe"""
        self.user.set_password('mypassword')
        
        # Vérifier que le mot de passe est bien haché et non stocké en clair
        self.assertNotEqual(self.user.password_hash, 'mypassword')
    
    def test_password_verification(self):
        """Test de la vérification du mot de passe"""
        self.user.set_password('mypassword')
        
        # Vérifier que check_password renvoie True pour le bon mot de passe
        self.assertTrue(self.user.check_password('mypassword'))
        
        # Vérifier que check_password renvoie False pour un mauvais mot de passe
        self.assertFalse(self.user.check_password('wrongpassword'))

    def test_no_password_in_plain_text(self):
        """Test que le mot de passe en clair n'est pas stocké"""
        self.user.set_password('mypassword')
        
        # Vérifier que le mot de passe en clair n'existe pas dans le modèle
        with self.assertRaises(AttributeError):
            _ = self.user.password  # Cela devrait lever une exception AttributeError

if __name__ == '__main__':
    unittest.main()
