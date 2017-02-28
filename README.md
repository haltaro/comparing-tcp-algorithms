# comparing-tcp-algorithms

Codes for comparing TCP congestion control algorithms with ns-3 and visualizing with matplotlib.

# Requirements

I assume Linux system. You have to install:
* [ns-3](https://www.nsnam.org/): Refer to [tutorial](https://www.nsnam.org/docs/release/3.26/tutorial/html/index.html). I used version 3.26.
* Python: I used version 2.7.11.
* [NumPy](http://www.numpy.org/): For data manipulation. I used version 1.10.4.
* [matplotlib](http://matplotlib.org/): For visualization. I used version 1.5.1.

# Model

## Congestion state

Based on [ns-3 implementation](), I assume the congestion states shown below:
* OPEN:
* DISORDER:
* RECOVERY:
* LOSS: 

## Congestion control algorithms

Based on [ns-3 implementation](), I assume the congestion control algorithms shown below:

|Algorithm|`TypeId`|source|
|:--|:--|:--|
|[NewReno](https://tools.ietf.org/html/rfc6582) | `TcpNewReno`| [`tcp-congestion-ops.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-congestion-ops_8cc.html)|
|[HighSpeed](https://tools.ietf.org/html/rfc3649) | `TcpHighSpeed`|[`tcp-highspeed.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-highspeed_8cc.html) |
|[Hybla](http://www.mathcs.emory.edu/~cheung/Courses/558/Syllabus/Papers/TCP-Hybla.pdf) | `TcpHybla`| [`tcp-hybla.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-hybla_8cc.html) |
|[Westwood](https://pdfs.semanticscholar.org/d3f0/a499906d7821cf204d9ca26900c11179777e.pdf) | `TcpWestwood`| [`tcp-westwood.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-westwood_8cc.html) |
|Westwood+ | `TcpWestwoodPlus`| [`tcp-westwood.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-westwood_8cc.html) |
|[Vegas](http://cseweb.ucsd.edu/~rbraud/jsac.pdf) | `TcpVegas` | [`tcp-vegas.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-vegas_8cc.html) |
|[Scalable](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.107.5330&rep=rep1&type=pdf) | `TcpScalable`| [`tcp-scalable.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-scalable_8cc.html) |
|[Veno](http://ieeexplore.ieee.org/document/1177186/) | `TcpVeno`| [`tcp-veno.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-veno_8cc.html) |
|[Bic](http://infocom2004.ieee-infocom.org/Papers/52_4.PDF) | `TcpBic`| [`tcp-bic.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-bic_8cc.html) |
|[YeAH](http://infocom.uniroma1.it/~vacirca/yeah/yeah.pdf) | `TcpYeah`| [`tcp-yeah.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-yeah_8cc.html) |
|[Illinois](http://dl.acm.org/citation.cfm?id=1190166) | `TcpIllinois`| [`tcp-illinois.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-illinois_8cc.html) |
|[H-TCP](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.3.7816&rep=rep1&type=pdf) | `TcpHtcp`| [`tcp-htcp.cc`](https://www.nsnam.org/docs/release/3.26/doxygen/tcp-htcp_8cc.html) |

# Installation


# Codes

## `tcp-algorithm-comparison.sh`

## `my-tcp-variants-comparison.cc`

## `plottcpalgo.py`

# Enjoy comparison
Just run `my-tcp-variants-comparison.sh`.

```bash
$ cd ~/ns-3.26/source/ns-3.26
$ ./my-tcp-variants-comparison.sh
```

## 

# License
* `my-tcp-variants-comparison.sh` and `plottcpalgo.py`: MIT
* `my-tcp-variants-comparison.cc`: GNU GPLv2
