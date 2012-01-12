#!/usr/bin/env jython

import sys

from kahuna.lookup import Lookup
from kahuna.session import ContextLoader


if len(sys.argv) == 2:
    context = ContextLoader().load_context()
    try:
        lookup = Lookup(context)
        lookup.lookup_vm(sys.argv[1])
    finally:
        context.close()
else:
    print "Usage: %s <vm name>" % sys.argv[0]
