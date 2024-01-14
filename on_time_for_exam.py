hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

exam_time = hour_exam * 60 + minute_exam
exam_arrive = hour_arrive * 60 + minute_arrive
diff = exam_arrive - exam_time
if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm:02d} hours after the start")
elif diff >= -30:
    print("On time")
    if not diff == 0:
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    if diff > -60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm:02d} hours before the start")


