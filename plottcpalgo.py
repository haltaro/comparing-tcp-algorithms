#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


def get_data(algo, variable='cwnd', duration=20.):
    # Function for getting and manipulating data.

    file_name = 'data/Tcp' + algo + '-' + variable + '.data'
    data = np.empty((0, 2))
    for line in open(file_name, 'r'):
        data = np.append(
            data, np.array([map(float, line[:-1].split())]),
            axis=0)
    data = data.T

    # For making data consistent with each other,
    # delete unnecessary columns and add the last column.
    data = data[:, data[0] < duration]
    if len(data[0]) == 0:
        data = np.append(
            data, np.array([[duration, 0]]).T,
            axis=1)
    else:
        data = np.append(
            data, np.array([[duration, data[1, -1]]]).T,
            axis=1)

    return data


def plot_cwnd_ack_rtt_each_algorithm(duration=20.):
    algos = ['NewReno', 'HighSpeed', 'Hybla', 'Westwood', 'WestwoodPlus',
             'Vegas', 'Scalable', 'Veno', 'Bic', 'Yeah', 'Illinois', 'Htcp']
    segment = 340  # 1 [segment] = 340 [byte]
    plt.figure()

    for algo in algos:
        plt.subplot(311)
        cwnd_data = get_data(algo, 'cwnd', duration)
        ssth_data = get_data(algo, 'ssth', duration)
        state_data = get_data(algo, 'cong-state', duration)

        # Since the initial value of ssthresh is too large,
        # we have to limit the range of y-axis.
        ymax = max(cwnd_data[1] / segment) * 1.1

        # Fill colors according to congestion states:
        # 0: OPEN:     blue
        # 1: DISORDER: green
        # 3: RECOVERY: yellow
        # 4: LOSS:     red
        # Initial congestion state is OPEN (1).
        plt.fill_between(cwnd_data[0], cwnd_data[1] / segment,
                         facecolor='lightblue')
        for n in range(len(state_data[0]) - 1):
            fill_range = cwnd_data[0] >= state_data[0, n]
            if state_data[1, n] == 1:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='lightgreen')
            elif state_data[1, n] == 3:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='khaki')
            elif state_data[1, n] == 4:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='lightcoral')
            else:  # OPEN
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='lightblue')
        plt.plot(cwnd_data[0], cwnd_data[1] / segment, drawstyle='steps-post',
                 color='b', label='cwnd')
        plt.plot(ssth_data[0], ssth_data[1] / segment, drawstyle='steps-post',
                 color='b', linestyle='dotted', label='ssth')
        plt.ylim(0, ymax)
        plt.ylabel('cwnd [segment]')
        plt.legend()
        plt.title(algo)

        plt.subplot(312)
        ack_data = get_data(algo, 'ack', duration)
        plt.plot(ack_data[0], ack_data[1] / segment, drawstyle='steps-post',
                 color='r')
        plt.ylabel('ACK [segment]')

        plt.subplot(313)
        rtt_data = get_data(algo, 'rtt', duration)
        plt.plot(rtt_data[0], rtt_data[1], drawstyle='steps-post', color='g')
        plt.ylabel('RTT[s]')

        plt.xlabel('Time [s]')
        plt.savefig('data/Tcp' + algo + str(int(duration)).zfill(3) +
                    '-cwnd-ack-rtt.png')
        plt.clf()
    plt.show(block=False)
    plt.close()


def plot_cwnd_all_algorithms(duration=20.):
    algos = ['NewReno', 'HighSpeed', 'Hybla', 'Westwood', 'WestwoodPlus',
             'Vegas', 'Scalable', 'Veno', 'Bic', 'Yeah', 'Illinois', 'Htcp']
    segment = 340  # 1 [segment] = 340 [byte]

    plt.figure(figsize=(15, 10))
    for i, algo in enumerate(algos):
        plt.subplot(3, 4, i + 1)
        cwnd_data = get_data(algo, 'cwnd', duration)
        ssth_data = get_data(algo, 'ssth', duration)
        state_data = get_data(algo, 'cong-state', duration)

        # Fill colors according to congestion states:
        # 0: OPEN:     blue
        # 1: DISORDER: green
        # 3: RECOVERY: yellow
        # 4: LOSS:     red
        # Initial congestion state is OPEN (1).
        plt.fill_between(cwnd_data[0], cwnd_data[1] / segment,
                         facecolor='lightblue')
        for n in range(len(state_data[0]) - 1):
            fill_range = cwnd_data[0] >= state_data[0, n]
            if state_data[1, n] == 1:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='lightgreen')
            elif state_data[1, n] == 3:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='khaki')
            elif state_data[1, n] == 4:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='lightcoral')
            else:
                plt.fill_between(
                    cwnd_data[0, fill_range], cwnd_data[1, fill_range] / segment,
                    facecolor='lightblue')
        plt.plot(cwnd_data[0], cwnd_data[1] / segment, drawstyle='steps-post')
        plt.plot(ssth_data[0], ssth_data[1] / segment, drawstyle='steps-post',
                 color='b', linestyle='dotted')

        # Since the initial value of ssthresh is too big,
        # we have to limit the range of y-axis.
        plt.ylim(0, 1200)
        plt.title(algo)

    plt.savefig('data/TcpAll' + str(int(duration)).zfill(3) + '-cwnd.png')
    plt.show(block=False)
    plt.close()


if __name__ == '__main__':
    print "----- Plotting cwnd of all algorithms -----"
    plot_cwnd_all_algorithms()
    print "----- Plotting cwnd, ACK, and RTT of each algorithm -----"
    plot_cwnd_all_algorithms()
