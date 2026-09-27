import math
import random

def get_min_moves(n):
    
    k = 0
    while (k * (k + 1)) // 2 < n:
        k += 1
    return k

def find_breaking_floor(n, actual_breaking_floor):
    k = get_min_moves(n)
    step_size = k
    current_floor = 0
    moves_count = 0
    
    print(f"\n[Սիմուլյացիա] Իրականում ձուն ջարդվում է **{actual_breaking_floor}** հարկում:")
    print(f"Առավելագույն նախատեսված քայլերի քանակը այս շենքի համար՝ {k}\n")
    
    while current_floor < n and step_size > 0:
        current_floor += step_size
        moves_count += 1
        
        if current_floor > n:
            current_floor = n
            
        print(f"Քայլ {moves_count}: Նետում ենք {current_floor}-րդ հարկից...")
        
        if current_floor >= actual_breaking_floor:
            print(f" -> Ձուն **ջարդվեց** {current_floor}-րդ հարկում։")       
            start_search = current_floor - step_size + 1
            end_search = current_floor - 1
            
            print(f" -> Անցնում ենք 2-րդ գնդակին և ստուգում {start_search}-ից մինչև {end_search} հարկերը։")
            
            for f in range(start_search, end_search + 1):
                moves_count += 1
                print(f"   Քայլ {moves_count}: Նետում ենք {f}-րդ հարկից...")
                if f >= actual_breaking_floor:
                    print(f"\n✓ Գտնվեց! Ձուն ջարդվում է **{f}**-րդ հարկում։")
                    print(f"Ընդհանուր կատարված քայլեր՝ {moves_count}")
                    return f
            

            print(f"\n✓ Գտնվեց! Ձուն ջարդվում է **{current_floor}**-րդ հարկում։")
            print(f"Ընդհանուր կատարված քայլեր՝ {moves_count}")
            return current_floor
        else:
            print(f" -> Ձուն չջարդվեց։")
            step_size -= 1


if __name__ == "__main__":
    try:
        n = int(input("Մուտքագրեք շենքի հարկերի քանակը (օրինակ՝ 64 կամ 100): "))
        if n <= 0:
            print("Խնդրում եմ մուտքագրել դրական թիվ:")
        else:
            actual_floor = random.randint(1, n)
            find_breaking_floor(n, actual_floor)
            
    except ValueError:
        print("Խնդրում եմ մուտքագրել վավեր ամբողջ թիվ:")
