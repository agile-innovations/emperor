#!/usr/bin/env python
from __future__ import division

from jinja2 import Template
from random import sample
from sys import argv

import numpy as np


def listify(a):
    return np.asarray(a, dtype='str').tolist()

with open('new-emperor.html', 'w') as f, open('template.html') as temp:
    template = Template(temp.read())

    N = 10
    if len(argv) > 1:
        N = int(argv[1])

    categories = np.asarray(np.random.randint(1, 1000, N), str)

    coords_ids = listify(np.arange(N))
    coords = listify(np.random.randn(N, 10))
    pct_var = listify(1/np.exp(np.arange(10)))

    md_headers = ['SampleID', 'DOB']
    metadata = []
    for _id in coords_ids:
        metadata.append([_id, ''.join(sample(categories, 1))])

    f.write(template.render(coords_ids=coords_ids, coords=coords,
                            pct_var=pct_var, md_headers=md_headers,
                            metadata=metadata))
