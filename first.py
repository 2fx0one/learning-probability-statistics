import survey

table = survey.Pregnancies()

table.ReadRecords()

print('# pregnancies ', len(table.records))

# aliveRecords = list(filter(lambda x: x.outcome == 1, table.records))
aliveRecords = [x for x in table.records if x.outcome == 1]

print('# pregnancies alive 活婴的数量', len(aliveRecords))

# aliveBirthOrderfirst = list(filter(lambda x: x.birthord == 1, aliveRecords))
aliveBirthOrderfirst = [x for x in aliveRecords if x.birthord == 1]
print('# aliveBirthOrderfirst 第一胎 ', len(aliveBirthOrderfirst))

# aliveBirthOrderOther = filter(lambda x: x.birthord != 1, aliveRecords)
aliveBirthOrderOther = [x for x in aliveRecords if x.birthord != 1]
print('# aliveBirthOrderOther 其他 ', len(aliveBirthOrderOther))

# for r in aliveBirthOrderfirst:
#     print(r.prglength)
firstAvg = sum([_.prglength for _ in aliveBirthOrderfirst]) / len(aliveBirthOrderfirst)
otherAvg = sum([_.prglength for _ in aliveBirthOrderOther]) / len(aliveBirthOrderOther)
print("first avg of prglength", firstAvg)
print("Other avg of prglength", otherAvg)

print('diff days = ', abs(firstAvg - otherAvg)*7)
print('diff hour = ', abs(firstAvg - otherAvg)*7*24)
# 1. 在 survey.py 和数据文件的目录中创建一个 first.py 文件，然后将下 面的代码输入或复制到文件中:
#   import survey
#   table = survey.Pregnancies()
#   table.ReadRecords()
#   print 'Number of pregnancies', len(table.records)
# 结果应该是 13593 条怀孕记录。
# 2. 编写一个循环遍历表(table)，计算其中活婴的数量。查阅临床结
# 果(outcome)的文档，确认你的结果跟文档中的总结一致。
# 3. 修改这个循环，将活婴的记录分成两组:一组是第一胎出生;另一 组是其他情况。再看一些出生顺序(birthord)的文档，看看你 的结果跟文档中的结果是否一致。
# 在处理新的数据集时，这种检查对于发现数据中的错误和不一致 性、检查程序中的错误以及检验对字段编码方式的理解是否正确等 都是很有用的。
# 4. 分别计算第一胎婴儿和其他婴儿的平均怀孕周期(单位是周)。两 组之间有差异吗?差异有多大?


# Number of first babies 4413
# Number of others 4735
# Mean gestation in weeks:
# First babies 38.6009517335
# Others 38.5229144667
# Difference in days 0.546260867443
