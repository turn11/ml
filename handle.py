#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import build_db as bd
import build_db_index as dbindex
import ml as ml

def simple_draw(label, y):
    plt.figure(figsize=(8, 4))
    plt.plot(y, label=label)
    plt.legend()
    plt.show()


def draw_date(files):
    x = []
    y = []
    mwcs = pd.get_minutes_counts_with_id(files)
    for mwc in mwcs:
        x.append(mwc[0])
        y.append(mwc[1])

    simple_draw(files, mwcs)


def draw_month():
    results = pd.get_month_total()
    print results

    plt.figure(figsize=(8, 4))
    plt.plot(results.__getslice__(0, 7), label="first week")
    plt.plot(results.__getslice__(7, 14), label="second week")
    plt.plot(results.__getslice__(14, 21), label="third week")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = ml.get_vector("gmszone")
    print data
    gmszone = ml.get_neighbors("gmszone")
    print gmszone
    result1 = ml.get_points("gmszone")
    print result1
    alesdokshanin = ml.get_points("alesdokshanin")
    print alesdokshanin