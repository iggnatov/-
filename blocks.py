# Коэффициент корреляции
cor = round(correl.correl(english_marks, info_marks),2)

# Получение данных
info_marks = get_values.info_marks()
english_marks = get_values.english_marks()

# Дополнительные команды получения данных
sleep_time = get_values.sleep_time()
math_marks = get_values.math_marks()
russ_marks = get_values.russ_marks() 
hobby = get_values.hobby()
having_pet = get_values.having_pet()
having_computer = get_values.having_computer()
sport = get_values.sport()
reading = get_values.reading()
room = get_values.room()
my1 = get_values.my1()
my2 = get_values.my2()

# Построение графика
plt.title('Коэффициент корреляции = ' + str(cor) + 
'\n' +  'Какой вывод Вы можете сделать?')
plt.plot(english_marks, info_marks, 'go')
plt.show()

# Подключение библиотек
import matplotlib.pyplot as plt
import get_values
import correl
