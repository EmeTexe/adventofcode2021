# Part 1 and 2 in same
data = [line.rstrip() for line in open("input.txt")]

error = 0
end_score = []
mapping = {"{":"}", "[":"]", "(":")", "<":">"}
score_error = {")":3, "]":57, "}":1197, ">":25137}
score_end = {")":1, "]":2, "}":3, ">":4}
for l in data:
    end = ""
    for c in l:
        if c in mapping:
            end += mapping[c]
        elif c == end[-1]:
            end = end[:-1]
        else:
            error += score_error[c]
            break
    else:
        s = 0
        for c in end[::-1]:
            s*=5
            s+=score_end[c]
        end_score.append(s)

print(error)
print(sorted(end_score)[int((len(end_score)-1)/2)])


