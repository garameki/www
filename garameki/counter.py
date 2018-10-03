#!/usr/bin/env python3


# CGIのヘッダ
print("Content-type: text/html; charset=utf-8");
print("");

# HTLMのヘッダ
print("<!DOCTYPE html><head><META http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body style='color:white;'>");

# コンテンツ 
file_name = "./counter.txt"
number = 0
try:
    file = open(file_name)
    data = file.read()
    print('<div style="text-align:center;">')
    print(data)
    print("</div>")
    number = int(data) + 1

except Exception as e:
    print(e)
finally:
    file.close()


try:
    file = open(file_name, 'w')
    file.write(str(number))
except Exception as e:
    print(e)
finally:
    file.close()

print("</body></html>");



