import unittest
import converte_romano_Luis

class Testconversor_romanos(unittest.TestCase):
    def test_valida_numero(self):
        self.assertTrue(converte_romano_Luis.valida_numero(33),)
    def test_valida_numero_1(self):
        self.assertFalse(converte_romano_Luis.valida_numero(4000),)
    def test_valida_numero_2(self):
        self.assertFalse(converte_romano_Luis.valida_numero(-1),)

    def test_numero_para_romano(self):
        self.assertEqual(converte_romano_Luis.numero_para_romano(55),'LV')
    def test_numero_para_romano_1(self):        
        self.assertEqual(converte_romano_Luis.numero_para_romano(500),'D')
    def test_numero_para_romano_2(self):
        self.assertEqual(converte_romano_Luis.numero_para_romano(900),'CM')
    def test_numero_para_romano_3(self):
        self.assertEqual(converte_romano_Luis.numero_para_romano(3500),'MMMD')




if __name__ == '__main__':
    unittest.main()
