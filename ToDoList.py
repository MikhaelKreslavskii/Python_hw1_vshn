"""
Класс для хранения списка задач
"""
class ToDoList:
    def __init__(self) -> None:
        self.tasks = []
        self.status = {
            0: "Не начата",
            1: "В процессе",
            2: "Завершена"
        }

    ###Добавление задачи
    def add_task(self, description, task_id=1, status=0):
        exist_ids = [x["id"] for x in self.tasks]
        
        if task_id in exist_ids:

            task_id = max(exist_ids) +1 
            print(f"New task id: {task_id}")
        
         

        task = {
            "id": task_id,
            "description": description,
            "status": status
        }

        self.tasks.append(task)
        print(f"Задача под id {task_id} добавлена\n")

    ##Просмотр списка задач
    def view_tasks(self):
        for task in self.tasks:
            
            print(f"Задача с id: {task['id']}\n{task['description']}\n{self.status[task['status']]}\n")
        

    ###Удаление задачи из списка
    def remove_task(self, task_id):
        exist_ids = [x["id"] for x in self.tasks]
        if task_id not in exist_ids:
            print("Данной задачи не существует")
            
        else:
            self.tasks = [x for x in self.tasks if x["id"]!=task_id]
            print(f"Задача с id {task_id} удалена")
            
        print()
        
    ##Обновление статуса
    def update_status(self, task_id, status):
        exist_ids = [x["id"] for x in self.tasks]
        if task_id not in exist_ids:
            print("Данной задачи не существует")
        elif status not in self.status.keys():
            print("Такого статуса не существует")
        else:

            for task in self.tasks:
                if task["id"]==task_id:
                    task["status"] = status
                    print("Статус задачи изменен")
        print()

    ###Выгрузка задач из файла
    def get_tasks_from_file(self, file_path):
        try:
            with open(file=file_path, mode="r", encoding="utf-8") as f:
                task_lines = f.readlines()
               
                for task_line in task_lines:
                    task_line = task_line.strip().split(sep=';')
                    
                    
                    if len(task_line)==3: 
                        
                        status_id = int(task_line[2].strip())
                        
                        
                        
                        self.add_task(task_id=int(task_line[0]), description=task_line[1], status=status_id)
                    else:
                        print("Количество данных не равно 3")


        except Exception as e:
            print(e)

    ###Загрузка задач в файл
    def load_tasks_to_file(self, file_path):
        
        try:
            with open(file=file_path,mode='w',encoding="utf-8") as f:
                for task in self.tasks:
                    f.write(f"{task['id']};{task['description']};{task['status']}\n")
                    print("Запись")
        except Exception as e:
            print(e)