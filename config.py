import sys, os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://MasterDBUser:Downing2019@waterwedoingdatabaseinstance.cw5biyyyen32.us-east-1.rds.amazonaws.com:5432/waterwedoingDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 2