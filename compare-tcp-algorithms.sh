#!/bin/bash

#  MIT License
# 
#  Copyright (c) 2017 haltaro
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#  Author: haltaro <github.com/haltaro>
#  Reseacher in a Japanese company. His reseach interests are related to
#  network architectures, protocols, traffic control, mathematical modeling,
#  optimization, machine learning, and shiba dog :-)

ALGORITHMS=(TcpNewReno TcpHighSpeed TcpHybla TcpWestwood TcpWestwoodPlus TcpVegas TcpScalable TcpVeno TcpBic TcpYeah TcpIllinois TcpHtcp)

for item in ${ALGORITHMS[@]}; do
  echo "----- Simulating $item -----"
  ./waf --run "my-tcp-variants-comparison --transport_prot=$item --prefix_name='data/$item' --tracing=True --duration=20"
done

./plottcpalgo.py
