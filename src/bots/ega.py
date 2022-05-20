
class EGAMixin(object):

    '''
    '''

    def __init__(self,  limit=0, skip=0):
        '''
        '''

        self.limit = limit
        self.skip = skip
        self.timeout = 30

    @staticmethod
    def get_type():
        '''
        Type of API
        '''

        return 'ega'        

    def get_number_of_results(self):
        '''
        '''
        
        response = self.fetch()

        if response.get('status') == 200:

            return response.get('content').get('response').get('numTotalResults')
        
        else:

            return response
        
    def set(self, **kwargs):
        '''
        '''

        for k, v in kwargs.items():

            if hasattr(self, k):

                setattr(self, k, v)

            else:

                raise Exception(f'Unknown attribute {k} for object {self}')    
    
    def trim_response(self, response):
        '''
        '''
        return response.get('response').get('result')


    def _make_url(self, url):
        '''
        '''
        params = {
            'limit':self.limit,
            'skip':self.skip
        }

        final_url = url + '?'

        for key, value in params.items():

            final_url += f'{key}={value}&'

        return final_url[0:-1]

    def _make_response(self, response):
        '''
        '''
        status_code = response.status_code

        content = response.json()

        return {
            'status':status_code,
            'content':content
        }

    def _make_error(self, exception):
        '''
        '''

        status_code = 503 # service unavailable

        return {
            'status':status_code,
            'content':exception
        }         

    