headers = {}

## Datasets
name = 'datasets'
header = [  'uuid',
            'date_created',
            'date_publised',
            'published',
            'released',
            'title',
            'description',
            'technology',
            'num_samples',
            'dataset_types',
            'dataset_links',
            'attributes',
            'policy_id',
            'files',
            'access_type',
            ]

pattern = [ 'egaStableId',
            'creationTime',
            'releasedDate',
            'published',
            'released',
            'title',
            'description',
            'technology',
            'numSamples',
            'datasetTypes',
            'datasetLinks',
            'attributes',
            'policyStableId',
            'files',
            'accessType',
            ]

headers[name] = [(h, p) for h, p in zip(header, pattern)]

## Studies
name = 'studies'
header = [  'uuid',
            'date_created',
            'date_publised',
            'published',
            'released',
            'title',
            'description',
            'abstract',
            'study_type',
            'pubmed_id',
            'tags'
            ]

pattern = [ 'egaStableId',
            'creationTime',
            'releasedDate',
            'published',
            'released',
            'title',
            'description',
            'studyAbstract',
            'studyType',
            'pubMedIds',
            'customTags',
            ]

headers[name] = [(h, p) for h, p in zip(header, pattern)]

## Dacs
name = 'dacs'
header = [  'uuid',
            'date_created',
            'published',
            'released',
            'title',
            'url',
            'contacts',
            ]

pattern = [ 'egaStableId',
            'creationTime',
            'published',
            'released',
            'title',
            'url',
            'contacts',
            ]

headers[name] = [(h, p) for h, p in zip(header, pattern)]
