#!/usr/bin/python

import sys
import math
import tqdm
import multiprocessing

from src.utils.bot_config import config as bot_club

RETRIES=10
MAX_WORKERS=20

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


'''
For bot in bots
    Fetch total number to retrieve
    Define chunksize
    Define start and stop 
    For chunk in range
        Create a new process
        Fetch data
        If successful
            save
                If save successsful
                    continue
                else
                    retry
        Else
            retry
'''

def fetch_data(bot_config, idx, skip=None, limit=None, start=None, stop=None):
    '''
    '''

    bot = bot_config.get('bot')
    timeout = bot_config.get('timeout')

    if (skip is not None) and (limit is not None):
        api = bot(skip=skip, limit=limit)
    elif (start is not None) and (stop is not None):
        api = bot(start=start, stop=stop)

    api.set(timeout=timeout)

    filename = f"{idx}.json"
    filepath = api.make_filepath(filename)

    fetch_success = False
    save_success = False    
    fetch_retries = RETRIES
    save_retries = RETRIES

    while (not fetch_success) and (fetch_retries > 0):

        response = api.fetch()

        if response.get('status') == 200:

            fetch_success = True

            while (not save_success) and (save_retries > 0):

                result = api.trim_response(response.get('content'))

                save_success = api.save_json(result, filepath)

                save_retries -= 1
            
            fetch_retries -= 1
        
    if not fetch_success:

        print(f'FETCH FAILED FOR {idx}')

    return (fetch_success, fetch_retries)



def process(bot_config, num_results):
    '''
    '''

    bot = bot_config.get('bot')
    chunksize = bot_config.get('chunksize')
    max_workers = bot_config.get('max_workers')
    pause = bot_config.get('pause')

    ##### THIS NEEDS TO BE GENERALISED
    limit = chunksize
    skip = 0


    num_chunks = math.ceil(num_results / chunksize)

    is_complete = False
    active_workers = {i: {} for i in range(max_workers)}
    count = 0

    print(f'Fetching data from {bot().target_url}')

    progress_bar = tqdm.tqdm(total=num_chunks)

    while not is_complete:
        
        spawn = 0
        spaces = []
        repeats = []

        # Initialisation
        for pid, process in active_workers.items(): # Loop through active workers
            if process:
                worker = process['worker']  # Get the worker
                data = process['data']  # Get the data assigned to the worker
                if not worker.is_alive(): # If the worker has completed
                    spawn += 1  # We have room for a new worker
                    spaces.append(pid) # So free up their space
                    if not worker.exitcode == 0: # If the exit code was not 0, something went wrong, we need to repeat
                        repeats.append(data) # Repeat this chunk
                    worker.join() # Rest well, worker
            else:
                spawn = max_workers
                spaces = list(active_workers.keys())
        
        for repeat in repeats:
            keywords = {'limit':repeat.get('limit'), 'skip':repeat.get('skip')}
            worker = multiprocessing.Process(target=fetch_data, args=(bot_config, count), kwargs=keywords)
            worker.start()
            pid = spaces.pop()
            active_workers[pid] = {
                'worker': worker,
                'data': repeat
            }
            spawn -= 1
            count += 1
            skip += chunksize
            # print(f'Process started: id {pid} - restart')




        
        for _ in range(spawn):

            if count > num_chunks:
                is_complete = True
                [process['worker'].join() for _, process in active_workers.items()]
                break

            keywords = {'limit':limit, 'skip':skip}
            worker = multiprocessing.Process(target=fetch_data, args=(bot_config, count), kwargs=keywords)
            worker.start()
            pid = spaces.pop()
            active_workers[pid] = {
                'worker': worker,
                'data': keywords
            }
            spawn -= 1
            count += 1
            skip += chunksize

            progress_bar.update(1)
            # print(f'Process started: id {pid}')   

    
    progress_bar.close()             










if __name__ == "__main__":

    print(sys.argv)

    datasources = sys.argv[1:]

    # api = EGAExperimentBot(limit=10)
    # print(api.get_number_of_results())

    if 'all' in datasources:

        sources = bot_club.keys()

    else:

        sources = datasources


    for s in sources:

        bot_config = bot_club.get(s)

        bot = bot_config.get('bot')
        
        if bot.get_type() == 'ega': 

            api = bot(limit=1)
        
        else:

            raise Exception('No other bot is defined')                

        num_results = api.get_number_of_results()

        print('\nnum_results: ', num_results)

        process(bot_config, num_results)





            



            


# if __name__ == "__main__":
#     limit=10
#     skip=0
#     api = EGADacBot(limit=limit, skip=skip)
#     response = api.fetch()
#     if response.get('status') == 200:
#         payload = response.get('content').get('response').get('result')
#         api.pprint(payload)
#         success = api.save_json(payload, api.target_dir + '/' + 'test.json')
#         print('success: ', success)


    