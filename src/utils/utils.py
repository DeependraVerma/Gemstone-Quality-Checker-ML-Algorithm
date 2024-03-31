import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.exception.exception import customexception
from src.logger.logging import logging

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        logging.info('save object from save_object function utils')

    except Exception as e:
        logging.info('Exception Occured in save_object function utils')
        raise customexception(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            pickle.dump(file_obj)
        logging.info('load object from load_object function utils')
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise customexception(e,sys)
    
def evaluate_model(true,pred):
    try:
        report = {}
    except Exception as e:
        logging.info('Exception Occured in evaluate_model function utils')
        raise customexception(e,sys)