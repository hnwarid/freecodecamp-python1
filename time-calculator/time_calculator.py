def add_time(start, duration, day=None):
    days_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    days_list = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meridian = "AM"

    begin_var, start_meridian = start.split()
    hr_var, min_var = begin_var.split(":")
    hr_add, min_add = duration.split(":")
    if start_meridian == "PM":
        hr_var = int(hr_var) + 12

    sum_hr = int(hr_var) + int(hr_add)
    sum_min = int(min_var) + int(min_add)

    if sum_min > 60:
        sum_min %= 60
        sum_hr += 1
    days_adds = sum_hr // 24
    sum_hr %= 24

    if sum_hr > 12:
        sum_hr %= 12
        meridian = "PM"
    if sum_hr == 12:
        meridian = "PM"
    if sum_hr == 0:
        sum_hr += 12
        meridian = "AM"
    if sum_min < 10:
        sum_min = "0" + str(sum_min)

    if day is None:
        if days_adds == 0:
            new_time = "{}:{} {}".format(sum_hr, sum_min, meridian)
        elif days_adds == 1:
            new_time = "{}:{} {} (next day)".format(sum_hr, sum_min, meridian)
        else:
            new_time = "{}:{} {} ({} days later)".format(sum_hr, sum_min, meridian, days_adds)

    elif day is not None:
        day = day.lower().capitalize()
        day_value = days_dict[day]
        day_value += days_adds
        if day_value > 7:
            day_value %= 7
        day = days_list[day_value]
        if days_adds == 0:
            new_time = "{}:{} {}, {}".format(sum_hr, sum_min, meridian, day)
        elif days_adds == 1:
            new_time = "{}:{} {}, {} (next day)".format(sum_hr, sum_min, meridian, day)
        else:
            new_time = "{}:{} {}, {} ({} days later)".format(sum_hr, sum_min, meridian, day, days_adds)

    return new_time
