from src.bots.apibot import APIBot

class NasdaqBot(APIBot):

    '''
    '''

    def __init__(self):
        '''
        '''

        url = '?'
        d = '?'
        timeout = None

        super().__init__(target_url=url, target_dir=d, timeout=timeout)