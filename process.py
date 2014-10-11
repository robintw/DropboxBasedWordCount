import os
from glob import glob
from dateutil.parser import parse
import pandas as pd
from subprocess import *


def do_count(globstring):
    files = glob(globstring)

    results = []

    for f in files:
        print f
        try:
            res = int(Popen(
                [r'C:\Perl64\bin\wperl.exe', r'C:\Program Files\MiKTeX 2.9\scripts\texcount\perl\texcount.pl', '-brief',
                 '-total', '-1', '-sum', f], shell=True, stderr=STDOUT, stdout=PIPE).communicate()[0])
        except:
            continue

        splitted = os.path.basename(f).split("_")
        datestr = " ".join(splitted[:4])
        timestr = splitted[4]
        timestr = timestr[:2] + ":" + timestr[2:4] + ":" + timestr[4:]

        print datestr
        print timestr

        results.append({'timestamp': parse(datestr + " " + timestr),
                        'wordcount': res})

    return results


def do_all_counts(root):
    folders = [x[0] for x in os.walk("C:\TestRevisions")][1:]
    for folder in folders:
        res = do_count(os.path.join(folder, '*.tex'))
        df = pd.DataFrame(res)
        df.to_pickle(os.path.join(root, "%s.pd" % folder))


def process_df_monthly(filename):
    df = pd.read_pickle(filename)
    df.index = pd.DatetimeIndex(df.timestamp)
    del df['timestamp']
    df.columns = [os.path.splitext(os.path.basename(filename))[0]]
    return df.resample('D', 'last').fillna(method='ffill')


def make_plot():
    res = period_of_int.plot(subplots=True, legend=False, grid=False, style=['r', 'g', 'b', 'y', 'k'])
    for ax in res:
        ax.yaxis.set_label_position('left')
        ax.yaxis.set_ticklabels([])
        ax.set_ylabel(ax.legendlabels[0], labelpad=20, rotation=0, horizontalalignment='right')
        ax.grid(axis='x', which='both')
