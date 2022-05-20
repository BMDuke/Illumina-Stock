#!/usr/bin/python

import os
import sys

from src.utils.tabulator import Tabulator
from src.utils.headers import headers
from src.utils.bot_config import config as bot_club

RETRIES=10
MAX_WORKERS=2

'''
args:
> illumina
> snp
> nasdaq
> datasets
> experiments
> studies
> dacs
> all

Create pretty table with default values
'''



if __name__ == "__main__":

    datasources = sys.argv[1:]

    # api = EGAExperimentBot(limit=10)
    # print(api.get_number_of_results())

    if 'all' in datasources:

        sources = bot_club.keys()

    else:

        sources = datasources


    for s in sources:

        source = bot_club.get(s)

        bot = source.get('bot')
        chunksize = source.get('chunksize')
        
        if bot.get_type() == 'ega': 

            api = bot(limit=1)
        
        else:

            raise Exception('No other bot is defined')                

        raw_filepath = api.target_dir
        target_filepath = os.path.split(raw_filepath)[0]
        header = headers.get(s)

        tabulator = Tabulator(raw_dir=raw_filepath, out_dir=target_filepath, headers=header)
        success = tabulator.tabulate()

        print('Execution success: ', success)


        





            



    