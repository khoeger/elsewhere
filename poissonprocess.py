"""
From Leemis, 2011
Pg. 186

    Poisson Process
        Given
            event x, number of which is modelled by poisson process
            lambda = arrival rate
            (a,b]  = time interval

        f(x) = [(lambda( b - a ))**x * e **(-lambda(b-a))]/
                [x!]


    This tells us the number of events.

    We care about the incidence time of the events.

Pg. 188

    Erlang time to nth event
        f(x) = [lambda(lambda * x)** (n-1) * e ** (-lambda * x)]/
                (n-1)!
Pg. 190
    The event times have the same distriubtion as  a Poisson number of random
    variables that are uniformly distributed over the interval.

We want to generate arrival times. So,
Law, Pg. 375
    arrival times, arrival Process
        A_i = t_i - t_i-1 , interarrival time between (i-1)st and ith events

        - events arrive one at a time
        - N(t+s) - N(t) (arrivals in time interval)
            does not depend on what time it is.
        - N(t+s) - (N(t)) indepednent of t for all t, s >=0, so memoryless. Prior events
            do not effect later events in same series.

        P[N(t+s)-N(t)=k] = [e**(-lambda*s)(lambda*s)^**k]/(k!)
        k= 0,1,2,...
        t,s >=0


Law, Pg. 473
    Generating Possion Process
        has IID exponential r.v. arrival times A_i = t_i - t_i-1
        have common mean 1/lambda

        generate t_is, the times of arrival recurssively as follows.

        1.U~U(0,1)
        2. Return t_i = t_i-1 - (1/lambda)* ln U

"""

import random
