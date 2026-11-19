class Queue:
    def __init__(self, *args):
        self.queue = [*args]

    def getPosition(self, name):
        return self.queue.index(name) + 1

    def isNeighbours(self, person1, person2):
        return abs(self.getPosition(person1) - self.getPosition(person2)) == 1

    def isValid(self):
        """
        Проверяем только те правила, которые уже можно проверить
        на текущем состоянии очереди.
        """

        # Юра стоит раньше Иры
        if "Юра" in self.queue and "Ира" in self.queue and self.getPosition("Юра") > self.getPosition("Ира"):
            return False

        # Юра стоит после Коли
        if "Коля" in self.queue and "Юра" in self.queue and self.getPosition("Коля") > self.getPosition("Юра"):
            return False

        # Оля и Коля не стоят рядом
        if "Оля" in self.queue and "Коля" in self.queue and self.isNeighbours("Оля", "Коля"):
            return False

        # Саша не находится рядом ни с Колей, ни с Юрой, ни с Олей
        if "Саша" in self.queue:
            for person in ["Коля", "Юра", "Оля"]:
                if (person in self.queue) and self.isNeighbours("Саша", person):
                    return False

        return True

    def mix(self):
        """
        Backtracking: строим очередь слева направо.
        Возвращает первую найденную корректную перестановку.
        """

        people = self.queue.copy()
        self.queue = []

        def backtrack():
            # Все люди расставлены
            if len(self.queue) == len(people):
                return True

            for person in people:
                # Уже поставлен
                if person in self.queue:
                    continue

                # Делаем шаг
                self.queue.append(person)

                # Если текущая частичная очередь допустима,
                # продолжаем строить её
                if self.isValid() & backtrack():
                    return True

                # Текущий вариант оказался тупиком.
                # Откатываем последний шаг.
                self.queue.pop()

            return False

        if backtrack():
            return self.queue

        # Решения нет
        self.queue = people
        return None


queue = Queue("Юра", "Ира", "Оля", "Саша", "Коля")

result = queue.mix()

print("Результат:", result)
print("Корректно:", queue.isValid())
