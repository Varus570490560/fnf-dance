import configparser


class Config:
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read('../config/config.ini')
        self.input_dir = cf.get('path', 'input_dir')
        self.output_dir = cf.get('path', 'output_dir')
