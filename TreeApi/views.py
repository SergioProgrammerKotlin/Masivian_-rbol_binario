from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.

@api_view(["POST"])
def BinaryTree(Binary_Tree):
    try:
        # Node class with its elements
        class Node:
            #Constructor
            def __init__ (self, value):
                self.value = value
                self.left = None
                self.right = None

        # Class Binary Tree with some rules for pre-order
        class Binary:
            # Constructor
            def __init__ (self):
                self.root = None
            #Insert method
            def insert(self, number):

                new_node = Node(number)

                if self == None:
                    self.root = new_node
                else:
                    current_node = self.root
                    while current_node is not 0:
                        if new_node < current_node:
                            new_node.left = current_node
                        else:
                            new_node.right = current_node

    
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)