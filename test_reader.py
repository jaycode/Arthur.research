import unittest
from pymongo import MongoClient
import pdb

import os, sys, inspect
# Including subdirectory with current file as starting reference point.
lib_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],'..','libs')))
if lib_path not in sys.path:
  sys.path.insert(0, lib_path)

import arthur

class TestReader(unittest.TestCase):
  def test_reading_zip(self):

    ### Reading side ###
    pdb.set_trace()
    reader = arthur.Reader()
    reader.read_zip('DRAS_sample_v1_20150605.zip')
    assert len(reader.documents) > 0
    # Each data point inside a document must have the following features:
    # - value: Text value, could be a meaningless value like "Back" or useful one like
    #          "3150 Rutland Rd, Victoria, British Columbia".
    # - is_repeated: Is this data point repeated throughout many documents?
    # - char_length: Length of characters.
    # - pos_x: x position in document.
    # - pos_y: y position in document.
    # And maybe the following, but let's work on this later.
    # For our initial system we will just read with fixed rules.
    # - closest_word_right: Closest word at its right.
    # - closest_word_bottom: Closest word at its bottom.
    # - blahblahblah later

    # Documents as numpy array:
    # 
    # Doc#   char_length    pos_x   pos_y
    #    1           123       20     200
    #    1           122       25     202
    # documents(Documents object) -> document(Document object) -> data point(numeric)
    data_point = reader.documents[0][0][0]


    ### Learning side ###
    context = {
      n: 10, # Number of features to learn.
      topic: None # Later, used for guessing required features.
    }
    learner = arthur.Learner(reader.documents, context)
    data = learner.data

  def later():
    features = reader.features
    mongo_client = MongoClient("mongodb://localhost:27017")
    db = mongo_client.arthur
    db.test_features.remove()
    db.test_features.insert(features)