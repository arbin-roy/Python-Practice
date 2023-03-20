def identifySeriesAndNthTerm(series_list, n):
    try:
        length = len(series_list)
        if series_list[1] % series_list[0] == 0:
            series_type = 'Geometric'
            if n <= length:
                return series_type, [series_list[n - 1] - 1, series_list[n - 1], series_list[n - 1] + 1]
            else:
                lElement = series_list[-1]
                for i in range(n - length):
                    lElement = lElement * series_list[0]
                return series_type, [lElement - 1, lElement, lElement + 1]
        elif series_list[1] - series_list[0] == series_list[2] - series_list[1]:
            series_type = 'Arithmetic'
            if n <= length:
                return series_type, [series_list[n - 1] - 1, series_list[n - 1], series_list[n - 1] + 1]
            else:
                lElement = series_list[-1]
                pElement = series_list[1] - series_list[0]
                for i in range(n - length):
                    lElement += pElement
                return series_type, [lElement - 1, lElement, lElement + 1]
        else:
            return 'none', [0, 0, 0]
    except IndexError:
        return 'none', [0, 0, 0]


if __name__ == "__main__":
    print(identifySeriesAndNthTerm([5, 8, 11], 7))
    print(identifySeriesAndNthTerm([3, 9, 27, 81, 243], 7))
