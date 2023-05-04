import random
from textwrap import dedent
from math import factorial
from time import time

DRUM_SZ = 12
TICK_SZ = 4

# n - num poss to start
# r - num selections

def num_perms(n,r):
    prod = 1
    for x in range(n,n-r,-1):
        prod *=x
    return prod

def num_combs(n,r):
    prod=1
    for x in range(n,r,-1):
        prod *= x
    return prod//factorial(n-r)

def pull_from_drum(drum: list[int]):    # for manual running
    result = random.choice(drum)
    drum.remove(result)
    return result

def manual_run():
    drum = [*range(1,DRUM_SZ+1)]

    ticket = [*range(1,DRUM_SZ+1)]
    random.shuffle(ticket)
    ticket = ticket[:4]

    num_match = 0

    print(f"Your ticket: {ticket}\n")
    print('-'*25)

    for p in range(TICK_SZ):
        print(f"\nPull {p+1}/{TICK_SZ}: ")

        result = pull_from_drum(drum)
        print(f"Pulled: {result}")

        if result in ticket:
            print("This number matched a number on your ticket!")
            num_match += 1
        else:
            print("This number did not match your ticket!")

    print()
    if num_match == TICK_SZ:
        print("The numbers pulled matched your ticket exactly! Big Win!")
    else:
        print(dedent("""\
        Only {}/{} of the numbers on your ticket were pulled!
        Better luck next time! \
        """.format(num_match, TICK_SZ)
    ))
    return (num_match, TICK_SZ)

def auto_run(num_tries, drum_sz, tick_sz):
    result_freq = {n: 0 for n in range(tick_sz+1)}
    d_A = [*range(drum_sz)]
    d_B = [*range(drum_sz)]

    for _ in range(num_tries):
        random.shuffle(d_A)
        random.shuffle(d_B)

        drum, ticket = map(sorted, (d_A[:4], d_B[:4]))

        num_match = 8-len(set(drum+ticket))
        result_freq[num_match] += 1

    return result_freq

def ideal_pct(drum_sz, tick_sz):
    perms_matching = factorial(tick_sz)
    perms_tot = num_perms(drum_sz, tick_sz) 

    return round(100*(perms_matching/perms_tot), 10)

def main():
    tick_sz = 4
    drum_sz = 12
    num_tries = 100_000

    t0 = time()
    freqs = auto_run(num_tries, drum_sz, tick_sz)
    t1 = time()
    print(f"Time elapsed: {round((t1-t0)*1000, 5)}ms")

    for (k,v) in freqs.items():
        pct_freq = round(100*(v/num_tries),5)
        print(
            "{}/{} Matching: {:,}/{:,} ({:.3f}% occurrence)" \
                .format(k, tick_sz, v, num_tries, pct_freq)
        )

    ideal_freq_pct = ideal_pct(drum_sz, tick_sz)
    print("\nIdeal frequency of all matching: {:.9f}%".format(ideal_freq_pct))

if __name__ == "__main__":
    main()