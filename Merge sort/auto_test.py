#!/bin/python3
import random
import os
from argparse import ArgumentParser as ap
from matplotlib import pyplot as plt
import time
import numpy as np

def main():
    parser = ap(prog = 'auto_test.py',description = 'Checks the time taken for sorting algorithm for best, worst and average cases',epilog='SortTester@zrn')
    parser.add_argument("count_inputs",default=10000,type=int,help="Number of samples to generate")
    parser.add_argument("-m", "--method",type=str,default="average",help="Method used to generate samples. Can be [average,bestcase,worstcase].")
    parser.add_argument("-s","--steps",default=10,type=int,help="Number of steps to use")
    args = parser.parse_args()
    gen_func = {"average" : average,
    "bestcase" : bestcase,
    "worstcase" : worstcase,}
    
    try:
        times = []
        n_vals = []
        for i in np.array(np.linspace(int(args.count_inputs*0.1),args.count_inputs,args.steps),dtype=np.int32):
            fp = gen_func[args.method](i)
            start = time.time()
            os.system("./a.out  > /dev/null < " + fp)
            times.append(time.time() - start)
            n_vals.append(i)
        
        print("\n".join([f"{n} samples : {s}s" for n,s in zip(n_vals,times)]))
        fig, ax = plt.subplots()
        plt.plot(n_vals,times)
        for i in range(len(times)):
            plt.annotate("{:.2f}".format(times[i]),xy=(n_vals[i],times[i]))
        plt.show()
            
        
    except KeyError:
        print("Invalid generator function, please use one of [average,bestcase,worstcase].")

def average(n : int) -> str:
    with open("testcase.txt","w") as f:
        f.write(str(n) + " ")
        f.write(" ".join([str(random.randint(1,100000000)) for i in range(n)]))
        f.close()
    return "testcase.txt"

def bestcase(n : int) -> str:
    with open("testcase.txt","w") as f:
        f.write(str(n) + " ")
        f.write(" ".join([str(i) for i in range(n)]))
        f.close()
    return "testcase.txt"

def worstcase(n : int) -> str:
    with open("testcase.txt","w") as f:
        f.write(str(n) + " ")
        f.write(" ".join([str(i) for i in range(n,0,-1)]))
        f.close()
    return "testcase.txt"


if __name__ == '__main__':
    main()


