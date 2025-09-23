import random

def test_random():
    #สร้างตัวแปร random_number ตัวแปรคือการสุ่มเลขระหว่าง 1 - 10
    random_number = random.randint(1, 10)
    
    guess_number = input ("Guess the number: ")
    guess_number = int(guess_number) #แปลง str to int ไม่งั้นจะใช้เครื่องหมายไม่ได้
    
    print("!!Guess Number between (1-10)")

    if random_number == guess_number:
        print("!!!Congrulations!!!")

    elif random_number < guess_number:
        print("Too high")

    elif random_number > guess_number:
        print("Too low")


    #print(random_number)

test_random() #ตัวเรียกใช้ function 