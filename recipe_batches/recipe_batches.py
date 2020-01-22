#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  my_list = []
  if len(ingredients) < len(recipe):
    return 0
  for key in recipe: 
      my_list.append(ingredients[key]/recipe[key])
  return math.floor(min(my_list))
   
'''
  if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
'''


#print(my_ing['milk'])

print(recipe_batches({ 'milk': 2 }, { 'milk': 200 }))