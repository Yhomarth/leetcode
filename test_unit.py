# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:39:12 2019

@author: y.reyes
"""
import unittest

import utils.num_romano as num_romano
import utils.remove_element as remove_element


class PruebasFunciones(unittest.TestCase):
    
    def test_romanToInt(self):
        """ Haciendo prueba de los numeros romanos """
        self.assertEqual(num_romano.romanToInt("III"),3)
        self.assertEqual(num_romano.romanToInt("IV"),4)
        self.assertEqual(num_romano.romanToInt("IX"),9)
        self.assertEqual(num_romano.romanToInt("LVIII"),58)
        self.assertEqual(num_romano.romanToInt("MCMXCIV"),1994)   
        
    
    def test_remove_element(self):
        """Haciendo prueba para remover elementos"""
        self.assertEqual(remove_element.removeElement([3,2,2,3], 2), 2)
        self.assertEqual(remove_element.removeElement([0,1,2,2,3,0,4,2], 2), 5)
        


if __name__ == "__main__":
    unittest.main()