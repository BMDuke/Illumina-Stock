from src.bots.apibot import APIBot
from src.bots.ega import EGAMixin

class EGADatasetBot(EGAMixin, APIBot):

    '''
    Note: The EGAMixin must be the parameter on the left
    of APIBot for the correct initialisation to occur. 
    '''

    def __init__(self, limit=0, skip=0):
        '''
        '''

        url = 'https://ega-archive.org/metadata/v2/datasets'
        d = 'data/ega_dataset/raw'

        APIBot.__init__(self, target_url=url, target_dir=d)
        EGAMixin.__init__(self, limit=limit, skip=skip)



