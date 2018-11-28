#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:44:18 2018

@author: davidxiong
"""

class Tree:
    def __init__(self,cargo,left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.cargo

    def print_tree_postorder(tree):
        if tree is None: return
        print_tree_postorder(tree.left)
        print_tree
 
    
def showtree(tree):
    if tree==None: return
    print(tree.cargo, end ='')
    showtree(tree.left)
    showtree(tree.right)

def get_number(token_list):
    if get_token(token_list,"("):
        x = get_sum(token_list)
        if not get_token(token_list,")"):
            raise ValueError('missing close parenthesis')
        return x
    else:



    
    


