from structures_stats import DictKeyCounter, DictValueCollector

nested_structures = [
        {'first_row': 
            {
                'subtree': [
                    {
                        'some': {'genomic': 'yes'},
                        'another': {'genomic': 'also'}
                    },
                    {
                        'unrelated': {'genomic': 'yes'}
                    }
                ],
                'out of subtree': {
                    'genomic': 'out'
                }
            }
        },

        {'second_row': 
            {
                'subtree_but_object': {'genomic': 'only_one'},
            }
        }
]


counter = DictKeyCounter("genomic")

assert [4,1] == list(map(counter.count, nested_structures))


collector = DictValueCollector("genomic")
assert [['yes', 'also', 'yes', 'out'], ['only_one']] == list(map(collector.collect, nested_structures))
