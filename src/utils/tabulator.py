import os
import csv
import json
import pandas

class Tabulator(object):

    '''
    Converts many raw json files into one combined 
    csv
    '''

    def __init__(self, raw_dir=None, out_dir=None, filename='data.csv', 
                    headers=None, delimiter=':'):
        '''
        '''
        self.raw_dir = raw_dir
        self.out_dir = out_dir
        self.filename = filename
        self.headers = headers
        self.delimiter = delimiter

    def tabulate(self):
        '''
        '''
        raw_dir = self.raw_dir

        self._init_table()

        files = self._list_files(raw_dir)

        successes = []

        for file in files:

            data = self._load_json(file)
            data = self._json_to_table(data)
            
            for row in data:

                is_success = self._write_row(row)
                successes.append(is_success)
        
        return all(successes)

    def _list_files(self, raw_dir):
        '''
        '''
        return [os.path.join(raw_dir, f) 
                    for f in os.listdir(raw_dir) 
                    if os.path.isfile(os.path.join(raw_dir, f)) and f.endswith('.json')]

    def _load_json(self, file):
        '''
        '''

        try:

            with open(file) as json_file:
                data = json.load(json_file)
                return data

        except Exception as e:

            raise e

    def _json_to_table(self, data):
        '''
        '''

        table = []

        for record in data:

            row = self._parse_json(record)
            table.append(row)

        return table

    def _parse_json(self, record):
        '''
        '''

        row = []

        for column in self._header('pattern'):

            path = column.split(self.delimiter)

            value = None

            for step in path:
                
                value = record.get(step)
            
            row.append(value)
        
        return row        

    def _init_table(self):
        '''
        '''

        row = self._header('name')

        self._write_row(row, method='w')
        

    def _header(self, method):
        '''
        Headers is a list of name, pattern tuples uesd for 
        parsing raw json
        '''

        if method == 'name':

            return [h for h, _ in self.headers]
        
        elif method == 'pattern':

            return [h for _, h in self.headers]
        
        else:

            raise Exception(f'Uknonwn method \'{method}\' to parse headers in Tabulator._header(method)')

    def _write_row(self, row, method='a'):
        '''
        '''

        filepath = self._make_filepath()

        try:

            with open(filepath, method, newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(row)
            
            return True
        
        except Exception as e:

            return False
    
    def _make_filepath(self):
        '''
        '''
        if not hasattr(self, '_fout'):

            self._fout = os.path.join(self.out_dir, self.filename)
        
        return self._fout
