NUMBER_OF_WORKERS = 5

JOB_DELAY = 60

JOBS = [(None, None) for i in range(NUMBER_OF_WORKERS)]

DEBUG = True


def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def get_dependencies(lines):

    dependencies = {}
    for line in lines:
        before = line.split()[1]
        after = line.split()[7]

        if after not in dependencies:
            dependencies[after] = []

        if before not in dependencies:
            dependencies[before] = []

        dependencies[after].append(before)

    return dependencies


def get_time_for_job(job):
    return ord(job) - ord('A') + JOB_DELAY


def main():

    available_slots = NUMBER_OF_WORKERS
    done = []
    dependencies = get_dependencies(read_input())

    time_slot = 0

    if DEBUG:
        print ('Slot\t', end='')
        for i in range(NUMBER_OF_WORKERS):
            print ('W{}\t'.format(i + 1), end='')
        print('Done')

    while len(dependencies.keys()) > 0:

        jobs_done = []

        for i in range(len(JOBS)):
            if JOBS[i][0] != None:
                if JOBS[i][1] == 0:
                    jobs_done.append(JOBS[i][0])
                    JOBS[i] = (None, None)
                    available_slots += 1
                else:
                    JOBS[i] = (JOBS[i][0], JOBS[i][1] - 1)

        for job in jobs_done:
            for k, v in dependencies.items():
                if job in v:
                    v.remove(job)

        job_candidates = []
        for k, v in dependencies.items():
            if len(v) > 0:
                continue
            if k in jobs_done:
                continue
            already_running = False
            for j in JOBS:
                if j[0] == k:
                    already_running = True
            if already_running:
                continue
            job_candidates.append(k)

        print ('job candidates', job_candidates)
        chosen_jobs = sorted(job_candidates)[:available_slots]
        print ('chosen jobs', chosen_jobs)
        print()

        for pending_job in chosen_jobs:
            for i in range(len(JOBS)):
                if JOBS[i][0] == None:
                    JOBS[i] = (pending_job, get_time_for_job(pending_job))
                    available_slots -= 1
                    break

        for job in jobs_done:
            del dependencies[job]
        done += jobs_done

        if DEBUG:
            print ('{}\t'.format(time_slot), end='')
            for i in range(NUMBER_OF_WORKERS):
                print ('{}\t'.format(JOBS[i][0] if JOBS[i][0] != None else '.'), end='')
            print(''.join(done))

        time_slot += 1

    print (time_slot - 1)



if __name__ == '__main__':
    main()
