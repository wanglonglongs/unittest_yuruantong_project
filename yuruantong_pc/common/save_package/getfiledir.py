import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATADIR = os.path.join(dir, 'data')

CONFDIR = os.path.join(dir, 'config')

BASEFACTORYDIR = os.path.join(dir, 'basefactory')

RESULTDIR = os.path.join(dir, 'result')

LOGDIR = os.path.join(RESULTDIR, 'log')

REPORTDIR = os.path.join(RESULTDIR, 'report')

SCREENSHOTDIR = os.path.join(RESULTDIR, 'screenshot')

CASEDIR = os.path.join(dir, 'tests')

#print(SCREENSHOTDIR)


