from src.bots.ega_dac import EGADacBot
from src.bots.ega_dataset import EGADatasetBot
from src.bots.ega_experiment import EGAExperimentBot
from src.bots.ega_study import EGAStudyBot
from src.bots.illumina import IlluminaBot
from src.bots.nasdaq import NasdaqBot
from src.bots.snp import SnPBot



config = {

    'illumina':{
        'bot':IlluminaBot,
        'chunksize':100,
        'timeout':0, 
        'max_workers':20,
        'pause':0,
    }, 

    'snp':{
        'bot':SnPBot,
        'chunksize':100,
        'timeout':0, 
        'max_workers':20,
        'pause':0,
    }, 

    'nasdaq':{
        'bot':NasdaqBot,
        'chunksize':100,
        'timeout':0, 
        'max_workers':20,
        'pause':0,
    }, 

    'datasets':{
        'bot':EGADatasetBot,
        'chunksize':100,
        'timeout':30, 
        'max_workers':20,
        'pause':0,
    }, 

    'experiments':{
        'bot':EGAExperimentBot,
        'chunksize':2000000,
        'timeout':3600, 
        'max_workers':1,
        'pause':0,
    }, 

    'studies':{
        'bot':EGAStudyBot,
        'chunksize':100,
        'timeout':30, 
        'max_workers':20,
        'pause':0,
    }, 

    'dacs':{
        'bot':EGADacBot,
        'chunksize':100,
        'timeout':60, 
        'max_workers':2,
        'pause':0,
    }, 
}