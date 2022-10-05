from ztfquery import lightcurve
lcq = lightcurve.LCQuery.from_position(197.501495, +75.721959, 5)
print(lcq.data) # data strored as pandas DataFrame
lcq.show()
