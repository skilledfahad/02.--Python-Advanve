import statistics

# score = [6, 7, 2, 6, 3, 5, 5, 5, 2, 5, 6, 1, 2]
#
# a = statistics.mean(score)  # average
# print(a)
# b = statistics.median(score)  # data mid point
# print(b)
# c = statistics.mode(score)  # most viewed
# print(c)

# score_2 = [30, 90]
# print(statistics.median_low(score_2))
# print(statistics.median(score_2))
# print(statistics.median_high(score_2), "\n")
#
# score_1 = [20, 40, 60, 80, 100]
# print((statistics.median_low(score_1)))
# print(statistics.median(score_1))
# print(statistics.median_high(score_1), "\n")
#
grades=[70,90,50,85]
# x=statistics.mean(grades)
# print(x)
# print(statistics.variance(grades,x))  # statistics.variance(grades)

grades1=[70,70,70,70]
y=statistics.mean(grades1)
print(y)
print(statistics.variance(grades1))

print(statistics.stdev(grades1)) # low deviasion meance datas are not so different from each other
print(statistics.stdev(grades))  # dev= sqrt of (variance)