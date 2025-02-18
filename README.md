# NCC multiple choice grader
An automatic multiple choice test grader

# How to Install
Run `pip install -r requirements.txt`

# How to Use
- use `create_test_sheets.py` to create test sheet
- create `test.csv` to save test answer
- put the test answer on `test.jpg`
- run the `run.py` to get the test result

# Demo

## Test.csv
```csv
1;D;1
2;B;1
3;C;1
4;C;1
5;B;1
6;E;1
7;A;1
8;D;1
9;B;1
10;A;1
11;A;1
12;C;1
13;E;1
14;B;1
15;B;1
16;D;1
17;B;1
18;A;1
19;A;1
20;A;1
21;A;1
22;A;1
23;A;1
24;A;1
25;C;1
26;B;1
27;B;1
28;A;1
29;D;1
30;B;1
31;C;1
32;D;1
33;B;1
```

## Test sheet
![](test_sheet.png)

## Test
![](test.jpg)

## Result
```bash
▶ python3 run.py
b'Sully Chen'
Result: 10/33
[b'Sully Chen']
```

# Video
https://youtu.be/Nd7bdpKR1kI
