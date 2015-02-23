import random

def prob(p):
    number_of_times_loop_goes = 100
    number_of_successes = 0.0
    print p
    for i in xrange(number_of_times_loop_goes):
        randThing = random.random()
        print randThing
        if randThing < p:
            number_of_successes += 1.0
    print number_of_successes
    print p


if __name__ == '__main__':
    import sys
    prob(float(sys.argv[1]))
