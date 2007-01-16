#!/usr/bin/env python

import sys
import resource
import os
mem_limit = int(sys.argv[1])
resource.setrlimit(resource.RLIMIT_AS, (mem_limit, mem_limit))
resource.setrlimit(resource.RLIMIT_NPROC, (0,0))
# TODO: Correct the Maximum No of open Files! Currently not working
no_of_files = 3
#resource.setrlimit(resource.RLIMIT_NOFILE, (no_of_files, no_of_files))
cmd = sys.argv[2]
os.execv(cmd,[os.path.basename(cmd)])
