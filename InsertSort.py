''' 
    1.SORU: Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız
            Average case: Aradığımız sayının ortada olması
            Worst case: Aradığımız sayının sonda olması
            Best case: Aradığımız sayının dizinin en başında olması

        CEVAP:  Average case kapsamına girer çünkü aradığı sayı ortalarda yer alıyor sıralama sonunda ve yazmış oldugum koda da bu gözlemleniyor. 

    2.SORU: Big-O gösterimini yazınız.

            key=27 
            [22,27,16,2,18,6]  (n)

            key=16
            [16,22,27,2,18,6]  (n-1)

            key=2
            [2,16,22,27,18,6] (n-2)

            key=18
            [2,16,18,22,27,6] (n-3)

            key=6
            [2,6,16,18,22,27] (1)

            Dizinin sıralı olmadığı durumlarda her eleman için iç döngü çalıştırılır, bu da yaklaşık olarak n x n=n^2 işlem gerektirir.
            O(n^2)
'''

def InsertSort(array):
    for i in range(1,len(array)):
        key=array[i]
        print("key:",key)
        k=i-1
        while k>=0 and key<array[k]:
            array[k+1]=array[k]
            k-=1
            array[k+1]=key


def ArrayPrint(array):
    for i in range(len(array)):
        print(array[i],end=" ")
    print()


if __name__=="__main__":
    number_array=[22,27,16,2,18,6]
    #number_array=[7,3,5,8,2,9,4,15,6]
    InsertSort(number_array)
    ArrayPrint(number_array)


''' 
    [7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 3 adımını yazınız.

    key=3 
    [2,3,7,5,8,9,4,15,6]   (n)

    key=5
    [2,3,4,5,7,8,9,15,6]  (n-1)

    key=8
    [2,3,4,5,6,7,8,9,15] (n-2)
'''