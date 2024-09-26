from ToDoList import ToDoList
my_todoList = ToDoList()

FILE_PATH = "todolist.txt"
my_todoList.get_tasks_from_file(file_path=FILE_PATH)

my_todoList.view_tasks()

###Добвление задач
my_todoList.add_task("Помыть посуду")
my_todoList.add_task("Сделать задание по Python")
my_todoList.add_task("Приготовить ужин")



my_todoList.view_tasks() # просмотр текущих задач

##Изменение статуса
my_todoList.update_status(2, "Abracadabra") #попытка присвоить несуществующий статус
my_todoList.update_status(2, "В процессе")

my_todoList.view_tasks()

##удаление задач
my_todoList.remove_task(7) ##удаление задачи с несуществующим id
my_todoList.remove_task(1)

my_todoList.view_tasks()

my_todoList.load_tasks_to_file(file_path=FILE_PATH)