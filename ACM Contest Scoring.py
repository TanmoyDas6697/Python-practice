import sys

def solve_contest():
    wrong_attempts = {}

    solved_problems = set()
    
    total_solved = 0
    total_score = 0

    for line in sys.stdin:
        line = line.strip()
        if line == "-1":
            break
        
        parts = line.split()
        if len(parts) < 3:
            continue
            
        time = int(parts[0])
        problem = parts[1]
        result = parts[2]

        if problem in solved_problems:
            continue

        if result == "right":
            total_solved += 1
            solved_problems.add(problem)
            
            penalties = wrong_attempts.get(problem, 0) * 20
            total_score += (time + penalties)
        else:
            wrong_attempts[problem] = wrong_attempts.get(problem, 0) + 1

    print(f"{total_solved} {total_score}")

if __name__ == "__main__":
    solve_contest()