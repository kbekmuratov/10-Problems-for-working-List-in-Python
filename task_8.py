# Задача 8: Количество элементов в списке
# Создай список с названиями пяти городов. Напиши программу, которая подсчитает, 
# сколько городов в списке, и выведет сообщение вроде "У меня есть 5 любимых городов."

sentence = ['London', 'NY', 'Astana', 'Almaty','Syndey']

def find_count(sentence):
    count = 0
    
    for i in sentence:
        count+=1
    return count

c = find_count(sentence)

print(c)

