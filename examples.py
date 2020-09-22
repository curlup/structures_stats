import pandas as pd

from . import DictKeyCounter, DictValueCollector

df = pd.DataFrame({
    'id': [1, 2], 
    'nested_structure': [
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
})

counter = DictKeyCounter("genomic")
df.assign(genomic_count=lambda r: counter.count(r.nested_structure))


collector = DictValueCollector("genomic")
df.assign(genomic_types=lambda r: collector.collect(r.nested_structure))


