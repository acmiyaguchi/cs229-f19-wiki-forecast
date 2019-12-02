import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import csv
import sys
import pdb

def plot_hist(df):
    
    xlabels = df.index.values
    y = df[('rmse', 'mean')]
    stdv = df[('rmse', 'std')]

#    fig, ax = plt.subplots()
       
    ax = df.plot.bar(y=('rmse', 'mean'))
    ax.errorbar(xlabels, df[('rmse', 'mean')],
        yerr=df[('rmse', 'std')], fmt='none')
    # x = np.arange(len(xlabels))
    # width=0.35
    # rects = []
    # for i in range(len(xlabels)):
        # rect = ax.bar(x - 0.5 * width,
            # df.iloc[:][('rmse', 'mean')],
            # width,
            # label=str(i))
        # rects.append(rect)        

    # ax.set_ylabel('RMSE')
    # ax.set_xticks(x)
    # ax.set_xticklabels([str(i) + ': ' + xlabels[i] for i in range(len(xlabels))])
    # ax.legend()
    
    plt.show()
#    plt.save(file='{0}.png'.format(filename))


def main(summary_data_file):
    with open(summary_data_file) as f:
        r = csv.reader(f)
        records = [ x[1:] for x in r ]
        header = records[0]
        records = records[1:]
        print('Read lines=', len(records))
    summary = pd.DataFrame(records, columns=header).astype({
      'mape': np.float,
      'rmse': np.float,
      'trial_id': np.int,
      'name': 'str'
    })
    print(summary)
    print(summary.info())
    pdb.set_trace()
    df = summary.groupby(['name']).agg({
       'rmse': ['min', 'max', 'mean', 'std', 'count'],
       'mape': ['min', 'max', 'mean', 'std', 'count']
      })
    print(df)
    plot_hist(df)

if __name__ == '__main__':
  main(sys.argv[1])