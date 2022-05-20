from src.bots.apibot import APIBot

class SnPBot(APIBot):

    '''
    '''

    def __init__(self):
        '''
        '''

        url = '?'
        d = '?'
        timeout = None

        super().__init__(target_url=url, target_dir=d, timeout=timeout)