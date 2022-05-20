import requests
import json
import os

class APIBot(object):

    '''
    This is the base class for the bots that are going to 
    scrape the APIs and produce the raw data to build the
    dataset.

    > Fetch data from API as JSON
    > Return status code 
    > Write result to disk as .json
    '''

    # Class attrs

    def __init__(self, target_url=None, target_dir=None, timeout=None, verbose=False):
        '''
        '''
        self.target_url = target_url
        self.target_dir = target_dir
        self.timeout = timeout
        self.verbose = verbose

    def fetch(self):
        '''
        '''
        if self.verbose:
            self._print_fetching()

        headers = self._make_headers()
        url = self._make_url(self.target_url)

        try:

            response = requests.get(url, headers=headers, timeout=self.timeout)

            return self._make_response(response)

        except Exception as e:
            
            return self._make_error(e)
            
        

    def save_json(self, object, filename):
        '''
        '''
        try:

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(object, f, ensure_ascii=False, indent=4)        
            
            return True
        
        except:

            return False

    def pprint(self, input):
        '''
        '''
        print(json.dumps(input, indent=4, sort_keys=True))

    def make_filepath(self, fname):
        '''
        '''

        return os.path.join(self.target_dir, fname)                    

    def _make_headers(self):
        '''
        '''
        return {}
    
    def _parse_response_header(self, header):
        '''
        '''
        pass

    def _make_response(self, response):
        '''
        '''
        return response

    def _make_error(self, exception):
        '''
        '''
        return exception        
    
    def _make_url(self, url):
        '''
        '''
        return url
    
    def _print_fetching(self):
        '''
        '''
        pass
    

    






if __name__ == "__main__":
    url = 'https://www.yahoofinanceapi.com/'
    d = '/home/stephen/Desktop/illumina_stock/data'
    api = APIBot(target_url=url, target_dir=d)